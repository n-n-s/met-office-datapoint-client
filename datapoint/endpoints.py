from enum import Enum

BASE_URL = "http://datapoint.metoffice.gov.uk/public/data/val"


class DataSource(str, Enum):
    MARINE = "wxmarineobs"


class Endpoints(str, Enum):
    SITE_LIST = "sitelist"
    CAPABILITIES = "capabilities"


class DataFrequency(str, Enum):
    HOURLY = "hourly"
