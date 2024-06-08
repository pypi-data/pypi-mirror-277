# openapi_client.DefaultApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_controller_clerk_get_webhook**](DefaultApi.md#webhook_controller_clerk_get_webhook) | **GET** /webhook/clerk | 
[**webhook_controller_clerk_post_webhook**](DefaultApi.md#webhook_controller_clerk_post_webhook) | **POST** /webhook/clerk | 
[**webhook_controller_stripe_post_webhook**](DefaultApi.md#webhook_controller_stripe_post_webhook) | **POST** /webhook/stripe | 


# **webhook_controller_clerk_get_webhook**
> object webhook_controller_clerk_get_webhook()



### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3001"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.webhook_controller_clerk_get_webhook()
        print("The response of DefaultApi->webhook_controller_clerk_get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->webhook_controller_clerk_get_webhook: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_controller_clerk_post_webhook**
> object webhook_controller_clerk_post_webhook()



### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3001"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.webhook_controller_clerk_post_webhook()
        print("The response of DefaultApi->webhook_controller_clerk_post_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->webhook_controller_clerk_post_webhook: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_controller_stripe_post_webhook**
> webhook_controller_stripe_post_webhook()



### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3001"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_instance.webhook_controller_stripe_post_webhook()
    except Exception as e:
        print("Exception when calling DefaultApi->webhook_controller_stripe_post_webhook: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

