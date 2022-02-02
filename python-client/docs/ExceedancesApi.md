# luftqualitaet.ExceedancesApi

All URIs are relative to *https://www.umweltbundesamt.de/api/air_data/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transgressions_json_get**](ExceedancesApi.md#transgressions_json_get) | **GET** /transgressions/json | Get exceedances data


# **transgressions_json_get**
> bool, date, datetime, dict, float, int, list, str, none_type transgressions_json_get(component, year)

Get exceedances data

Returns exceedances data

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import exceedances_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = exceedances_api.ExceedancesApi(api_client)
    component = 1 # int | Id of component
    year = "2019" # str | A 4-digit Year
    lang = "de" # str | The language code (optional) if omitted the server will use the default value of "en"
    index = "code" # str | The type of index to be used (optional) if omitted the server will use the default value of "id"

    # example passing only required values which don't have defaults set
    try:
        # Get exceedances data
        api_response = api_instance.transgressions_json_get(component, year)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling ExceedancesApi->transgressions_json_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get exceedances data
        api_response = api_instance.transgressions_json_get(component, year, lang=lang, index=index)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling ExceedancesApi->transgressions_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component** | **int**| Id of component |
 **year** | **str**| A 4-digit Year |
 **lang** | **str**| The language code | [optional] if omitted the server will use the default value of "en"
 **index** | **str**| The type of index to be used | [optional] if omitted the server will use the default value of "id"

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

