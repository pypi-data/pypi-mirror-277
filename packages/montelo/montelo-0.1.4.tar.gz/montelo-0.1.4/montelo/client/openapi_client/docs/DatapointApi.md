# openapi_client.DatapointApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datapoint_controller_batch_create_datapoint**](DatapointApi.md#datapoint_controller_batch_create_datapoint) | **POST** /dataset/{datasetId}/datapoint/batch | 
[**datapoint_controller_create_datapoint**](DatapointApi.md#datapoint_controller_create_datapoint) | **POST** /dataset/{datasetId}/datapoint | 
[**datapoint_controller_delete_datapoint**](DatapointApi.md#datapoint_controller_delete_datapoint) | **DELETE** /datapoint/{datapointId} | 


# **datapoint_controller_batch_create_datapoint**
> datapoint_controller_batch_create_datapoint(dataset_id, batch_add_to_dataset_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.batch_add_to_dataset_input import BatchAddToDatasetInput
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
    api_instance = openapi_client.DatapointApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    batch_add_to_dataset_input = openapi_client.BatchAddToDatasetInput() # BatchAddToDatasetInput | 

    try:
        api_instance.datapoint_controller_batch_create_datapoint(dataset_id, batch_add_to_dataset_input)
    except Exception as e:
        print("Exception when calling DatapointApi->datapoint_controller_batch_create_datapoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **batch_add_to_dataset_input** | [**BatchAddToDatasetInput**](BatchAddToDatasetInput.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datapoint_controller_create_datapoint**
> DatapointDto datapoint_controller_create_datapoint(dataset_id, add_to_dataset_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.add_to_dataset_input import AddToDatasetInput
from openapi_client.models.datapoint_dto import DatapointDto
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
    api_instance = openapi_client.DatapointApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    add_to_dataset_input = openapi_client.AddToDatasetInput() # AddToDatasetInput | 

    try:
        api_response = api_instance.datapoint_controller_create_datapoint(dataset_id, add_to_dataset_input)
        print("The response of DatapointApi->datapoint_controller_create_datapoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatapointApi->datapoint_controller_create_datapoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **add_to_dataset_input** | [**AddToDatasetInput**](AddToDatasetInput.md)|  | 

### Return type

[**DatapointDto**](DatapointDto.md)

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

# **datapoint_controller_delete_datapoint**
> SuccessDto datapoint_controller_delete_datapoint(datapoint_id)



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
    api_instance = openapi_client.DatapointApi(api_client)
    datapoint_id = 'datapoint_id_example' # str | 

    try:
        api_response = api_instance.datapoint_controller_delete_datapoint(datapoint_id)
        print("The response of DatapointApi->datapoint_controller_delete_datapoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatapointApi->datapoint_controller_delete_datapoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datapoint_id** | **str**|  | 

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

