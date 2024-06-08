# openapi_client.DatapointRunApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datapoint_run_controller_create_datapoint_run**](DatapointRunApi.md#datapoint_run_controller_create_datapoint_run) | **POST** /datapoint-run | 
[**datapoint_run_controller_get_datapoint_with_experiment**](DatapointRunApi.md#datapoint_run_controller_get_datapoint_with_experiment) | **GET** /datapoint-run/{datapointRunId} | 
[**datapoint_run_controller_update_datapoint_run**](DatapointRunApi.md#datapoint_run_controller_update_datapoint_run) | **PATCH** /datapoint-run | 


# **datapoint_run_controller_create_datapoint_run**
> DatapointRunDto datapoint_run_controller_create_datapoint_run(create_datapoint_run_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.create_datapoint_run_input import CreateDatapointRunInput
from openapi_client.models.datapoint_run_dto import DatapointRunDto
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
    api_instance = openapi_client.DatapointRunApi(api_client)
    create_datapoint_run_input = openapi_client.CreateDatapointRunInput() # CreateDatapointRunInput | 

    try:
        api_response = api_instance.datapoint_run_controller_create_datapoint_run(create_datapoint_run_input)
        print("The response of DatapointRunApi->datapoint_run_controller_create_datapoint_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatapointRunApi->datapoint_run_controller_create_datapoint_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_datapoint_run_input** | [**CreateDatapointRunInput**](CreateDatapointRunInput.md)|  | 

### Return type

[**DatapointRunDto**](DatapointRunDto.md)

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

# **datapoint_run_controller_get_datapoint_with_experiment**
> DatapointRunWithExperimentDto datapoint_run_controller_get_datapoint_with_experiment(datapoint_run_id)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.datapoint_run_with_experiment_dto import DatapointRunWithExperimentDto
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
    api_instance = openapi_client.DatapointRunApi(api_client)
    datapoint_run_id = 'datapoint_run_id_example' # str | 

    try:
        api_response = api_instance.datapoint_run_controller_get_datapoint_with_experiment(datapoint_run_id)
        print("The response of DatapointRunApi->datapoint_run_controller_get_datapoint_with_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatapointRunApi->datapoint_run_controller_get_datapoint_with_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datapoint_run_id** | **str**|  | 

### Return type

[**DatapointRunWithExperimentDto**](DatapointRunWithExperimentDto.md)

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

# **datapoint_run_controller_update_datapoint_run**
> SuccessDto datapoint_run_controller_update_datapoint_run(update_datapoint_run_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.success_dto import SuccessDto
from openapi_client.models.update_datapoint_run_input import UpdateDatapointRunInput
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
    api_instance = openapi_client.DatapointRunApi(api_client)
    update_datapoint_run_input = openapi_client.UpdateDatapointRunInput() # UpdateDatapointRunInput | 

    try:
        api_response = api_instance.datapoint_run_controller_update_datapoint_run(update_datapoint_run_input)
        print("The response of DatapointRunApi->datapoint_run_controller_update_datapoint_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatapointRunApi->datapoint_run_controller_update_datapoint_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_datapoint_run_input** | [**UpdateDatapointRunInput**](UpdateDatapointRunInput.md)|  | 

### Return type

[**SuccessDto**](SuccessDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

