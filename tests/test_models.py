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
