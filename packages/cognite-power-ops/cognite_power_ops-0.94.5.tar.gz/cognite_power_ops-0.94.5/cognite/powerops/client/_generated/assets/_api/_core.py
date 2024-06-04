from __future__ import annotations

import math
import re
import warnings
from itertools import groupby

from collections import Counter, defaultdict, UserList
from collections.abc import Sequence, Collection
from dataclasses import dataclass, field
from typing import Generic, Literal, Any, Iterator, Protocol, SupportsIndex, TypeVar, overload, cast, Union

from cognite.client import CogniteClient
from cognite.client import data_modeling as dm
from cognite.client.data_classes import TimeSeriesList
from cognite.client.data_classes.data_modeling.instances import Instance
from cognite.client.data_classes.data_modeling.instances import InstanceAggregationResultList

from cognite.powerops.client._generated.assets.data_classes._core import (
    DomainModel,
    DomainModelCore,
    DomainModelWrite,
    DomainRelationWrite,
    PageInfo,
    GraphQLList,
    ResourcesWriteResult,
    T_DomainModel,
    T_DomainModelWrite,
    T_DomainModelWriteList,
    T_DomainModelList,
    T_DomainRelation,
    T_DomainRelationWrite,
    T_DomainRelationList,
    DomainModelCore,
    DomainRelation,
)
from cognite.powerops.client._generated.assets import data_classes


DEFAULT_LIMIT_READ = 25
DEFAULT_QUERY_LIMIT = 3
INSTANCE_QUERY_LIMIT = 1_000
# This is the actual limit of the API, we typically set it to a lower value to avoid hitting the limit.
ACTUAL_INSTANCE_QUERY_LIMIT = 10_000
IN_FILTER_LIMIT = 5_000

Aggregations = Literal["avg", "count", "max", "min", "sum"]

_METRIC_AGGREGATIONS_BY_NAME = {
    "avg": dm.aggregations.Avg,
    "count": dm.aggregations.Count,
    "max": dm.aggregations.Max,
    "min": dm.aggregations.Min,
    "sum": dm.aggregations.Sum,
}

_T_co = TypeVar("_T_co", covariant=True)


# Source from https://github.com/python/typing/issues/256#issuecomment-1442633430
# This works because str.__contains__ does not accept an object (either in typeshed or at runtime)
class SequenceNotStr(Protocol[_T_co]):
    @overload
    def __getitem__(self, index: SupportsIndex, /) -> _T_co: ...

    @overload
    def __getitem__(self, index: slice, /) -> Sequence[_T_co]: ...

    def __contains__(self, value: object, /) -> bool: ...

    def __len__(self) -> int: ...

    def __iter__(self) -> Iterator[_T_co]: ...

    def index(self, value: Any, /, start: int = 0, stop: int = ...) -> int: ...

    def count(self, value: Any, /) -> int: ...

    def __reversed__(self) -> Iterator[_T_co]: ...


