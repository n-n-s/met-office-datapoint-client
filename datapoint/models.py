import datetime as dt
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class BaseModelExtension(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )


class Site(BaseModelExtension):
    id: str
    latitude: float
    longitude: float
    obs_location_type: str
    obs_region: str
    obs_source: str
    name: str


class ObsParamValue(BaseModel):
    title: str = Field(alias="$")
    name: str
    units: str


class ObsParams(BaseModel):
    Param: list[ObsParamValue]


class DvRep(BaseModel):
    minutes_after_midnight: int = Field(alias="$")
    wind_direction: Optional[str] = Field(alias="D", default=None)
    dew_point: Optional[float] = Field(alias="Dp", default=None)
    screen_relative_humidity: Optional[float] = Field(alias="H", default=None)
    pressure: Optional[float] = Field(alias="P", default=None)
    wind_speed: Optional[float] = Field(alias="S", default=None)
    temperature: Optional[float] = Field(alias="T", default=None)
    visibility: Optional[float] = Field(alias="V", default=None)
    wave_height: Optional[float] = Field(alias="Wh", default=None)
    wave_period: Optional[float] = Field(alias="Wp", default=None)


class DvPeriod(BaseModel):
    type: str
    value: str
    rep: list[DvRep] = Field(alias="Rep")


class DvLocation(BaseModel):
    id: str = Field(alias="i")
    latitude: float = Field(alias="lat")
    longitude: float = Field(alias="lon")
    name: str
    period: list[DvPeriod] = Field(alias="Period")


class DvValue(BaseModel):
    data_date: dt.datetime = Field(alias="dataDate")
    type: str
    location: Optional[DvLocation] = Field(alias="Location", default=None)


class SiteRep(BaseModel):
    Wx: ObsParams
    DV: DvValue
