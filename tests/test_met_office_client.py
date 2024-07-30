import logging

import responses

from datapoint import MetOfficeDataPointClient, models
from datapoint.endpoints import BASE_URL, DataFrequency, DataSource, Endpoints


@responses.activate
def test_get_site_list(monkeypatch, caplog):
    responses.add(
        responses.GET,
        url=f"{BASE_URL}/{DataSource.MARINE.value}/all/json/{Endpoints.SITE_LIST.value}?key=",
        json={
            "Locations": {
                "Location": [
                    {
                        "id": "162103",
                        "latitude": "49.9167",
                        "longitude": "-2.883",
                        "name": "Channel",
                        "obsLocationType": "Buoy",
                        "obsRegion": "South Coast",
                        "obsSource": "FM-13 SHIP",
                    }
                ]
            }
        },
    )

    caplog.set_level(logging.DEBUG)

    with MetOfficeDataPointClient(api_key="") as client:
        actual = client.get_site_list()
    expected = [
        models.Site(
            id="162103",
            latitude=49.9167,
            longitude=-2.883,
            name="Channel",
            obs_location_type="Buoy",
            obs_region="South Coast",
            obs_source="FM-13 SHIP",
        )
    ]

    assert actual == expected

    assert "Session created" in caplog.text
    assert "Session closed" in caplog.text


@responses.activate
def test_get_observations():
    fake_json = {
        "SiteRep": {
            "Wx": {
                "Param": [
                    {"name": "T", "units": "C", "$": "Temperature"},
                    {"name": "V", "units": "nmi", "$": "Visibility"},
                    {"name": "D", "units": "compass", "$": "Wind Direction"},
                    {"name": "W", "units": "", "$": "Weather Type"},
                    {"name": "P", "units": "hpa", "$": "Pressure"},
                    {"name": "Pt", "units": "Pa/s", "$": "Pressure Tendency"},
                    {"name": "Dp", "units": "C", "$": "Dew Point"},
                    {"name": "H", "units": "%", "$": "Screen Relative Humidity"},
                    {"name": "St", "units": "C", "$": "Sea Temperature"},
                    {"name": "S", "units": "kn", "$": "Wind Speed"},
                    {"name": "Wh", "units": "m", "$": "Wave Height"},
                    {"name": "Wp", "units": "s", "$": "Wave Period"},
                ]
            },
            "DV": {
                "dataDate": "2024-07-30T11:00:00Z",
                "type": "ShipSynops",
                "Location": {
                    "i": "162107",
                    "lat": "50.04",
                    "lon": "-6.04",
                    "name": "SEVEN STONES",
                    "Period": [
                        {
                            "type": "Day",
                            "value": "2024-07-29Z",
                            "Rep": [
                                {
                                    "D": "N",
                                    "H": "82.9",
                                    "P": "1020",
                                    "S": "3",
                                    "T": "17.2",
                                    "V": "26",
                                    "Dp": "14.3",
                                    "Wh": "0.6",
                                    "Wp": "8.0",
                                    "St": "17.6",
                                    "$": "660",
                                },
                                {
                                    "D": "N",
                                    "H": "82.4",
                                    "P": "1020",
                                    "S": "4",
                                    "T": "17.2",
                                    "V": "26",
                                    "Dp": "14.2",
                                    "Wh": "0.7",
                                    "Wp": "7.0",
                                    "St": "17.9",
                                    "$": "720",
                                },
                                {
                                    "D": "N",
                                    "H": "78.2",
                                    "P": "1019",
                                    "S": "5",
                                    "T": "17.6",
                                    "V": "26",
                                    "Dp": "13.8",
                                    "Wh": "0.5",
                                    "Wp": "8.0",
                                    "St": "18.2",
                                    "$": "780",
                                },
                                {
                                    "D": "N",
                                    "H": "82.0",
                                    "P": "1019",
                                    "S": "7",
                                    "T": "18.1",
                                    "V": "26",
                                    "Dp": "15.0",
                                    "Wh": "0.5",
                                    "Wp": "8.0",
                                    "St": "18.0",
                                    "$": "840",
                                },
                                {
                                    "D": "N",
                                    "H": "80.5",
                                    "P": "1019",
                                    "S": "5",
                                    "T": "19.0",
                                    "V": "10",
                                    "Dp": "15.6",
                                    "Wh": "0.5",
                                    "Wp": "7.0",
                                    "St": "17.4",
                                    "$": "900",
                                },
                                {
                                    "D": "N",
                                    "H": "81.0",
                                    "P": "1019",
                                    "S": "9",
                                    "T": "18.6",
                                    "V": "10",
                                    "Dp": "15.3",
                                    "Wh": "0.5",
                                    "Wp": "7.0",
                                    "St": "17.8",
                                    "$": "960",
                                },
                                {
                                    "D": "NNW",
                                    "H": "85.8",
                                    "P": "1019",
                                    "S": "6",
                                    "T": "18.1",
                                    "V": "5",
                                    "Dp": "15.7",
                                    "Wh": "0.5",
                                    "Wp": "7.0",
                                    "St": "18.0",
                                    "$": "1020",
                                },
                            ],
                        },
                        {
                            "type": "Day",
                            "value": "2024-07-30Z",
                            "Rep": [
                                {
                                    "H": "92.0",
                                    "P": "1017",
                                    "T": "17.0",
                                    "V": "10",
                                    "Dp": "15.7",
                                    "Wh": "0.2",
                                    "Wp": "6.0",
                                    "St": "16.4",
                                    "$": "540",
                                },
                                {
                                    "D": "NNE",
                                    "H": "92.0",
                                    "P": "1017",
                                    "S": "14",
                                    "T": "17.1",
                                    "V": "5",
                                    "Dp": "15.8",
                                    "Wh": "0.2",
                                    "Wp": "9.0",
                                    "St": "16.4",
                                    "$": "600",
                                },
                                {
                                    "D": "NE",
                                    "H": "92.7",
                                    "P": "1017",
                                    "S": "10",
                                    "T": "17.3",
                                    "V": "5",
                                    "Dp": "16.1",
                                    "Wh": "0.2",
                                    "Wp": "8.0",
                                    "St": "16.5",
                                    "$": "660",
                                },
                            ],
                        },
                    ],
                },
            },
        }
    }
    fake_site_id = "12345"
    responses.add(
        responses.GET,
        url=f"{BASE_URL}/{DataSource.MARINE.value}/all/json/{fake_site_id}?res={DataFrequency.HOURLY.value}&key=",
        json=fake_json,
    )

    with MetOfficeDataPointClient(api_key="") as client:
        actual = client.get_observations(site_id=fake_site_id)

    expected = models.SiteRep.model_validate(fake_json["SiteRep"])

    assert actual == expected
