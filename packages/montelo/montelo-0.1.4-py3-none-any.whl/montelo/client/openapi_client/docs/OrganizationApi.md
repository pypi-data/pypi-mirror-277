# openapi_client.OrganizationApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_controller_create_project**](OrganizationApi.md#organization_controller_create_project) | **POST** /organization | 
[**organization_controller_get_projects_for_org**](OrganizationApi.md#organization_controller_get_projects_for_org) | **GET** /organization | 


# **organization_controller_create_project**
> FullProjectDto organization_controller_create_project(create_project_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.create_project_input import CreateProjectInput
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
    api_instance = openapi_client.OrganizationApi(api_client)
    create_project_input = openapi_client.CreateProjectInput() # CreateProjectInput | 

    try:
        api_response = api_instance.organization_controller_create_project(create_project_input)
        print("The response of OrganizationApi->organization_controller_create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_controller_create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_input** | [**CreateProjectInput**](CreateProjectInput.md)|  | 

### Return type

[**FullProjectDto**](FullProjectDto.md)

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

# **organization_controller_get_projects_for_org**
> List[FullProjectDto] organization_controller_get_projects_for_org()



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
    api_instance = openapi_client.OrganizationApi(api_client)

    try:
        api_response = api_instance.organization_controller_get_projects_for_org()
        print("The response of OrganizationApi->organization_controller_get_projects_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_controller_get_projects_for_org: %s\n" % e)
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

