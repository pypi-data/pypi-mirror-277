from __future__ import annotations

import warnings
from typing import TYPE_CHECKING, Any, Literal, Optional, Union

from cognite.client import data_modeling as dm
from pydantic import Field
from pydantic import field_validator, model_validator

from ._core import (
    DEFAULT_INSTANCE_SPACE,
    DataRecord,
    DataRecordGraphQL,
    DataRecordWrite,
    DomainModel,
    DomainModelCore,
    DomainModelWrite,
    DomainModelWriteList,
    DomainModelList,
    DomainRelationWrite,
    GraphQLCore,
    ResourcesWrite,
)
from ._function_output import FunctionOutput, FunctionOutputWrite

if TYPE_CHECKING:
    from ._alert import Alert, AlertGraphQL, AlertWrite
    from ._shop_result import ShopResult, ShopResultGraphQL, ShopResultWrite
    from ._shop_trigger_input import ShopTriggerInput, ShopTriggerInputGraphQL, ShopTriggerInputWrite


__all__ = [
    "ShopTriggerOutput",
    "ShopTriggerOutputWrite",
    "ShopTriggerOutputApply",
    "ShopTriggerOutputList",
    "ShopTriggerOutputWriteList",
    "ShopTriggerOutputApplyList",
    "ShopTriggerOutputFields",
    "ShopTriggerOutputTextFields",
]


ShopTriggerOutputTextFields = Literal["workflow_execution_id", "function_name", "function_call_id"]
ShopTriggerOutputFields = Literal["workflow_execution_id", "workflow_step", "function_name", "function_call_id"]

_SHOPTRIGGEROUTPUT_PROPERTIES_BY_FIELD = {
    "workflow_execution_id": "workflowExecutionId",
    "workflow_step": "workflowStep",
    "function_name": "functionName",
    "function_call_id": "functionCallId",
}


class ShopTriggerOutputGraphQL(GraphQLCore):
    """This represents the reading version of shop trigger output, used
    when data is retrieved from CDF using GraphQL.

    It is used when retrieving data from CDF using GraphQL.

    Args:
        space: The space where the node is located.
        external_id: The external id of the shop trigger output.
        data_record: The data record of the shop trigger output node.
        workflow_execution_id: The process associated with the function execution
        workflow_step: This is the step in the process.
        function_name: The name of the function
        function_call_id: The function call id
        input_: The input field.
        alerts: An array of calculation level Alerts.
        shop_result: The shop result field.
    """

    view_id = dm.ViewId("sp_power_ops_models", "ShopTriggerOutput", "1")
    workflow_execution_id: Optional[str] = Field(None, alias="workflowExecutionId")
    workflow_step: Optional[int] = Field(None, alias="workflowStep")
    function_name: Optional[str] = Field(None, alias="functionName")
    function_call_id: Optional[str] = Field(None, alias="functionCallId")
    input_: Optional[ShopTriggerInputGraphQL] = Field(None, repr=False, alias="input")
    alerts: Optional[list[AlertGraphQL]] = Field(default=None, repr=False)
    shop_result: Optional[ShopResultGraphQL] = Field(None, repr=False, alias="shopResult")

    @model_validator(mode="before")
    def parse_data_record(cls, values: Any) -> Any:
        if not isinstance(values, dict):
            return values
        if "lastUpdatedTime" in values or "createdTime" in values:
            values["dataRecord"] = DataRecordGraphQL(
                created_time=values.pop("createdTime", None),
                last_updated_time=values.pop("lastUpdatedTime", None),
            )
        return values

    @field_validator("input_", "alerts", "shop_result", mode="before")
    def parse_graphql(cls, value: Any) -> Any:
        if not isinstance(value, dict):
            return value
        if "items" in value:
            return value["items"]
        return value

    def as_read(self) -> ShopTriggerOutput:
        """Convert this GraphQL format of shop trigger output to the reading format."""
        if self.data_record is None:
            raise ValueError("This object cannot be converted to a read format because it lacks a data record.")
        return ShopTriggerOutput(
            space=self.space or DEFAULT_INSTANCE_SPACE,
            external_id=self.external_id,
            data_record=DataRecord(
                version=0,
                last_updated_time=self.data_record.last_updated_time,
                created_time=self.data_record.created_time,
            ),
            workflow_execution_id=self.workflow_execution_id,
            workflow_step=self.workflow_step,
            function_name=self.function_name,
            function_call_id=self.function_call_id,
            input_=self.input_.as_read() if isinstance(self.input_, GraphQLCore) else self.input_,
            alerts=[alert.as_read() if isinstance(alert, GraphQLCore) else alert for alert in self.alerts or []],
            shop_result=self.shop_result.as_read() if isinstance(self.shop_result, GraphQLCore) else self.shop_result,
        )

    def as_write(self) -> ShopTriggerOutputWrite:
        """Convert this GraphQL format of shop trigger output to the writing format."""
        return ShopTriggerOutputWrite(
            space=self.space or DEFAULT_INSTANCE_SPACE,
            external_id=self.external_id,
            data_record=DataRecordWrite(existing_version=0),
            workflow_execution_id=self.workflow_execution_id,
            workflow_step=self.workflow_step,
            function_name=self.function_name,
            function_call_id=self.function_call_id,
            input_=self.input_.as_write() if isinstance(self.input_, DomainModel) else self.input_,
            alerts=[alert.as_write() if isinstance(alert, DomainModel) else alert for alert in self.alerts or []],
            shop_result=self.shop_result.as_write() if isinstance(self.shop_result, DomainModel) else self.shop_result,
        )


