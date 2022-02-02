# luftqualitaet.AnnualtabulationApi

All URIs are relative to *https://www.umweltbundesamt.de/api/air_data/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annualbalances_json_get**](AnnualtabulationApi.md#annualbalances_json_get) | **GET** /annualbalances/json | Get annualtabulation


# **annualbalances_json_get**
> InlineResponse2002 annualbalances_json_get(component, year)

Get annualtabulation

This entry point returns the data of annual tabulations

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import annualtabulation_api
from deutschland.luftqualitaet.model.inline_response2002 import InlineResponse2002
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annualtabulation_api.AnnualtabulationApi(api_client)
    component = 1 # int | Id of component
    year = "2019" # str | A 4-digit Year
    lang = "de" # str | The language code (optional) if omitted the server will use the default value of "en"

    # example passing only required values which don't have defaults set
    try:
        # Get annualtabulation
        api_response = api_instance.annualbalances_json_get(component, year)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling AnnualtabulationApi->annualbalances_json_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get annualtabulation
        api_response = api_instance.annualbalances_json_get(component, year, lang=lang)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling AnnualtabulationApi->annualbalances_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component** | **int**| Id of component |
 **year** | **str**| A 4-digit Year |
 **lang** | **str**| The language code | [optional] if omitted the server will use the default value of "en"

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

