from __future__ import annotations

from collections.abc import Sequence
from typing import overload
import warnings

from cognite.client import CogniteClient
from cognite.client import data_modeling as dm
from cognite.client.data_classes.data_modeling.instances import InstanceAggregationResultList

from cognite.powerops.client._generated.v1.data_classes._core import DEFAULT_INSTANCE_SPACE
from cognite.powerops.client._generated.v1.data_classes import (
    DomainModelCore,
    DomainModelWrite,
    ResourcesWriteResult,
    BidConfigurationDayAhead,
    BidConfigurationDayAheadWrite,
    BidConfigurationDayAheadFields,
    BidConfigurationDayAheadList,
    BidConfigurationDayAheadWriteList,
    BidConfigurationDayAheadTextFields,
)
from cognite.powerops.client._generated.v1.data_classes._bid_configuration_day_ahead import (
    _BIDCONFIGURATIONDAYAHEAD_PROPERTIES_BY_FIELD,
    _create_bid_configuration_day_ahead_filter,
)
from ._core import (
    DEFAULT_LIMIT_READ,
    DEFAULT_QUERY_LIMIT,
    Aggregations,
    NodeAPI,
    SequenceNotStr,
    QueryStep,
    QueryBuilder,
)
from .bid_configuration_day_ahead_partials import BidConfigurationDayAheadPartialsAPI
from .bid_configuration_day_ahead_query import BidConfigurationDayAheadQueryAPI