class ShopTriggerOutput(FunctionOutput):
    """This represents the reading version of shop trigger output.

    It is used to when data is retrieved from CDF.

    Args:
        space: The space where the node is located.
        external_id: The external id of the shop trigger output.
        data_record: The data record of the shop trigger output node.
        workflow_execution_id: The process associated with the function execution
        workflow_step: This is the step in the process.
        function_name: The name of the function
        function_call_id: The function call id
        input_: The input field.
        alerts: An array of calculation level Alerts.
        shop_result: The shop result field.
    """

    node_type: Union[dm.DirectRelationReference, None] = dm.DirectRelationReference(
        "sp_power_ops_types", "ShopTriggerOutput"
    )
    shop_result: Union[ShopResult, str, dm.NodeId, None] = Field(None, repr=False, alias="shopResult")

    def as_write(self) -> ShopTriggerOutputWrite:
        """Convert this read version of shop trigger output to the writing version."""
        return ShopTriggerOutputWrite(
            space=self.space,
            external_id=self.external_id,
            data_record=DataRecordWrite(existing_version=self.data_record.version),
            workflow_execution_id=self.workflow_execution_id,
            workflow_step=self.workflow_step,
            function_name=self.function_name,
            function_call_id=self.function_call_id,
            input_=self.input_.as_write() if isinstance(self.input_, DomainModel) else self.input_,
            alerts=[alert.as_write() if isinstance(alert, DomainModel) else alert for alert in self.alerts or []],
            shop_result=self.shop_result.as_write() if isinstance(self.shop_result, DomainModel) else self.shop_result,
        )

    def as_apply(self) -> ShopTriggerOutputWrite:
        """Convert this read version of shop trigger output to the writing version."""
        warnings.warn(
            "as_apply is deprecated and will be removed in v1.0. Use as_write instead.",
            UserWarning,
            stacklevel=2,
        )
        return self.as_write()


