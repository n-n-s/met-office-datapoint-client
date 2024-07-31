import datetime as dt
import logging
from typing import Optional

import pandas as pd
from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from datapoint.utils import parse_timestamp

logger = logging.getLogger(__name__)


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

    def get_measurement_values(self) -> pd.DataFrame:
        _df_list = []
        for p in self.DV.location.period:
            _midnight_timestamp = parse_timestamp(v=p.value)
            for r in p.rep:
                _data = r.dict()
                _minutes_after_midnight = _data.pop("minutes_after_midnight")
                _timestamp = _midnight_timestamp + pd.Timedelta(minutes=_minutes_after_midnight)
                _df_list.append(pd.DataFrame(_data, index=[_timestamp]))
        df = pd.concat(_df_list)
        df.index.name = "dttimestamp"
        return df
