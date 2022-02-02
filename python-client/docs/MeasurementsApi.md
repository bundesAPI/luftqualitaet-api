# luftqualitaet.MeasurementsApi

All URIs are relative to *https://www.umweltbundesamt.de/api/air_data/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**measures_json_get**](MeasurementsApi.md#measures_json_get) | **GET** /measures/json | Get all measurements
[**measures_limits_get**](MeasurementsApi.md#measures_limits_get) | **GET** /measures/limits | Get measurement date limits


# **measures_json_get**
> [Measure] measures_json_get(date_from, time_from, date_to, time_to)

Get all measurements

This entry point returns measures for the provided parameters.

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import measurements_api
from deutschland.luftqualitaet.model.measure import Measure
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = measurements_api.MeasurementsApi(api_client)
    date_from = "2019-01-01" # str | A date
    time_from = 9 # int | An hour.
    date_to = "2019-01-01" # str | A date
    time_to = 9 # int | An hour.
    station = 769 # int | Id of station (optional)
    component = 1 # int | Id of component (optional)
    scope = 2 # int | Id of scope (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all measurements
        api_response = api_instance.measures_json_get(date_from, time_from, date_to, time_to)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MeasurementsApi->measures_json_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all measurements
        api_response = api_instance.measures_json_get(date_from, time_from, date_to, time_to, station=station, component=component, scope=scope)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MeasurementsApi->measures_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_from** | **str**| A date |
 **time_from** | **int**| An hour. |
 **date_to** | **str**| A date |
 **time_to** | **int**| An hour. |
 **station** | **int**| Id of station | [optional]
 **component** | **int**| Id of component | [optional]
 **scope** | **int**| Id of scope | [optional]

### Return type

[**[Measure]**](Measure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**422** | required parameter is missing. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measures_limits_get**
> InlineResponse2004 measures_limits_get()

Get measurement date limits

This entry point returns all limits of measurements

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import measurements_api
from deutschland.luftqualitaet.model.inline_response2004 import InlineResponse2004
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = measurements_api.MeasurementsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get measurement date limits
        api_response = api_instance.measures_limits_get()
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MeasurementsApi->measures_limits_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