class NodeReadAPI(Generic[T_DomainModel, T_DomainModelList]):
    def __init__(
        self,
        client: CogniteClient,
        sources: dm.ViewIdentifier | Sequence[dm.ViewIdentifier] | dm.View | Sequence[dm.View] | None,
        class_type: type[T_DomainModel],
        class_list: type[T_DomainModelList],
        view_by_read_class: dict[type[DomainModelCore], dm.ViewId],
    ):
        self._client = client
        self._sources = sources
        self._class_type = class_type
        self._class_list = class_list
        self._view_by_read_class = view_by_read_class

    def _delete(self, external_id: str | Sequence[str], space: str) -> dm.InstancesDeleteResult:
        if isinstance(external_id, str):
            return self._client.data_modeling.instances.delete(nodes=(space, external_id))
        else:
            return self._client.data_modeling.instances.delete(
                nodes=[(space, id) for id in external_id],
            )

    @overload
    def _retrieve(
        self,
        external_id: str,
        space: str,
        retrieve_edges: bool = False,
        edge_api_name_type_direction_view_id_penta: (
            list[tuple[EdgeAPI, str, dm.DirectRelationReference, Literal["outwards", "inwards"], dm.ViewId]] | None
        ) = None,
    ) -> T_DomainModel | None: ...

    @overload
    def _retrieve(
        self,
        external_id: SequenceNotStr[str],
        space: str,
        retrieve_edges: bool = False,
        edge_api_name_type_direction_view_id_penta: (
            list[tuple[EdgeAPI, str, dm.DirectRelationReference, Literal["outwards", "inwards"], dm.ViewId]] | None
        ) = None,
    ) -> T_DomainModelList: ...

    def _retrieve(
        self,
        external_id: str | SequenceNotStr[str],
        space: str,
        retrieve_edges: bool = False,
        edge_api_name_type_direction_view_id_penta: (
            list[tuple[EdgeAPI, str, dm.DirectRelationReference, Literal["outwards", "inwards"], dm.ViewId]] | None
        ) = None,
    ) -> T_DomainModel | T_DomainModelList | None:
        is_multiple = True
        if isinstance(external_id, str):
            node_ids = (space, external_id)
            is_multiple = False
        else:
            node_ids = [(space, ext_id) for ext_id in external_id]

        instances = self._client.data_modeling.instances.retrieve(nodes=node_ids, sources=self._sources)
        nodes = self._class_list([self._class_type.from_instance(node) for node in instances.nodes])

        if retrieve_edges and nodes:
            self._retrieve_and_set_edge_types(nodes, edge_api_name_type_direction_view_id_penta)

        if is_multiple:
            return nodes
        elif not nodes:
            return None
        else:
            return nodes[0]

    def _search(
        self,
        view_id: dm.ViewId,
        query: str,
        properties_by_field: dict[str, str],
        properties: str | Sequence[str],
        filter_: dm.Filter | None = None,
        limit: int = DEFAULT_LIMIT_READ,
    ) -> T_DomainModelList:
        if isinstance(properties, str):
            properties = [properties]

        if properties:
            properties = [properties_by_field.get(prop, prop) for prop in properties]

        nodes = self._client.data_modeling.instances.search(
            view=view_id, query=query, instance_type="node", properties=properties, filter=filter_, limit=limit
        )
        return self._class_list([self._class_type.from_instance(node) for node in nodes])

    @overload
    def _aggregate(
        self,
        view_id: dm.ViewId,
        aggregate: (
            Aggregations
            | dm.aggregations.MetricAggregation
            | Sequence[Aggregations]
            | Sequence[dm.aggregations.MetricAggregation]
        ),
        properties_by_field: dict[str, str],
        properties: str | Sequence[str] | None = None,
        group_by: None = None,
        query: str | None = None,
        search_properties: str | Sequence[str] | None = None,
        limit: int = DEFAULT_LIMIT_READ,
        filter: dm.Filter | None = None,
    ) -> list[dm.aggregations.AggregatedNumberedValue]: ...

    @overload
    def _aggregate(
        self,
        view_id: dm.ViewId,
        aggregate: (
            Aggregations
            | dm.aggregations.MetricAggregation
            | Sequence[Aggregations]
            | Sequence[dm.aggregations.MetricAggregation]
        ),
        properties_by_field: dict[str, str],
        properties: str | Sequence[str] = None,
        group_by: str | Sequence[str] | None = None,
        query: str | None = None,
        search_properties: str | Sequence[str] | None = None,
        limit: int = DEFAULT_LIMIT_READ,
        filter: dm.Filter | None = None,
    ) -> InstanceAggregationResultList: ...

    def _aggregate(
        self,
        view_id: dm.ViewId,
        aggregate: (
            Aggregations
            | dm.aggregations.MetricAggregation
            | Sequence[Aggregations]
            | Sequence[dm.aggregations.MetricAggregation]
        ),
        properties_by_field: dict[str, str],
        properties: str | Sequence[str] | None = None,
        group_by: str | Sequence[str] | None = None,
        query: str | None = None,
        search_properties: str | Sequence[str] | None = None,
        limit: int = DEFAULT_LIMIT_READ,
        filter: dm.Filter | None = None,
    ) -> list[dm.aggregations.AggregatedNumberedValue] | InstanceAggregationResultList:
        if isinstance(group_by, str):
            group_by = [group_by]

        if group_by:
            group_by = [properties_by_field.get(prop, prop) for prop in group_by]

        if isinstance(search_properties, str):
            search_properties = [search_properties]

        if search_properties:
            search_properties = [properties_by_field.get(prop, prop) for prop in search_properties]

        if isinstance(properties, str):
            properties = [properties]

        if properties:
            properties = [properties_by_field.get(prop, prop) for prop in properties]

        if isinstance(aggregate, (str, dm.aggregations.MetricAggregation)):
            aggregate = [aggregate]

        if properties is None and (invalid := [agg for agg in aggregate if isinstance(agg, str) and agg != "count"]):
            raise ValueError(f"Cannot aggregate on {invalid} without specifying properties")

        aggregates = []
        for agg in aggregate:
            if isinstance(agg, dm.aggregations.MetricAggregation):
                aggregates.append(agg)
            elif isinstance(agg, str):
                if agg == "count" and properties is None:
                    aggregates.append(dm.aggregations.Count("externalId"))
                elif properties is None:
                    raise ValueError(f"Cannot aggregate on {agg} without specifying properties")
                else:
                    for prop in properties:
                        aggregates.append(_METRIC_AGGREGATIONS_BY_NAME[agg](prop))
            else:
                raise TypeError(f"Expected str or MetricAggregation, got {type(agg)}")

        return self._client.data_modeling.instances.aggregate(
            view=view_id,
            aggregates=aggregates,
            group_by=group_by,
            instance_type="node",
            query=query,
            properties=search_properties,
            filter=filter,
            limit=limit,
        )

    def _histogram(
        self,
        view_id: dm.ViewId,
        property: str,
        interval: float,
        properties_by_field: dict[str, str],
        query: str | None = None,
        search_properties: str | Sequence[str] | None = None,
        limit: int = DEFAULT_LIMIT_READ,
        filter: dm.Filter | None = None,
    ) -> dm.aggregations.HistogramValue:
        property = properties_by_field.get(property, property)

        if isinstance(search_properties, str):
            search_properties = [search_properties]
        if search_properties:
            search_properties = [properties_by_field.get(prop, prop) for prop in search_properties]

        return self._client.data_modeling.instances.histogram(
            view=view_id,
            histograms=dm.aggregations.Histogram(property, interval),
            instance_type="node",
            query=query,
            properties=search_properties,
            filter=filter,
            limit=limit,
        )

    def _list(
        self,
        limit: int,
        filter: dm.Filter,
        retrieve_edges: bool = False,
        edge_api_name_type_direction_view_id_penta: (
            list[tuple[EdgeAPI, str, dm.DirectRelationReference, Literal["outwards", "inwards"]]] | None
        ) = None,
    ) -> T_DomainModelList:
        nodes = self._client.data_modeling.instances.list(
            instance_type="node", sources=self._sources, limit=limit, filter=filter
        )
        node_list = self._class_list([self._class_type.from_instance(node) for node in nodes])
        if retrieve_edges and node_list:
            self._retrieve_and_set_edge_types(node_list, edge_api_name_type_direction_view_id_penta)

        return node_list

    def _retrieve_and_set_edge_types(
        self,
        nodes: T_DomainModelList,
        edge_api_name_type_direction_view_id_penta: (
            list[tuple[EdgeAPI, str, dm.DirectRelationReference, Literal["outwards", "inwards"], dm.ViewId]] | None
        ) = None,
    ):
        for edge_type, values in groupby(edge_api_name_type_direction_view_id_penta or [], lambda x: x[2].as_tuple()):
            edges: dict[dm.EdgeId, dm.Edge] = {}
            value_list = list(values)
            for edge_api, edge_name, edge_type, direction, view_id in value_list:
                is_type = dm.filters.Equals(
                    ["edge", "type"],
                    {"space": edge_type.space, "externalId": edge_type.external_id},
                )
                if len(ids := nodes.as_node_ids()) > IN_FILTER_LIMIT:
                    filter_ = is_type
                else:
                    is_nodes = dm.filters.In(
                        ["edge", "startNode"] if direction == "outwards" else ["edge", "endNode"],
                        values=[id_.dump(camel_case=True, include_instance_type=False) for id_ in ids],
                    )
                    filter_ = dm.filters.And(is_type, is_nodes)
                result = edge_api._list(limit=-1, filter_=filter_)
                edges.update({edge.as_id(): edge for edge in result})
            edge_list = list(edges.values())
            if len(value_list) == 1:
                _, edge_name, _, direction, _ = value_list[0]
                self._set_edges(nodes, edge_list, edge_name, direction)
            else:
                # This is an 'edge' case where we have view with multiple edges of the same type.
                edge_by_end_node: dict[tuple[str, str], list[dm.Edge]] = defaultdict(list)
                for edge in edge_list:
                    node_id = edge.end_node.as_tuple() if direction == "outwards" else edge.start_node.as_tuple()
                    edge_by_end_node[node_id].append(edge)

                for no, (edge_api, edge_name, _, direction, view_id) in enumerate(value_list):
                    if not edge_by_end_node:
                        break
                    if no == len(value_list) - 1:
                        # Last edge, use all remaining nodes
                        attribute_edges = [e for e_list in edge_by_end_node.values() for e in e_list]
                    else:
                        existing = self._client.data_modeling.instances.retrieve(
                            nodes=list(edge_by_end_node), sources=view_id
                        )
                        attribute_edges = []
                        for node in existing.nodes:
                            attribute_edge = edge_by_end_node.pop(node.as_id().as_tuple(), [])
                            attribute_edges.extend(attribute_edge)

                    self._set_edges(nodes, attribute_edges, edge_name, direction)

    @staticmethod
    def _set_edges(
        nodes: Sequence[DomainModel],
        edges: Sequence[dm.Edge],
        edge_name: str,
        direction: Literal["outwards", "inwards"],
    ):
        edges_by_node: dict[tuple, list] = defaultdict(list)
        for edge in edges:
            node_id = edge.start_node.as_tuple() if direction == "outwards" else edge.end_node.as_tuple()
            edges_by_node[node_id].append(edge)

        for node in nodes:
            node_id = node.as_tuple_id()
            if node_id in edges_by_node:
                setattr(
                    node,
                    edge_name,
                    [
                        edge.end_node.external_id if direction == "outwards" else edge.start_node.external_id
                        for edge in edges_by_node[node_id]
                    ],
                )


