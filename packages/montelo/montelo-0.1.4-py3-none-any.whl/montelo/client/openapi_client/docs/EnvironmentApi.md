# openapi_client.EnvironmentApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environment_controller_create_env**](EnvironmentApi.md#environment_controller_create_env) | **POST** /env | 
[**environment_controller_get_env**](EnvironmentApi.md#environment_controller_get_env) | **GET** /env/{envId} | 


# **environment_controller_create_env**
> EnvironmentDto environment_controller_create_env(create_env_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.create_env_input import CreateEnvInput
from openapi_client.models.environment_dto import EnvironmentDto
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
    api_instance = openapi_client.EnvironmentApi(api_client)
    create_env_input = openapi_client.CreateEnvInput() # CreateEnvInput | 

    try:
        api_response = api_instance.environment_controller_create_env(create_env_input)
        print("The response of EnvironmentApi->environment_controller_create_env:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentApi->environment_controller_create_env: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_env_input** | [**CreateEnvInput**](CreateEnvInput.md)|  | 

### Return type

[**EnvironmentDto**](EnvironmentDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environment_controller_get_env**
> EnvironmentDto environment_controller_get_env(env_id)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.environment_dto import EnvironmentDto
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
    api_instance = openapi_client.EnvironmentApi(api_client)
    env_id = 'env_id_example' # str | 

    try:
        api_response = api_instance.environment_controller_get_env(env_id)
        print("The response of EnvironmentApi->environment_controller_get_env:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentApi->environment_controller_get_env: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_id** | **str**|  | 

### Return type

[**EnvironmentDto**](EnvironmentDto.md)

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

