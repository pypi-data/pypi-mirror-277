# openapi_client.ApiKeyApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_controller_get_api_keys_for_project**](ApiKeyApi.md#api_key_controller_get_api_keys_for_project) | **GET** /api-keys | 
[**api_key_controller_reveal_one**](ApiKeyApi.md#api_key_controller_reveal_one) | **GET** /api-keys/{apiKeyId} | 
[**api_key_controller_rotate_one**](ApiKeyApi.md#api_key_controller_rotate_one) | **POST** /api-keys/{apiKeyId} | 


# **api_key_controller_get_api_keys_for_project**
> List[ApiKeyWithEnvDto] api_key_controller_get_api_keys_for_project()



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.api_key_with_env_dto import ApiKeyWithEnvDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApiKeyApi(api_client)

    try:
        api_response = api_instance.api_key_controller_get_api_keys_for_project()
        print("The response of ApiKeyApi->api_key_controller_get_api_keys_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->api_key_controller_get_api_keys_for_project: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiKeyWithEnvDto]**](ApiKeyWithEnvDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_controller_reveal_one**
> ApiKeyWithEnvDto api_key_controller_reveal_one(api_key_id)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.api_key_with_env_dto import ApiKeyWithEnvDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApiKeyApi(api_client)
    api_key_id = 'api_key_id_example' # str | 

    try:
        api_response = api_instance.api_key_controller_reveal_one(api_key_id)
        print("The response of ApiKeyApi->api_key_controller_reveal_one:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->api_key_controller_reveal_one: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**|  | 

### Return type

[**ApiKeyWithEnvDto**](ApiKeyWithEnvDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_controller_rotate_one**
> ApiKeyWithEnvDto api_key_controller_rotate_one(api_key_id)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.api_key_with_env_dto import ApiKeyWithEnvDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApiKeyApi(api_client)
    api_key_id = 'api_key_id_example' # str | 

    try:
        api_response = api_instance.api_key_controller_rotate_one(api_key_id)
        print("The response of ApiKeyApi->api_key_controller_rotate_one:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->api_key_controller_rotate_one: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**|  | 

### Return type

[**ApiKeyWithEnvDto**](ApiKeyWithEnvDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