class NodeAPI(
    Generic[T_DomainModel, T_DomainModelWrite, T_DomainModelList], NodeReadAPI[T_DomainModel, T_DomainModelList]
):
    def __init__(
        self,
        client: CogniteClient,
        sources: dm.ViewIdentifier | Sequence[dm.ViewIdentifier] | dm.View | Sequence[dm.View] | None,
        class_type: type[T_DomainModel],
        class_list: type[T_DomainModelList],
        class_write_list: type[T_DomainModelWriteList],
        view_by_read_class: dict[type[DomainModelCore], dm.ViewId],
    ):
        super().__init__(client, sources, class_type, class_list, view_by_read_class)
        self._class_write_list = class_write_list

    def _apply(
        self, item: T_DomainModelWrite | Sequence[T_DomainModelWrite], replace: bool = False, write_none: bool = False
    ) -> ResourcesWriteResult:
        if isinstance(item, DomainModelWrite):
            instances = item.to_instances_write(self._view_by_read_class, write_none)
        else:
            instances = self._class_write_list(item).to_instances_write(self._view_by_read_class, write_none)
        result = self._client.data_modeling.instances.apply(
            nodes=instances.nodes,
            edges=instances.edges,
            auto_create_start_nodes=True,
            auto_create_end_nodes=True,
            replace=replace,
        )
        time_series = []
        if instances.time_series:
            time_series = self._client.time_series.upsert(instances.time_series, mode="patch")

        return ResourcesWriteResult(result.nodes, result.edges, TimeSeriesList(time_series))


