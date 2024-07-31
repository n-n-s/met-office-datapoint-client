import pandas as pd

from datapoint import utils


def test_parse_timestamp():
    actual = utils.parse_timestamp(v="2000-01-01Z")
    expected = pd.Timestamp("2000-01-01 00:00:00Z")
    assert actual == expected
