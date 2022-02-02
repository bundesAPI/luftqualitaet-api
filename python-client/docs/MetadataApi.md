# luftqualitaet.MetadataApi

All URIs are relative to *https://www.umweltbundesamt.de/api/air_data/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**components_json_get**](MetadataApi.md#components_json_get) | **GET** /components/json | Get all components
[**meta_json_get**](MetadataApi.md#meta_json_get) | **GET** /meta/json | Get combined metadata for use
[**networks_json_get**](MetadataApi.md#networks_json_get) | **GET** /networks/json | Get all networks
[**scopes_json_get**](MetadataApi.md#scopes_json_get) | **GET** /scopes/json | Get all scopes
[**stationsettings_json_get**](MetadataApi.md#stationsettings_json_get) | **GET** /stationsettings/json | Get all station settings
[**stationtypes_json_get**](MetadataApi.md#stationtypes_json_get) | **GET** /stationtypes/json | Get all station types
[**thresholds_json_get**](MetadataApi.md#thresholds_json_get) | **GET** /thresholds/json | Get all thresholds
[**transgressiontypes_json_get**](MetadataApi.md#transgressiontypes_json_get) | **GET** /transgressiontypes/json | Get all exceedances types


# **components_json_get**
> InlineResponse2003 components_json_get()

Get all components

This entry point returns a list of all components.

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import metadata_api
from deutschland.luftqualitaet.model.inline_response2003 import InlineResponse2003
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    lang = "de" # str | The language code (optional) if omitted the server will use the default value of "en"
    index = "code" # str | The type of index to be used (optional) if omitted the server will use the default value of "id"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all components
        api_response = api_instance.components_json_get(lang=lang, index=index)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MetadataApi->components_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language code | [optional] if omitted the server will use the default value of "en"
 **index** | **str**| The type of index to be used | [optional] if omitted the server will use the default value of "id"

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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

# **meta_json_get**
> InlineResponse2006 meta_json_get(use)

Get combined metadata for use

The use parameter defines what meta data should be returned. E.g. if you set use to airquality, meta data of airquality is returned.

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import metadata_api
from deutschland.luftqualitaet.model.inline_response2006 import InlineResponse2006
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    use = "airquality" # str | Defines the use.
    lang = "de" # str | The language code (optional) if omitted the server will use the default value of "en"
    date_from = "2019-01-01" # str | A date (required only for use = airquality) (optional)
    date_to = "2019-01-01" # str | A date (required only for use = airquality) (optional)
    time_from = 9 # int | An hour. (optional)
    time_to = 9 # int | An hour. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get combined metadata for use
        api_response = api_instance.meta_json_get(use)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MetadataApi->meta_json_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get combined metadata for use
        api_response = api_instance.meta_json_get(use, lang=lang, date_from=date_from, date_to=date_to, time_from=time_from, time_to=time_to)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MetadataApi->meta_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use** | **str**| Defines the use. |
 **lang** | **str**| The language code | [optional] if omitted the server will use the default value of "en"
 **date_from** | **str**| A date (required only for use &#x3D; airquality) | [optional]
 **date_to** | **str**| A date (required only for use &#x3D; airquality) | [optional]
 **time_from** | **int**| An hour. | [optional]
 **time_to** | **int**| An hour. | [optional]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

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

# **networks_json_get**
> [Network] networks_json_get()

Get all networks

This entry point returns a list of all networks.

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import metadata_api
from deutschland.luftqualitaet.model.network import Network
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    lang = "de" # str | The language code (optional) if omitted the server will use the default value of "en"
    index = "code" # str | The type of index to be used (optional) if omitted the server will use the default value of "id"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all networks
        api_response = api_instance.networks_json_get(lang=lang, index=index)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MetadataApi->networks_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language code | [optional] if omitted the server will use the default value of "en"
 **index** | **str**| The type of index to be used | [optional] if omitted the server will use the default value of "id"

### Return type

[**[Network]**](Network.md)

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

# **scopes_json_get**
> InlineResponse2005 scopes_json_get()

Get all scopes

The entry point returns a list of all scopes.

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import metadata_api
from deutschland.luftqualitaet.model.inline_response2005 import InlineResponse2005
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    lang = "de" # str | The language code (optional) if omitted the server will use the default value of "en"
    index = "code" # str | The type of index to be used (optional) if omitted the server will use the default value of "id"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all scopes
        api_response = api_instance.scopes_json_get(lang=lang, index=index)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MetadataApi->scopes_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language code | [optional] if omitted the server will use the default value of "en"
 **index** | **str**| The type of index to be used | [optional] if omitted the server will use the default value of "id"

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

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

# **stationsettings_json_get**
> [Stationsetting] stationsettings_json_get()

Get all station settings

This entry point returns a list of all station settings.

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import metadata_api
from deutschland.luftqualitaet.model.stationsetting import Stationsetting
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    lang = "de" # str | The language code (optional) if omitted the server will use the default value of "en"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all station settings
        api_response = api_instance.stationsettings_json_get(lang=lang)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MetadataApi->stationsettings_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language code | [optional] if omitted the server will use the default value of "en"

### Return type

[**[Stationsetting]**](Stationsetting.md)

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

# **stationtypes_json_get**
> [Stationtype] stationtypes_json_get()

Get all station types

This entry point returns a list of all station types.

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import metadata_api
from deutschland.luftqualitaet.model.stationtype import Stationtype
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    lang = "de" # str | The language code (optional) if omitted the server will use the default value of "en"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all station types
        api_response = api_instance.stationtypes_json_get(lang=lang)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MetadataApi->stationtypes_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language code | [optional] if omitted the server will use the default value of "en"

### Return type

[**[Stationtype]**](Stationtype.md)

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

# **thresholds_json_get**
> [Threshold] thresholds_json_get(use)

Get all thresholds

This entry point returns a list of all thresholds

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import metadata_api
from deutschland.luftqualitaet.model.threshold import Threshold
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    use = "airquality" # str | Defines which thresholds to use.
    lang = "de" # str | The language code (optional) if omitted the server will use the default value of "en"
    component = 1 # int | Id of component (optional)
    scope = 2 # int | Id of scope (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all thresholds
        api_response = api_instance.thresholds_json_get(use)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MetadataApi->thresholds_json_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all thresholds
        api_response = api_instance.thresholds_json_get(use, lang=lang, component=component, scope=scope)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MetadataApi->thresholds_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use** | **str**| Defines which thresholds to use. |
 **lang** | **str**| The language code | [optional] if omitted the server will use the default value of "en"
 **component** | **int**| Id of component | [optional]
 **scope** | **int**| Id of scope | [optional]

### Return type

[**[Threshold]**](Threshold.md)

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

# **transgressiontypes_json_get**
> [Transgressiontype] transgressiontypes_json_get()

Get all exceedances types

Returns all exceedances types

### Example


```python
import time
from deutschland import luftqualitaet
from deutschland.luftqualitaet.api import metadata_api
from deutschland.luftqualitaet.model.transgressiontype import Transgressiontype
from pprint import pprint
# Defining the host is optional and defaults to https://www.umweltbundesamt.de/api/air_data/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = luftqualitaet.Configuration(
    host = "https://www.umweltbundesamt.de/api/air_data/v2"
)


# Enter a context with an instance of the API client
with luftqualitaet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    lang = "de" # str | The language code (optional) if omitted the server will use the default value of "en"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all exceedances types
        api_response = api_instance.transgressiontypes_json_get(lang=lang)
        pprint(api_response)
    except luftqualitaet.ApiException as e:
        print("Exception when calling MetadataApi->transgressiontypes_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language code | [optional] if omitted the server will use the default value of "en"

### Return type

[**[Transgressiontype]**](Transgressiontype.md)

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

