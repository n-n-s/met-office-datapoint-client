from datapoint import models


def test_location():
    j = {
        "id": "162103",
        "latitude": "49.9167",
        "longitude": "-2.883",
        "name": "Channel",
        "obsLocationType": "Buoy",
        "obsRegion": "South Coast",
        "obsSource": "FM-13 SHIP",
    }
    actual = models.Site.model_validate(j)
    expected = models.Site(
        id="162103",
        latitude=49.9167,
        longitude=-2.883,
        name="Channel",
        obs_location_type="Buoy",
        obs_region="South Coast",
        obs_source="FM-13 SHIP",
    )
    assert actual == expected


class TestDvPeriod:
    any_string = "anything"
    any_int = 42
    any_float = 0.1

    def test_non_list_rep(self):
        actual = models.DvPeriod(
            type=self.any_string,
            value=self.any_string,
            Rep={
                "$": self.any_int,
                "D": self.any_string,
                "S": self.any_float,
                "Wh": self.any_float,
                "Wp": self.any_float,
            },
        )

        assert isinstance(actual.rep, list)
        assert isinstance(actual.rep[0], models.DvRep)
