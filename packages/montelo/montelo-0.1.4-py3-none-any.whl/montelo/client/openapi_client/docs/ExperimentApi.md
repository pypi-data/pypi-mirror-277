# openapi_client.ExperimentApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experiment_controller_create**](ExperimentApi.md#experiment_controller_create) | **POST** /dataset/{datasetId}/experiment | 
[**experiment_controller_get_analytics_for_experiment**](ExperimentApi.md#experiment_controller_get_analytics_for_experiment) | **GET** /experiment/{experimentId}/analytics | 
[**experiment_controller_get_evals_for_experiment**](ExperimentApi.md#experiment_controller_get_evals_for_experiment) | **GET** /experiment/{experimentId}/evals | 
[**experiment_controller_get_experiments_for_dataset**](ExperimentApi.md#experiment_controller_get_experiments_for_dataset) | **GET** /dataset/{datasetId}/experiment | 
[**experiment_controller_get_paginated_datapoints_for_experiment**](ExperimentApi.md#experiment_controller_get_paginated_datapoints_for_experiment) | **GET** /experiment/{experimentId}/datapoints | 
[**experiment_controller_get_paginated_experiment_with_datapoint_runs**](ExperimentApi.md#experiment_controller_get_paginated_experiment_with_datapoint_runs) | **GET** /experiment/{experimentId} | 
[**experiment_controller_get_paginated_experiments_for_environment**](ExperimentApi.md#experiment_controller_get_paginated_experiments_for_environment) | **GET** /env/{envId}/experiment | 


# **experiment_controller_create**
> ExperimentDto experiment_controller_create(dataset_id, create_experiment_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.create_experiment_input import CreateExperimentInput
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
    api_instance = openapi_client.ExperimentApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    create_experiment_input = openapi_client.CreateExperimentInput() # CreateExperimentInput | 

    try:
        api_response = api_instance.experiment_controller_create(dataset_id, create_experiment_input)
        print("The response of ExperimentApi->experiment_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiment_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **create_experiment_input** | [**CreateExperimentInput**](CreateExperimentInput.md)|  | 

### Return type

[**ExperimentDto**](ExperimentDto.md)

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

# **experiment_controller_get_analytics_for_experiment**
> ExperimentAnalyticsDto experiment_controller_get_analytics_for_experiment(experiment_id)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.experiment_analytics_dto import ExperimentAnalyticsDto
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
    api_instance = openapi_client.ExperimentApi(api_client)
    experiment_id = 'experiment_id_example' # str | 

    try:
        api_response = api_instance.experiment_controller_get_analytics_for_experiment(experiment_id)
        print("The response of ExperimentApi->experiment_controller_get_analytics_for_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiment_controller_get_analytics_for_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **str**|  | 

### Return type

[**ExperimentAnalyticsDto**](ExperimentAnalyticsDto.md)

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

# **experiment_controller_get_evals_for_experiment**
> ExperimentEvalsDto experiment_controller_get_evals_for_experiment(experiment_id)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.experiment_evals_dto import ExperimentEvalsDto
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
    api_instance = openapi_client.ExperimentApi(api_client)
    experiment_id = 'experiment_id_example' # str | 

    try:
        api_response = api_instance.experiment_controller_get_evals_for_experiment(experiment_id)
        print("The response of ExperimentApi->experiment_controller_get_evals_for_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiment_controller_get_evals_for_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **str**|  | 

### Return type

[**ExperimentEvalsDto**](ExperimentEvalsDto.md)

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

# **experiment_controller_get_experiments_for_dataset**
> List[ExperimentDto] experiment_controller_get_experiments_for_dataset(dataset_id)



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
    api_instance = openapi_client.ExperimentApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_response = api_instance.experiment_controller_get_experiments_for_dataset(dataset_id)
        print("The response of ExperimentApi->experiment_controller_get_experiments_for_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiment_controller_get_experiments_for_dataset: %s\n" % e)
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

# **experiment_controller_get_paginated_datapoints_for_experiment**
> PaginatedExperimentWithDatapointsDto experiment_controller_get_paginated_datapoints_for_experiment(experiment_id, take=take, skip=skip)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.paginated_experiment_with_datapoints_dto import PaginatedExperimentWithDatapointsDto
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
    api_instance = openapi_client.ExperimentApi(api_client)
    experiment_id = 'experiment_id_example' # str | 
    take = 'take_example' # str |  (optional)
    skip = 'skip_example' # str |  (optional)

    try:
        api_response = api_instance.experiment_controller_get_paginated_datapoints_for_experiment(experiment_id, take=take, skip=skip)
        print("The response of ExperimentApi->experiment_controller_get_paginated_datapoints_for_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiment_controller_get_paginated_datapoints_for_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **str**|  | 
 **take** | **str**|  | [optional] 
 **skip** | **str**|  | [optional] 

### Return type

[**PaginatedExperimentWithDatapointsDto**](PaginatedExperimentWithDatapointsDto.md)

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

# **experiment_controller_get_paginated_experiment_with_datapoint_runs**
> PaginatedExperimentWithDatapointRunsDto experiment_controller_get_paginated_experiment_with_datapoint_runs(experiment_id, take=take, skip=skip)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.paginated_experiment_with_datapoint_runs_dto import PaginatedExperimentWithDatapointRunsDto
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
    api_instance = openapi_client.ExperimentApi(api_client)
    experiment_id = 'experiment_id_example' # str | 
    take = 'take_example' # str |  (optional)
    skip = 'skip_example' # str |  (optional)

    try:
        api_response = api_instance.experiment_controller_get_paginated_experiment_with_datapoint_runs(experiment_id, take=take, skip=skip)
        print("The response of ExperimentApi->experiment_controller_get_paginated_experiment_with_datapoint_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiment_controller_get_paginated_experiment_with_datapoint_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **str**|  | 
 **take** | **str**|  | [optional] 
 **skip** | **str**|  | [optional] 

### Return type

[**PaginatedExperimentWithDatapointRunsDto**](PaginatedExperimentWithDatapointRunsDto.md)

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

# **experiment_controller_get_paginated_experiments_for_environment**
> PaginatedExperimentsDto experiment_controller_get_paginated_experiments_for_environment(env_id, take=take, skip=skip)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.paginated_experiments_dto import PaginatedExperimentsDto
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
    api_instance = openapi_client.ExperimentApi(api_client)
    env_id = 'env_id_example' # str | 
    take = 'take_example' # str |  (optional)
    skip = 'skip_example' # str |  (optional)

    try:
        api_response = api_instance.experiment_controller_get_paginated_experiments_for_environment(env_id, take=take, skip=skip)
        print("The response of ExperimentApi->experiment_controller_get_paginated_experiments_for_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentApi->experiment_controller_get_paginated_experiments_for_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_id** | **str**|  | 
 **take** | **str**|  | [optional] 
 **skip** | **str**|  | [optional] 

### Return type

[**PaginatedExperimentsDto**](PaginatedExperimentsDto.md)

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

