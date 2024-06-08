# openapi_client.ProjectApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_controller_delete_project**](ProjectApi.md#project_controller_delete_project) | **DELETE** /project | 
[**project_controller_get_all_projects**](ProjectApi.md#project_controller_get_all_projects) | **GET** /project/all | 
[**project_controller_get_project**](ProjectApi.md#project_controller_get_project) | **GET** /project | 
[**project_controller_set_cohere_api_key**](ProjectApi.md#project_controller_set_cohere_api_key) | **POST** /project/cohere-api-key | 
[**project_controller_set_open_aiapi_key**](ProjectApi.md#project_controller_set_open_aiapi_key) | **POST** /project/openai-api-key | 


# **project_controller_delete_project**
> SuccessDto project_controller_delete_project()



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.success_dto import SuccessDto
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
    api_instance = openapi_client.ProjectApi(api_client)

    try:
        api_response = api_instance.project_controller_delete_project()
        print("The response of ProjectApi->project_controller_delete_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_controller_delete_project: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuccessDto**](SuccessDto.md)

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

# **project_controller_get_all_projects**
> List[FullProjectDto] project_controller_get_all_projects()



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.full_project_dto import FullProjectDto
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
    api_instance = openapi_client.ProjectApi(api_client)

    try:
        api_response = api_instance.project_controller_get_all_projects()
        print("The response of ProjectApi->project_controller_get_all_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_controller_get_all_projects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FullProjectDto]**](FullProjectDto.md)

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

# **project_controller_get_project**
> FullProjectDto project_controller_get_project()



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.full_project_dto import FullProjectDto
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
    api_instance = openapi_client.ProjectApi(api_client)

    try:
        api_response = api_instance.project_controller_get_project()
        print("The response of ProjectApi->project_controller_get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_controller_get_project: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FullProjectDto**](FullProjectDto.md)

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

# **project_controller_set_cohere_api_key**
> ProjectDto project_controller_set_cohere_api_key(set_cohere_api_key_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.project_dto import ProjectDto
from openapi_client.models.set_cohere_api_key_input import SetCohereApiKeyInput
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
    api_instance = openapi_client.ProjectApi(api_client)
    set_cohere_api_key_input = openapi_client.SetCohereApiKeyInput() # SetCohereApiKeyInput | 

    try:
        api_response = api_instance.project_controller_set_cohere_api_key(set_cohere_api_key_input)
        print("The response of ProjectApi->project_controller_set_cohere_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_controller_set_cohere_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_cohere_api_key_input** | [**SetCohereApiKeyInput**](SetCohereApiKeyInput.md)|  | 

### Return type

[**ProjectDto**](ProjectDto.md)

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

# **project_controller_set_open_aiapi_key**
> ProjectDto project_controller_set_open_aiapi_key(set_openai_api_key_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.project_dto import ProjectDto
from openapi_client.models.set_openai_api_key_input import SetOpenaiApiKeyInput
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
    api_instance = openapi_client.ProjectApi(api_client)
    set_openai_api_key_input = openapi_client.SetOpenaiApiKeyInput() # SetOpenaiApiKeyInput | 

    try:
        api_response = api_instance.project_controller_set_open_aiapi_key(set_openai_api_key_input)
        print("The response of ProjectApi->project_controller_set_open_aiapi_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_controller_set_open_aiapi_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_openai_api_key_input** | [**SetOpenaiApiKeyInput**](SetOpenaiApiKeyInput.md)|  | 

### Return type

[**ProjectDto**](ProjectDto.md)

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