class ShopTriggerOutputWrite(FunctionOutputWrite):
    """This represents the writing version of shop trigger output.

    It is used to when data is sent to CDF.

    Args:
        space: The space where the node is located.
        external_id: The external id of the shop trigger output.
        data_record: The data record of the shop trigger output node.
        workflow_execution_id: The process associated with the function execution
        workflow_step: This is the step in the process.
        function_name: The name of the function
        function_call_id: The function call id
        input_: The input field.
        alerts: An array of calculation level Alerts.
        shop_result: The shop result field.
    """

    node_type: Union[dm.DirectRelationReference, None] = dm.DirectRelationReference(
        "sp_power_ops_types", "ShopTriggerOutput"
    )
    shop_result: Union[ShopResultWrite, str, dm.NodeId, None] = Field(None, repr=False, alias="shopResult")

    def _to_instances_write(
        self,
        cache: set[tuple[str, str]],
        view_by_read_class: dict[type[DomainModelCore], dm.ViewId] | None,
        write_none: bool = False,
        allow_version_increase: bool = False,
    ) -> ResourcesWrite:
        resources = ResourcesWrite()
        if self.as_tuple_id() in cache:
            return resources

        write_view = (view_by_read_class or {}).get(
            ShopTriggerOutput, dm.ViewId("sp_power_ops_models", "ShopTriggerOutput", "1")
        )

        properties: dict[str, Any] = {}

        if self.workflow_execution_id is not None:
            properties["workflowExecutionId"] = self.workflow_execution_id

        if self.workflow_step is not None:
            properties["workflowStep"] = self.workflow_step

        if self.function_name is not None:
            properties["functionName"] = self.function_name

        if self.function_call_id is not None:
            properties["functionCallId"] = self.function_call_id

        if self.input_ is not None:
            properties["input"] = {
                "space": self.space if isinstance(self.input_, str) else self.input_.space,
                "externalId": self.input_ if isinstance(self.input_, str) else self.input_.external_id,
            }

        if self.shop_result is not None:
            properties["shopResult"] = {
                "space": self.space if isinstance(self.shop_result, str) else self.shop_result.space,
                "externalId": self.shop_result if isinstance(self.shop_result, str) else self.shop_result.external_id,
            }

        if properties:
            this_node = dm.NodeApply(
                space=self.space,
                external_id=self.external_id,
                existing_version=None if allow_version_increase else self.data_record.existing_version,
                type=self.node_type,
                sources=[
                    dm.NodeOrEdgeData(
                        source=write_view,
                        properties=properties,
                    )
                ],
            )
            resources.nodes.append(this_node)
            cache.add(self.as_tuple_id())

        edge_type = dm.DirectRelationReference("sp_power_ops_types", "calculationIssue")
        for alert in self.alerts or []:
            other_resources = DomainRelationWrite.from_edge_to_resources(
                cache,
                start_node=self,
                end_node=alert,
                edge_type=edge_type,
                view_by_read_class=view_by_read_class,
                write_none=write_none,
                allow_version_increase=allow_version_increase,
            )
            resources.extend(other_resources)

        if isinstance(self.input_, DomainModelWrite):
            other_resources = self.input_._to_instances_write(cache, view_by_read_class)
            resources.extend(other_resources)

        if isinstance(self.shop_result, DomainModelWrite):
            other_resources = self.shop_result._to_instances_write(cache, view_by_read_class)
            resources.extend(other_resources)

        return resources


class ShopTriggerOutputApply(ShopTriggerOutputWrite):
    def __new__(cls, *args, **kwargs) -> ShopTriggerOutputApply:
        warnings.warn(
            "ShopTriggerOutputApply is deprecated and will be removed in v1.0. Use ShopTriggerOutputWrite instead."
            "The motivation for this change is that Write is a more descriptive name for the writing version of the"
            "ShopTriggerOutput.",
            UserWarning,
            stacklevel=2,
        )
        return super().__new__(cls)


class ShopTriggerOutputList(DomainModelList[ShopTriggerOutput]):
    """List of shop trigger outputs in the read version."""

    _INSTANCE = ShopTriggerOutput

    def as_write(self) -> ShopTriggerOutputWriteList:
        """Convert these read versions of shop trigger output to the writing versions."""
        return ShopTriggerOutputWriteList([node.as_write() for node in self.data])

    def as_apply(self) -> ShopTriggerOutputWriteList:
        """Convert these read versions of primitive nullable to the writing versions."""
        warnings.warn(
            "as_apply is deprecated and will be removed in v1.0. Use as_write instead.",
            UserWarning,
            stacklevel=2,
        )
        return self.as_write()


class ShopTriggerOutputWriteList(DomainModelWriteList[ShopTriggerOutputWrite]):
    """List of shop trigger outputs in the writing version."""

    _INSTANCE = ShopTriggerOutputWrite


class ShopTriggerOutputApplyList(ShopTriggerOutputWriteList): ...