class EdgeAPI:
    def __init__(self, client: CogniteClient):
        self._client = client

    def _list(
        self,
        limit: int = DEFAULT_LIMIT_READ,
        filter_: dm.Filter | None = None,
    ) -> dm.EdgeList:
        return self._client.data_modeling.instances.list("edge", limit=limit, filter=filter_)


class EdgePropertyAPI(EdgeAPI, Generic[T_DomainRelation, T_DomainRelationWrite, T_DomainRelationList]):
    def __init__(
        self,
        client: CogniteClient,
        view_by_read_class: dict[type[DomainModelCore], dm.ViewId],
        class_type: type[T_DomainRelation],
        class_write_type: type[T_DomainRelationWrite],
        class_list: type[T_DomainRelationList],
    ):
        super().__init__(client)
        self._view_by_read_class = view_by_read_class
        self._view_id = view_by_read_class[class_type]
        self._class_type = class_type
        self._class_write_type = class_write_type
        self._class_list = class_list

    def _list(
        self,
        limit: int = DEFAULT_LIMIT_READ,
        filter_: dm.Filter | None = None,
    ) -> T_DomainRelationList:
        edges = self._client.data_modeling.instances.list("edge", limit=limit, filter=filter_, sources=[self._view_id])
        return self._class_list([self._class_type.from_instance(edge) for edge in edges])


