# luftqualitaet.AirqualityApi

All URIs are relative to *https://www.umweltbundesamt.de/api/air_data/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**airquality_json_get**](AirqualityApi.md#airquality_json_get) | **GET** /airquality/json | Get airquality data
[**airquality_limits_get**](AirqualityApi.md#airquality_limits_get) | **GET** /airquality/limits | Get airquality date limits


# **airquality_json_get**
> InlineResponse200 airquality_json_get(date_from, time_from, date_to, time_to)

Get airquality data

This entry point returns airquality data for the provided parameters.

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import airquality_api
from deutschland.luftqualitaet.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = airquality_api.AirqualityApi(api_client)
    date_from = "2019-01-01" # str | A date
    time_from = 9 # int | An hour.
    date_to = "2019-01-01" # str | A date
    time_to = 9 # int | An hour.
    station = 769 # int | Id of station (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get airquality data
        api_response = api_instance.airquality_json_get(date_from, time_from, date_to, time_to)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling AirqualityApi->airquality_json_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get airquality data
        api_response = api_instance.airquality_json_get(date_from, time_from, date_to, time_to, station=station)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling AirqualityApi->airquality_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_from** | **str**| A date |
 **time_from** | **int**| An hour. |
 **date_to** | **str**| A date |
 **time_to** | **int**| An hour. |
 **station** | **int**| Id of station | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **airquality_limits_get**
> InlineResponse2001 airquality_limits_get()

Get airquality date limits

This entry point returns the date limits of airquality stations.

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import airquality_api
from deutschland.luftqualitaet.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = airquality_api.AirqualityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get airquality date limits
        api_response = api_instance.airquality_limits_get()
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling AirqualityApi->airquality_limits_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