class BidConfigurationDayAheadAPI(
    NodeAPI[BidConfigurationDayAhead, BidConfigurationDayAheadWrite, BidConfigurationDayAheadList]
):
    def __init__(self, client: CogniteClient, view_by_read_class: dict[type[DomainModelCore], dm.ViewId]):
        view_id = view_by_read_class[BidConfigurationDayAhead]
        super().__init__(
            client=client,
            sources=view_id,
            class_type=BidConfigurationDayAhead,
            class_list=BidConfigurationDayAheadList,
            class_write_list=BidConfigurationDayAheadWriteList,
            view_by_read_class=view_by_read_class,
        )
        self._view_id = view_id
        self.partials_edge = BidConfigurationDayAheadPartialsAPI(client)

    def __call__(
        self,
        name: str | list[str] | None = None,
        name_prefix: str | None = None,
        market_configuration: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        price_area: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        bid_date_specification: str | list[str] | None = None,
        bid_date_specification_prefix: str | None = None,
        external_id_prefix: str | None = None,
        space: str | list[str] | None = None,
        limit: int | None = DEFAULT_QUERY_LIMIT,
        filter: dm.Filter | None = None,
    ) -> BidConfigurationDayAheadQueryAPI[BidConfigurationDayAheadList]:
        """Query starting at bid configuration day aheads.

        Args:
            name: The name to filter on.
            name_prefix: The prefix of the name to filter on.
            market_configuration: The market configuration to filter on.
            price_area: The price area to filter on.
            bid_date_specification: The bid date specification to filter on.
            bid_date_specification_prefix: The prefix of the bid date specification to filter on.
            external_id_prefix: The prefix of the external ID to filter on.
            space: The space to filter on.
            limit: Maximum number of bid configuration day aheads to return. Defaults to 25. Set to -1, float("inf") or None to return all items.
            filter: (Advanced) If the filtering available in the above is not sufficient, you can write your own filtering which will be ANDed with the filter above.

        Returns:
            A query API for bid configuration day aheads.

        """
        has_data = dm.filters.HasData(views=[self._view_id])
        filter_ = _create_bid_configuration_day_ahead_filter(
            self._view_id,
            name,
            name_prefix,
            market_configuration,
            price_area,
            bid_date_specification,
            bid_date_specification_prefix,
            external_id_prefix,
            space,
            (filter and dm.filters.And(filter, has_data)) or has_data,
        )
        builder = QueryBuilder(BidConfigurationDayAheadList)
        return BidConfigurationDayAheadQueryAPI(self._client, builder, self._view_by_read_class, filter_, limit)

    def apply(
        self,
        bid_configuration_day_ahead: BidConfigurationDayAheadWrite | Sequence[BidConfigurationDayAheadWrite],
        replace: bool = False,
        write_none: bool = False,
    ) -> ResourcesWriteResult:
        """Add or update (upsert) bid configuration day aheads.

        Note: This method iterates through all nodes and timeseries linked to bid_configuration_day_ahead and creates them including the edges
        between the nodes. For example, if any of `partials` are set, then these
        nodes as well as any nodes linked to them, and all the edges linking these nodes will be created.

        Args:
            bid_configuration_day_ahead: Bid configuration day ahead or sequence of bid configuration day aheads to upsert.
            replace (bool): How do we behave when a property value exists? Do we replace all matching and existing values with the supplied values (true)?
                Or should we merge in new values for properties together with the existing values (false)? Note: This setting applies for all nodes or edges specified in the ingestion call.
            write_none (bool): This method, will by default, skip properties that are set to None. However, if you want to set properties to None,
                you can set this parameter to True. Note this only applies to properties that are nullable.
        Returns:
            Created instance(s), i.e., nodes, edges, and time series.

        Examples:

            Create a new bid_configuration_day_ahead:

                >>> from cognite.powerops.client._generated.v1 import PowerOpsModelsV1Client
                >>> from cognite.powerops.client._generated.v1.data_classes import BidConfigurationDayAheadWrite
                >>> client = PowerOpsModelsV1Client()
                >>> bid_configuration_day_ahead = BidConfigurationDayAheadWrite(external_id="my_bid_configuration_day_ahead", ...)
                >>> result = client.bid_configuration_day_ahead.apply(bid_configuration_day_ahead)

        """
        warnings.warn(
            "The .apply method is deprecated and will be removed in v1.0. "
            "Please use the .upsert method on the client instead. This means instead of "
            "`my_client.bid_configuration_day_ahead.apply(my_items)` please use `my_client.upsert(my_items)`."
            "The motivation is that all apply methods are the same, and having one apply method per API "
            " class encourages users to create items in small batches, which is inefficient."
            "In addition, .upsert method is more descriptive of what the method does.",
            UserWarning,
            stacklevel=2,
        )
        return self._apply(bid_configuration_day_ahead, replace, write_none)

    def delete(
        self, external_id: str | SequenceNotStr[str], space: str = DEFAULT_INSTANCE_SPACE
    ) -> dm.InstancesDeleteResult:
        """Delete one or more bid configuration day ahead.

        Args:
            external_id: External id of the bid configuration day ahead to delete.
            space: The space where all the bid configuration day ahead are located.

        Returns:
            The instance(s), i.e., nodes and edges which has been deleted. Empty list if nothing was deleted.

        Examples:

            Delete bid_configuration_day_ahead by id:

                >>> from cognite.powerops.client._generated.v1 import PowerOpsModelsV1Client
                >>> client = PowerOpsModelsV1Client()
                >>> client.bid_configuration_day_ahead.delete("my_bid_configuration_day_ahead")
        """
        warnings.warn(
            "The .delete method is deprecated and will be removed in v1.0. "
            "Please use the .delete method on the client instead. This means instead of "
            "`my_client.bid_configuration_day_ahead.delete(my_ids)` please use `my_client.delete(my_ids)`."
            "The motivation is that all delete methods are the same, and having one delete method per API "
            " class encourages users to delete items in small batches, which is inefficient.",
            UserWarning,
            stacklevel=2,
        )
        return self._delete(external_id, space)

    @overload
    def retrieve(self, external_id: str, space: str = DEFAULT_INSTANCE_SPACE) -> BidConfigurationDayAhead | None: ...

    @overload
    def retrieve(
        self, external_id: SequenceNotStr[str], space: str = DEFAULT_INSTANCE_SPACE
    ) -> BidConfigurationDayAheadList: ...

    def retrieve(
        self, external_id: str | SequenceNotStr[str], space: str = DEFAULT_INSTANCE_SPACE
    ) -> BidConfigurationDayAhead | BidConfigurationDayAheadList | None:
        """Retrieve one or more bid configuration day aheads by id(s).

        Args:
            external_id: External id or list of external ids of the bid configuration day aheads.
            space: The space where all the bid configuration day aheads are located.

        Returns:
            The requested bid configuration day aheads.

        Examples:

            Retrieve bid_configuration_day_ahead by id:

                >>> from cognite.powerops.client._generated.v1 import PowerOpsModelsV1Client
                >>> client = PowerOpsModelsV1Client()
                >>> bid_configuration_day_ahead = client.bid_configuration_day_ahead.retrieve("my_bid_configuration_day_ahead")

        """
        return self._retrieve(
            external_id,
            space,
            retrieve_edges=True,
            edge_api_name_type_direction_view_id_penta=[
                (
                    self.partials_edge,
                    "partials",
                    dm.DirectRelationReference("sp_power_ops_types", "BidConfiguration.partials"),
                    "outwards",
                    dm.ViewId("sp_power_ops_models", "PartialBidConfiguration", "1"),
                ),
            ],
        )

    def search(
        self,
        query: str,
        properties: BidConfigurationDayAheadTextFields | Sequence[BidConfigurationDayAheadTextFields] | None = None,
        name: str | list[str] | None = None,
        name_prefix: str | None = None,
        market_configuration: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        price_area: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        bid_date_specification: str | list[str] | None = None,
        bid_date_specification_prefix: str | None = None,
        external_id_prefix: str | None = None,
        space: str | list[str] | None = None,
        limit: int | None = DEFAULT_LIMIT_READ,
        filter: dm.Filter | None = None,
    ) -> BidConfigurationDayAheadList:
        """Search bid configuration day aheads

        Args:
            query: The search query,
            properties: The property to search, if nothing is passed all text fields will be searched.
            name: The name to filter on.
            name_prefix: The prefix of the name to filter on.
            market_configuration: The market configuration to filter on.
            price_area: The price area to filter on.
            bid_date_specification: The bid date specification to filter on.
            bid_date_specification_prefix: The prefix of the bid date specification to filter on.
            external_id_prefix: The prefix of the external ID to filter on.
            space: The space to filter on.
            limit: Maximum number of bid configuration day aheads to return. Defaults to 25. Set to -1, float("inf") or None to return all items.
            filter: (Advanced) If the filtering available in the above is not sufficient, you can write your own filtering which will be ANDed with the filter above.

        Returns:
            Search results bid configuration day aheads matching the query.

        Examples:

           Search for 'my_bid_configuration_day_ahead' in all text properties:

                >>> from cognite.powerops.client._generated.v1 import PowerOpsModelsV1Client
                >>> client = PowerOpsModelsV1Client()
                >>> bid_configuration_day_aheads = client.bid_configuration_day_ahead.search('my_bid_configuration_day_ahead')

        """
        filter_ = _create_bid_configuration_day_ahead_filter(
            self._view_id,
            name,
            name_prefix,
            market_configuration,
            price_area,
            bid_date_specification,
            bid_date_specification_prefix,
            external_id_prefix,
            space,
            filter,
        )
        return self._search(
            self._view_id, query, _BIDCONFIGURATIONDAYAHEAD_PROPERTIES_BY_FIELD, properties, filter_, limit
        )

    @overload
    def aggregate(
        self,
        aggregations: (
            Aggregations
            | dm.aggregations.MetricAggregation
            | Sequence[Aggregations]
            | Sequence[dm.aggregations.MetricAggregation]
        ),
        property: BidConfigurationDayAheadFields | Sequence[BidConfigurationDayAheadFields] | None = None,
        group_by: None = None,
        query: str | None = None,
        search_properties: (
            BidConfigurationDayAheadTextFields | Sequence[BidConfigurationDayAheadTextFields] | None
        ) = None,
        name: str | list[str] | None = None,
        name_prefix: str | None = None,
        market_configuration: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        price_area: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        bid_date_specification: str | list[str] | None = None,
        bid_date_specification_prefix: str | None = None,
        external_id_prefix: str | None = None,
        space: str | list[str] | None = None,
        limit: int | None = DEFAULT_LIMIT_READ,
        filter: dm.Filter | None = None,
    ) -> list[dm.aggregations.AggregatedNumberedValue]: ...

    @overload
    def aggregate(
        self,
        aggregations: (
            Aggregations
            | dm.aggregations.MetricAggregation
            | Sequence[Aggregations]
            | Sequence[dm.aggregations.MetricAggregation]
        ),
        property: BidConfigurationDayAheadFields | Sequence[BidConfigurationDayAheadFields] | None = None,
        group_by: BidConfigurationDayAheadFields | Sequence[BidConfigurationDayAheadFields] = None,
        query: str | None = None,
        search_properties: (
            BidConfigurationDayAheadTextFields | Sequence[BidConfigurationDayAheadTextFields] | None
        ) = None,
        name: str | list[str] | None = None,
        name_prefix: str | None = None,
        market_configuration: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        price_area: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        bid_date_specification: str | list[str] | None = None,
        bid_date_specification_prefix: str | None = None,
        external_id_prefix: str | None = None,
        space: str | list[str] | None = None,
        limit: int | None = DEFAULT_LIMIT_READ,
        filter: dm.Filter | None = None,
    ) -> InstanceAggregationResultList: ...

    def aggregate(
        self,
        aggregate: (
            Aggregations
            | dm.aggregations.MetricAggregation
            | Sequence[Aggregations]
            | Sequence[dm.aggregations.MetricAggregation]
        ),
        property: BidConfigurationDayAheadFields | Sequence[BidConfigurationDayAheadFields] | None = None,
        group_by: BidConfigurationDayAheadFields | Sequence[BidConfigurationDayAheadFields] | None = None,
        query: str | None = None,
        search_property: (
            BidConfigurationDayAheadTextFields | Sequence[BidConfigurationDayAheadTextFields] | None
        ) = None,
        name: str | list[str] | None = None,
        name_prefix: str | None = None,
        market_configuration: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        price_area: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        bid_date_specification: str | list[str] | None = None,
        bid_date_specification_prefix: str | None = None,
        external_id_prefix: str | None = None,
        space: str | list[str] | None = None,
        limit: int | None = DEFAULT_LIMIT_READ,
        filter: dm.Filter | None = None,
    ) -> list[dm.aggregations.AggregatedNumberedValue] | InstanceAggregationResultList:
        """Aggregate data across bid configuration day aheads

        Args:
            aggregate: The aggregation to perform.
            property: The property to perform aggregation on.
            group_by: The property to group by when doing the aggregation.
            query: The query to search for in the text field.
            search_property: The text field to search in.
            name: The name to filter on.
            name_prefix: The prefix of the name to filter on.
            market_configuration: The market configuration to filter on.
            price_area: The price area to filter on.
            bid_date_specification: The bid date specification to filter on.
            bid_date_specification_prefix: The prefix of the bid date specification to filter on.
            external_id_prefix: The prefix of the external ID to filter on.
            space: The space to filter on.
            limit: Maximum number of bid configuration day aheads to return. Defaults to 25. Set to -1, float("inf") or None to return all items.
            filter: (Advanced) If the filtering available in the above is not sufficient, you can write your own filtering which will be ANDed with the filter above.

        Returns:
            Aggregation results.

        Examples:

            Count bid configuration day aheads in space `my_space`:

                >>> from cognite.powerops.client._generated.v1 import PowerOpsModelsV1Client
                >>> client = PowerOpsModelsV1Client()
                >>> result = client.bid_configuration_day_ahead.aggregate("count", space="my_space")

        """

        filter_ = _create_bid_configuration_day_ahead_filter(
            self._view_id,
            name,
            name_prefix,
            market_configuration,
            price_area,
            bid_date_specification,
            bid_date_specification_prefix,
            external_id_prefix,
            space,
            filter,
        )
        return self._aggregate(
            self._view_id,
            aggregate,
            _BIDCONFIGURATIONDAYAHEAD_PROPERTIES_BY_FIELD,
            property,
            group_by,
            query,
            search_property,
            limit,
            filter_,
        )

    def histogram(
        self,
        property: BidConfigurationDayAheadFields,
        interval: float,
        query: str | None = None,
        search_property: (
            BidConfigurationDayAheadTextFields | Sequence[BidConfigurationDayAheadTextFields] | None
        ) = None,
        name: str | list[str] | None = None,
        name_prefix: str | None = None,
        market_configuration: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        price_area: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        bid_date_specification: str | list[str] | None = None,
        bid_date_specification_prefix: str | None = None,
        external_id_prefix: str | None = None,
        space: str | list[str] | None = None,
        limit: int | None = DEFAULT_LIMIT_READ,
        filter: dm.Filter | None = None,
    ) -> dm.aggregations.HistogramValue:
        """Produces histograms for bid configuration day aheads

        Args:
            property: The property to use as the value in the histogram.
            interval: The interval to use for the histogram bins.
            query: The query to search for in the text field.
            search_property: The text field to search in.
            name: The name to filter on.
            name_prefix: The prefix of the name to filter on.
            market_configuration: The market configuration to filter on.
            price_area: The price area to filter on.
            bid_date_specification: The bid date specification to filter on.
            bid_date_specification_prefix: The prefix of the bid date specification to filter on.
            external_id_prefix: The prefix of the external ID to filter on.
            space: The space to filter on.
            limit: Maximum number of bid configuration day aheads to return. Defaults to 25. Set to -1, float("inf") or None to return all items.
            filter: (Advanced) If the filtering available in the above is not sufficient, you can write your own filtering which will be ANDed with the filter above.

        Returns:
            Bucketed histogram results.

        """
        filter_ = _create_bid_configuration_day_ahead_filter(
            self._view_id,
            name,
            name_prefix,
            market_configuration,
            price_area,
            bid_date_specification,
            bid_date_specification_prefix,
            external_id_prefix,
            space,
            filter,
        )
        return self._histogram(
            self._view_id,
            property,
            interval,
            _BIDCONFIGURATIONDAYAHEAD_PROPERTIES_BY_FIELD,
            query,
            search_property,
            limit,
            filter_,
        )

    def list(
        self,
        name: str | list[str] | None = None,
        name_prefix: str | None = None,
        market_configuration: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        price_area: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
        bid_date_specification: str | list[str] | None = None,
        bid_date_specification_prefix: str | None = None,
        external_id_prefix: str | None = None,
        space: str | list[str] | None = None,
        limit: int | None = DEFAULT_LIMIT_READ,
        filter: dm.Filter | None = None,
        retrieve_edges: bool = True,
    ) -> BidConfigurationDayAheadList:
        """List/filter bid configuration day aheads

        Args:
            name: The name to filter on.
            name_prefix: The prefix of the name to filter on.
            market_configuration: The market configuration to filter on.
            price_area: The price area to filter on.
            bid_date_specification: The bid date specification to filter on.
            bid_date_specification_prefix: The prefix of the bid date specification to filter on.
            external_id_prefix: The prefix of the external ID to filter on.
            space: The space to filter on.
            limit: Maximum number of bid configuration day aheads to return. Defaults to 25. Set to -1, float("inf") or None to return all items.
            filter: (Advanced) If the filtering available in the above is not sufficient, you can write your own filtering which will be ANDed with the filter above.
            retrieve_edges: Whether to retrieve `partials` external ids for the bid configuration day aheads. Defaults to True.

        Returns:
            List of requested bid configuration day aheads

        Examples:

            List bid configuration day aheads and limit to 5:

                >>> from cognite.powerops.client._generated.v1 import PowerOpsModelsV1Client
                >>> client = PowerOpsModelsV1Client()
                >>> bid_configuration_day_aheads = client.bid_configuration_day_ahead.list(limit=5)

        """
        filter_ = _create_bid_configuration_day_ahead_filter(
            self._view_id,
            name,
            name_prefix,
            market_configuration,
            price_area,
            bid_date_specification,
            bid_date_specification_prefix,
            external_id_prefix,
            space,
            filter,
        )

        return self._list(
            limit=limit,
            filter=filter_,
            retrieve_edges=retrieve_edges,
            edge_api_name_type_direction_view_id_penta=[
                (
                    self.partials_edge,
                    "partials",
                    dm.DirectRelationReference("sp_power_ops_types", "BidConfiguration.partials"),
                    "outwards",
                    dm.ViewId("sp_power_ops_models", "PartialBidConfiguration", "1"),
                ),
            ],
        )
