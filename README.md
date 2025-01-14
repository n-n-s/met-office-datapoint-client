# Met Office DataPoint client

[![Tests](https://github.com/n-n-s/met-office-datapoint-client/actions/workflows/merge.yaml/badge.svg)](https://github.com/n-n-s/met-office-datapoint-client/actions/workflows/merge.yaml)

A python client for the [Met Office DataPoint](https://www.metoffice.gov.uk/services/data/datapoint) service.
This library is not authored or affiliated with the Met Office, but was created to conveniently obtain data from the
Met Office DataPoint service using python.
You will need to obtain your own personal API Key, the process for which is described in the
[Met Office DataPoint getting started guide](https://www.metoffice.gov.uk/services/data/datapoint/getting-started).

## Example usage:

Set an environment variable named `MET_OFFICE_API_KEY` as the value of your API Key.

```python
import os

from datapoint import MetOfficeDataPointClient

with MetOfficeDataPointClient(os.environ["MET_OFFICE_API_KEY"]) as client:
    sites = client.get_site_list()
    site_id = "162107"
    obs = client.get_observations(site_id=site_id)

df = obs.get_measurement_values()
```