@dataclass
class QueryStep:
    # Setup Variables
    name: str
    expression: dm.query.ResultSetExpression
    max_retrieve_limit: int
    select: dm.query.Select
    result_cls: type[DomainModelCore] | None = None
    is_single_direct_relation: bool = False

    # Query Variables
    cursor: str | None = None
    total_retrieved: int = 0
    results: list[Instance] = field(default_factory=list)
    last_batch_count: int = 0

    def update_expression_limit(self) -> None:
        if self.is_unlimited:
            self.expression.limit = ACTUAL_INSTANCE_QUERY_LIMIT
        else:
            self.expression.limit = max(min(INSTANCE_QUERY_LIMIT, self.max_retrieve_limit - self.total_retrieved), 0)

    @property
    def is_unlimited(self) -> bool:
        return self.max_retrieve_limit in {None, -1, math.inf}

    @property
    def is_finished(self) -> bool:
        return (
            (not self.is_unlimited and self.total_retrieved >= self.max_retrieve_limit)
            or self.cursor is None
            or self.last_batch_count == 0
            # Single direct relations are dependent on the parent node,
            # so we assume that the parent node is the limiting factor.
            or self.is_single_direct_relation
        )


class QueryBuilder(UserList, Generic[T_DomainModelList]):
    # The unique string is in case the data model has a field that ends with _\d+. This will make sure we don't
    # clean the name of the field.
    _unique_str = "a418"
    _name_pattern = re.compile(r"_a418\d+$")

    def __init__(self, result_cls: type[T_DomainModelList], nodes: Collection[QueryStep] = None):
        super().__init__(nodes or [])
        self._result_cls = result_cls

    # The dunder implementations are to get proper type hints
    def __iter__(self) -> Iterator[QueryStep]:
        return super().__iter__()

    @overload
    def __getitem__(self, item: int) -> QueryStep: ...

    @overload
    def __getitem__(self: type[QueryBuilder[T_DomainModelList]], item: slice) -> QueryBuilder[T_DomainModelList]: ...

    def __getitem__(self, item: int | slice) -> QueryStep | QueryBuilder[T_DomainModelList]:
        if isinstance(item, slice):
            return self.__class__(self.data[item])
        elif isinstance(item, int):
            return self.data[item]
        else:
            raise TypeError(f"Expected int or slice, got {type(item)}")

    def next_name(self, name: str) -> str:
        counter = Counter(self._clean_name(step.name) for step in self)
        if name in counter:
            return f"{name}_{self._unique_str}{counter[name]}"
        return name

    def _clean_name(self, name: str) -> str:
        return self._name_pattern.sub("", name)

    def reset(self):
        for expression in self:
            expression.total_retrieved = 0
            expression.cursor = None
            expression.results = []

    def update_expression_limits(self) -> None:
        for expression in self:
            expression.update_expression_limit()

    def build(self) -> dm.query.Query:
        with_ = {expression.name: expression.expression for expression in self}
        select = {expression.name: expression.select for expression in self if expression.select}
        cursors = self.cursors

        return dm.query.Query(with_=with_, select=select, cursors=cursors)

    @property
    def cursors(self) -> dict[str, str | None]:
        return {expression.name: expression.cursor for expression in self}

    def update(self, batch: dm.query.QueryResult):
        for expression in self:
            if expression.name not in batch:
                continue
            expression.last_batch_count = len(batch[expression.name])
            expression.total_retrieved += expression.last_batch_count
            expression.cursor = batch.cursors.get(expression.name)
            expression.results.extend(batch[expression.name].data)

    @property
    def is_finished(self):
        return all(expression.is_finished for expression in self)

    def unpack(self) -> T_DomainModelList:
        nodes_by_type: dict[str | None, dict[tuple[str, str], DomainModel]] = defaultdict(dict)
        edges_by_type_by_source_node: dict[tuple[str, str, str], dict[tuple[str, str], list[dm.Edge]]] = defaultdict(
            lambda: defaultdict(list)
        )
        relation_by_type_by_start_node: dict[tuple[str, str], dict[tuple[str, str], list[DomainRelation]]] = (
            defaultdict(lambda: defaultdict(list))
        )
        node_attribute_to_node_type: dict[str, str] = {}

        for step in self:
            name = step.name
            from_ = step.expression.from_

            if isinstance(step.expression, dm.query.NodeResultSetExpression) and from_:
                node_attribute_to_node_type[from_] = name

            if step.result_cls is None:  # This is a data model edge.
                for edge in step.results:
                    edge = cast(dm.Edge, edge)
                    edge_source = edge.start_node if step.expression.direction == "outwards" else edge.end_node
                    edges_by_type_by_source_node[(from_, name, step.expression.direction)][
                        (edge_source.space, edge_source.external_id)
                    ].append(edge)
            elif issubclass(step.result_cls, DomainModel):
                for node in step.results:
                    domain = step.result_cls.from_instance(node)
                    if (id_ := domain.as_tuple_id()) not in nodes_by_type[name]:
                        nodes_by_type[name][id_] = domain
            elif issubclass(step.result_cls, DomainRelation):
                for edge in step.results:
                    domain = step.result_cls.from_instance(edge)
                    relation_by_type_by_start_node[(from_, name)][domain.start_node.as_tuple()].append(domain)

            # Link direct relations
            is_direct_relation = (
                isinstance(step.expression, dm.query.NodeResultSetExpression) and from_ and from_ in nodes_by_type
            )
            if is_direct_relation:
                end_nodes = nodes_by_type[name]
                attribute_name = node_attribute_to_node_type[from_]
                for parent_node in nodes_by_type[from_].values():
                    attribute_value = getattr(parent_node, attribute_name)
                    if isinstance(attribute_value, str):
                        end_id = (parent_node.space, attribute_value)
                    elif isinstance(attribute_value, dm.NodeId):
                        end_id = attribute_value.space, attribute_value.external_id
                    else:
                        continue
                    if end_id in end_nodes:
                        setattr(parent_node, attribute_name, end_nodes[end_id])
                    else:
                        warnings.warn(f"Unpacking of query result: Could not find node with id {end_id}", stacklevel=2)

        for (node_name, node_attribute), relations_by_start_node in relation_by_type_by_start_node.items():
            for node in nodes_by_type[node_name].values():
                setattr(node, node_attribute, relations_by_start_node.get(node.as_tuple_id(), []))
            for relations in relations_by_start_node.values():
                for relation in relations:
                    edge_name = relation.edge_type.external_id.split(".")[-1]
                    if (nodes := nodes_by_type.get(edge_name)) and (
                        node := nodes.get((relation.end_node.space, relation.end_node.external_id))
                    ):
                        # Relations always have an end node.
                        relation.end_node = node

        for (node_name, node_attribute, direction), edges_by_source_node in edges_by_type_by_source_node.items():
            for node in nodes_by_type[node_name].values():
                edges = edges_by_source_node.get(node.as_tuple_id(), [])
                nodes = nodes_by_type.get(node_attribute_to_node_type.get(node_attribute), {})
                if direction == "outwards":
                    setattr(
                        node, node_attribute, [node for edge in edges if (node := nodes.get(edge.end_node.as_tuple()))]
                    )
                else:  # inwards
                    setattr(
                        node,
                        node_attribute,
                        [node for edge in edges if (node := nodes.get(edge.start_node.as_tuple()))],
                    )

        return self._result_cls(nodes_by_type[self[0].name].values())


