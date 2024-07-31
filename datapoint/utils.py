import pandas as pd


def parse_timestamp(v: str) -> pd.Timestamp:
    _day = v[0:10]
    _timezone = v[10:]
    return pd.Timestamp(_day + "T00:00:00" + _timezone)
