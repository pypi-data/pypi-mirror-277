# openapi_client.DatasetApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataset_controller_create_dataset**](DatasetApi.md#dataset_controller_create_dataset) | **POST** /dataset | 
[**dataset_controller_delete_dataset**](DatasetApi.md#dataset_controller_delete_dataset) | **DELETE** /dataset/{datasetId} | 
[**dataset_controller_download_dataset**](DatasetApi.md#dataset_controller_download_dataset) | **GET** /dataset/{datasetId}/download | 
[**dataset_controller_get_all_datasets_for_env**](DatasetApi.md#dataset_controller_get_all_datasets_for_env) | **GET** /env/{envId}/dataset | 
[**dataset_controller_get_dataset_recent_experiments**](DatasetApi.md#dataset_controller_get_dataset_recent_experiments) | **GET** /dataset/{datasetId}/experiments | 
[**dataset_controller_get_dataset_with_datapoints**](DatasetApi.md#dataset_controller_get_dataset_with_datapoints) | **GET** /dataset/{datasetId} | 


# **dataset_controller_create_dataset**
> DatasetDto dataset_controller_create_dataset(create_dataset_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.create_dataset_input import CreateDatasetInput
from openapi_client.models.dataset_dto import DatasetDto
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
    api_instance = openapi_client.DatasetApi(api_client)
    create_dataset_input = openapi_client.CreateDatasetInput() # CreateDatasetInput | 

    try:
        api_response = api_instance.dataset_controller_create_dataset(create_dataset_input)
        print("The response of DatasetApi->dataset_controller_create_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_controller_create_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dataset_input** | [**CreateDatasetInput**](CreateDatasetInput.md)|  | 

### Return type

[**DatasetDto**](DatasetDto.md)

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

# **dataset_controller_delete_dataset**
> SuccessDto dataset_controller_delete_dataset(dataset_id)



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
    api_instance = openapi_client.DatasetApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_response = api_instance.dataset_controller_delete_dataset(dataset_id)
        print("The response of DatasetApi->dataset_controller_delete_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_controller_delete_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

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

# **dataset_controller_download_dataset**
> dataset_controller_download_dataset(dataset_id)



### Example

* Bearer (JWT) Authentication (bearer):

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
    api_instance = openapi_client.DatasetApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.dataset_controller_download_dataset(dataset_id)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_controller_download_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dataset_controller_get_all_datasets_for_env**
> List[DatasetDto] dataset_controller_get_all_datasets_for_env(env_id)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.dataset_dto import DatasetDto
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
    api_instance = openapi_client.DatasetApi(api_client)
    env_id = 'env_id_example' # str | 

    try:
        api_response = api_instance.dataset_controller_get_all_datasets_for_env(env_id)
        print("The response of DatasetApi->dataset_controller_get_all_datasets_for_env:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_controller_get_all_datasets_for_env: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_id** | **str**|  | 

### Return type

[**List[DatasetDto]**](DatasetDto.md)

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

# **dataset_controller_get_dataset_recent_experiments**
> List[ExperimentDto] dataset_controller_get_dataset_recent_experiments(dataset_id)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.experiment_dto import ExperimentDto
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
    api_instance = openapi_client.DatasetApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_response = api_instance.dataset_controller_get_dataset_recent_experiments(dataset_id)
        print("The response of DatasetApi->dataset_controller_get_dataset_recent_experiments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_controller_get_dataset_recent_experiments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

[**List[ExperimentDto]**](ExperimentDto.md)

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

# **dataset_controller_get_dataset_with_datapoints**
> FullDatasetWithCountDto dataset_controller_get_dataset_with_datapoints(dataset_id, take=take, skip=skip)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.full_dataset_with_count_dto import FullDatasetWithCountDto
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
    api_instance = openapi_client.DatasetApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    take = 'take_example' # str | How many traces to get. If undefined returns all. (optional)
    skip = 'skip_example' # str | How many traces to skip. If undefined starts from beginning. (optional)

    try:
        api_response = api_instance.dataset_controller_get_dataset_with_datapoints(dataset_id, take=take, skip=skip)
        print("The response of DatasetApi->dataset_controller_get_dataset_with_datapoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_controller_get_dataset_with_datapoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **take** | **str**| How many traces to get. If undefined returns all. | [optional] 
 **skip** | **str**| How many traces to skip. If undefined starts from beginning. | [optional] 

### Return type

[**FullDatasetWithCountDto**](FullDatasetWithCountDto.md)

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