class QueryAPI(Generic[T_DomainModelList]):
    def __init__(
        self,
        client: CogniteClient,
        builder: QueryBuilder[T_DomainModelList],
        view_by_read_class: dict[type[DomainModelCore], dm.ViewId],
    ):
        self._client = client
        self._builder = builder
        self._view_by_read_class = view_by_read_class

    def _query(self) -> T_DomainModelList:
        self._builder.reset()
        query = self._builder.build()

        while True:
            self._builder.update_expression_limits()
            query.cursors = self._builder.cursors
            batch = self._client.data_modeling.instances.query(query)
            self._builder.update(batch)
            if self._builder.is_finished:
                break
        return self._builder.unpack()


def _create_edge_filter(
    edge_type: dm.DirectRelationReference,
    start_node: str | list[str] | dm.NodeId | list[dm.NodeId] | None = None,
    start_node_space: str = "IntegrationTestsImmutable",
    end_node: str | list[str] | dm.NodeId | list[dm.NodeId] | None = None,
    space_end_node: str = "IntegrationTestsImmutable",
    external_id_prefix: str | None = None,
    space: str | list[str] | None = None,
    filter: dm.Filter | None = None,
) -> dm.Filter:
    filters: list[dm.Filter] = [
        dm.filters.Equals(
            ["edge", "type"],
            {"space": edge_type.space, "externalId": edge_type.external_id},
        )
    ]
    if start_node and isinstance(start_node, str):
        filters.append(
            dm.filters.Equals(["edge", "startNode"], value={"space": start_node_space, "externalId": start_node})
        )
    elif start_node and isinstance(start_node, dm.NodeId):
        filters.append(
            dm.filters.Equals(
                ["edge", "startNode"], value=start_node.dump(camel_case=True, include_instance_type=False)
            )
        )
    if start_node and isinstance(start_node, list):
        filters.append(
            dm.filters.In(
                ["edge", "startNode"],
                values=[
                    (
                        {"space": start_node_space, "externalId": ext_id}
                        if isinstance(ext_id, str)
                        else ext_id.dump(camel_case=True, include_instance_type=False)
                    )
                    for ext_id in start_node
                ],
            )
        )
    if end_node and isinstance(end_node, str):
        filters.append(dm.filters.Equals(["edge", "endNode"], value={"space": space_end_node, "externalId": end_node}))
    elif end_node and isinstance(end_node, dm.NodeId):
        filters.append(
            dm.filters.Equals(["edge", "endNode"], value=end_node.dump(camel_case=True, include_instance_type=False))
        )
    if end_node and isinstance(end_node, list):
        filters.append(
            dm.filters.In(
                ["edge", "endNode"],
                values=[
                    (
                        {"space": space_end_node, "externalId": ext_id}
                        if isinstance(ext_id, str)
                        else ext_id.dump(camel_case=True, include_instance_type=False)
                    )
                    for ext_id in end_node
                ],
            )
        )
    if external_id_prefix:
        filters.append(dm.filters.Prefix(["edge", "externalId"], value=external_id_prefix))
    if space and isinstance(space, str):
        filters.append(dm.filters.Equals(["edge", "space"], value=space))
    if space and isinstance(space, list):
        filters.append(dm.filters.In(["edge", "space"], values=space))
    if filter:
        filters.append(filter)
    return dm.filters.And(*filters)