def _create_shop_trigger_output_filter(
    view_id: dm.ViewId,
    workflow_execution_id: str | list[str] | None = None,
    workflow_execution_id_prefix: str | None = None,
    min_workflow_step: int | None = None,
    max_workflow_step: int | None = None,
    function_name: str | list[str] | None = None,
    function_name_prefix: str | None = None,
    function_call_id: str | list[str] | None = None,
    function_call_id_prefix: str | None = None,
    input_: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
    shop_result: str | tuple[str, str] | list[str] | list[tuple[str, str]] | None = None,
    external_id_prefix: str | None = None,
    space: str | list[str] | None = None,
    filter: dm.Filter | None = None,
) -> dm.Filter | None:
    filters = []
    if isinstance(workflow_execution_id, str):
        filters.append(dm.filters.Equals(view_id.as_property_ref("workflowExecutionId"), value=workflow_execution_id))
    if workflow_execution_id and isinstance(workflow_execution_id, list):
        filters.append(dm.filters.In(view_id.as_property_ref("workflowExecutionId"), values=workflow_execution_id))
    if workflow_execution_id_prefix is not None:
        filters.append(
            dm.filters.Prefix(view_id.as_property_ref("workflowExecutionId"), value=workflow_execution_id_prefix)
        )
    if min_workflow_step is not None or max_workflow_step is not None:
        filters.append(
            dm.filters.Range(view_id.as_property_ref("workflowStep"), gte=min_workflow_step, lte=max_workflow_step)
        )
    if isinstance(function_name, str):
        filters.append(dm.filters.Equals(view_id.as_property_ref("functionName"), value=function_name))
    if function_name and isinstance(function_name, list):
        filters.append(dm.filters.In(view_id.as_property_ref("functionName"), values=function_name))
    if function_name_prefix is not None:
        filters.append(dm.filters.Prefix(view_id.as_property_ref("functionName"), value=function_name_prefix))
    if isinstance(function_call_id, str):
        filters.append(dm.filters.Equals(view_id.as_property_ref("functionCallId"), value=function_call_id))
    if function_call_id and isinstance(function_call_id, list):
        filters.append(dm.filters.In(view_id.as_property_ref("functionCallId"), values=function_call_id))
    if function_call_id_prefix is not None:
        filters.append(dm.filters.Prefix(view_id.as_property_ref("functionCallId"), value=function_call_id_prefix))
    if input_ and isinstance(input_, str):
        filters.append(
            dm.filters.Equals(
                view_id.as_property_ref("input"), value={"space": DEFAULT_INSTANCE_SPACE, "externalId": input_}
            )
        )
    if input_ and isinstance(input_, tuple):
        filters.append(
            dm.filters.Equals(view_id.as_property_ref("input"), value={"space": input_[0], "externalId": input_[1]})
        )
    if input_ and isinstance(input_, list) and isinstance(input_[0], str):
        filters.append(
            dm.filters.In(
                view_id.as_property_ref("input"),
                values=[{"space": DEFAULT_INSTANCE_SPACE, "externalId": item} for item in input_],
            )
        )
    if input_ and isinstance(input_, list) and isinstance(input_[0], tuple):
        filters.append(
            dm.filters.In(
                view_id.as_property_ref("input"), values=[{"space": item[0], "externalId": item[1]} for item in input_]
            )
        )
    if shop_result and isinstance(shop_result, str):
        filters.append(
            dm.filters.Equals(
                view_id.as_property_ref("shopResult"),
                value={"space": DEFAULT_INSTANCE_SPACE, "externalId": shop_result},
            )
        )
    if shop_result and isinstance(shop_result, tuple):
        filters.append(
            dm.filters.Equals(
                view_id.as_property_ref("shopResult"), value={"space": shop_result[0], "externalId": shop_result[1]}
            )
        )
    if shop_result and isinstance(shop_result, list) and isinstance(shop_result[0], str):
        filters.append(
            dm.filters.In(
                view_id.as_property_ref("shopResult"),
                values=[{"space": DEFAULT_INSTANCE_SPACE, "externalId": item} for item in shop_result],
            )
        )
    if shop_result and isinstance(shop_result, list) and isinstance(shop_result[0], tuple):
        filters.append(
            dm.filters.In(
                view_id.as_property_ref("shopResult"),
                values=[{"space": item[0], "externalId": item[1]} for item in shop_result],
            )
        )
    if external_id_prefix is not None:
        filters.append(dm.filters.Prefix(["node", "externalId"], value=external_id_prefix))
    if isinstance(space, str):
        filters.append(dm.filters.Equals(["node", "space"], value=space))
    if space and isinstance(space, list):
        filters.append(dm.filters.In(["node", "space"], values=space))
    if filter:
        filters.append(filter)
    return dm.filters.And(*filters) if filters else None
