# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .map_value import MapValue
from .observation_level import ObservationLevel

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Observation(pydantic.BaseModel):
    id: str
    trace_id: typing.Optional[str] = pydantic.Field(alias="traceId")
    type: str
    name: typing.Optional[str]
    start_time: dt.datetime = pydantic.Field(alias="startTime")
    end_time: typing.Optional[dt.datetime] = pydantic.Field(alias="endTime")
    completion_start_time: typing.Optional[dt.datetime] = pydantic.Field(alias="completionStartTime")
    model: typing.Optional[str]
    model_parameters: typing.Optional[typing.Dict[str, MapValue]] = pydantic.Field(alias="modelParameters")
    input: typing.Optional[typing.Any]
    version: typing.Optional[str]
    metadata: typing.Optional[typing.Any]
    output: typing.Optional[typing.Any]
    prompt_tokens: int = pydantic.Field(alias="promptTokens")
    completion_tokens: int = pydantic.Field(alias="completionTokens")
    total_tokens: int = pydantic.Field(alias="totalTokens")
    level: ObservationLevel
    status_message: typing.Optional[str] = pydantic.Field(alias="statusMessage")
    parent_observation_id: typing.Optional[str] = pydantic.Field(alias="parentObservationId")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