class GraphQLQueryResponse:
    def __init__(self, data_model_id: dm.DataModelId):
        self._output = GraphQLList([])
        self._data_class_by_type = _GRAPHQL_DATA_CLASS_BY_DATA_MODEL_BY_TYPE[data_model_id]

    def parse(self, response: dict[str, Any]) -> GraphQLList:
        if "errors" in response:
            raise RuntimeError(response["errors"])
        _, data = list(response.items())[0]
        self._parse_item(data)
        if "pageInfo" in data:
            self._output.page_info = PageInfo.load(data["pageInfo"])
        return self._output

    def _parse_item(self, data: dict[str, Any]) -> None:
        if "items" in data:
            for item in data["items"]:
                self._parse_item(item)
        elif "__typename" in data:
            try:
                item = self._data_class_by_type[data["__typename"]].model_validate(data)
            except KeyError:
                raise ValueError(f"Could not find class for type {data['__typename']}")
            else:
                self._output.append(item)
        else:
            raise RuntimeError("Missing '__typename' in GraphQL response. Cannot determine the type of the response.")


_GRAPHQL_DATA_CLASS_BY_DATA_MODEL_BY_TYPE = {
    dm.DataModelId("power-ops-assets", "PowerAsset", "1"): {
        "PriceArea": data_classes.PriceAreaGraphQL,
        "Watercourse": data_classes.WatercourseGraphQL,
        "Plant": data_classes.PlantGraphQL,
        "Generator": data_classes.GeneratorGraphQL,
        "Reservoir": data_classes.ReservoirGraphQL,
        "TurbineEfficiencyCurve": data_classes.TurbineEfficiencyCurveGraphQL,
        "GeneratorEfficiencyCurve": data_classes.GeneratorEfficiencyCurveGraphQL,
        "BidMethod": data_classes.BidMethodGraphQL,
    },
}
