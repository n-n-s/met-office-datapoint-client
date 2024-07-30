import logging

import requests

from datapoint import models
from datapoint.endpoints import BASE_URL, DataFrequency, DataSource, Endpoints

logger = logging.getLogger(__name__)


class MetOfficeDataPointClient:
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._client = None

    def __enter__(self):
        self._session = requests.Session()
        self._session.params.update({"key": self._api_key})
        logger.debug("Session created")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()
        logger.debug("Session closed")

    def get_site_list(self, data_source: DataSource = DataSource.MARINE.value) -> list[models.Site]:
        """

        .. code-block:: python

            from datapoint.met_office_client import MetOfficeDataPointClient

            with MetOfficeDataPointClient(api_key=os.environ["MET_OFFICE_API_KEY"]) as client:
                sites = client.get_site_list()
        """
        url = f"{BASE_URL}/{data_source}/all/json/{Endpoints.SITE_LIST.value}"
        resp = self._session.get(url=url)
        resp.raise_for_status()
        return [models.Site.model_validate(v) for v in resp.json()["Locations"]["Location"]]

    def get_observations(self, site_id: str, data_source: DataSource = DataSource.MARINE.value) -> models.SiteRep:
        """
        Get measurement values at the site

        .. code-block:: python

            from datapoint.met_office_client import MetOfficeDataPointClient

            with MetOfficeDataPointClient(api_key=os.environ["MET_OFFICE_API_KEY"]) as client:
                sites = client.get_site_list()
                site_id = sites[0].id  # for example take the first site in the list of sites
                obs = client.get_observations(site_id=site_id)
        """
        url = f"{BASE_URL}/{data_source}/all/json/{site_id}"
        resp = self._session.get(url=url, params={"res": DataFrequency.HOURLY.value})
        resp.raise_for_status()
        return models.SiteRep.model_validate(resp.json()["SiteRep"])
