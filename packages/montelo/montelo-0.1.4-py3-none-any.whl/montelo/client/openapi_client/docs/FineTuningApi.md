# openapi_client.FineTuningApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finetune_controller_create_cohere_fine_tune**](FineTuningApi.md#finetune_controller_create_cohere_fine_tune) | **POST** /dataset/{datasetId}/fine-tune/cohere | 
[**finetune_controller_create_fine_tune**](FineTuningApi.md#finetune_controller_create_fine_tune) | **POST** /dataset/{datasetId}/fine-tune | 
[**finetune_controller_create_open_ai_fine_tune**](FineTuningApi.md#finetune_controller_create_open_ai_fine_tune) | **POST** /dataset/{datasetId}/fine-tune/openai | 
[**finetune_controller_get_fine_tunes_for_env**](FineTuningApi.md#finetune_controller_get_fine_tunes_for_env) | **GET** /env/{envId}/fine-tune | 
[**finetune_controller_get_finetune_cost_estimate**](FineTuningApi.md#finetune_controller_get_finetune_cost_estimate) | **GET** /dataset/{datasetId}/fine-tune/cost-estimate | 


# **finetune_controller_create_cohere_fine_tune**
> FineTuneDto finetune_controller_create_cohere_fine_tune(dataset_id, fine_tune_cohere_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.fine_tune_cohere_input import FineTuneCohereInput
from openapi_client.models.fine_tune_dto import FineTuneDto
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
    api_instance = openapi_client.FineTuningApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    fine_tune_cohere_input = openapi_client.FineTuneCohereInput() # FineTuneCohereInput | 

    try:
        api_response = api_instance.finetune_controller_create_cohere_fine_tune(dataset_id, fine_tune_cohere_input)
        print("The response of FineTuningApi->finetune_controller_create_cohere_fine_tune:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningApi->finetune_controller_create_cohere_fine_tune: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **fine_tune_cohere_input** | [**FineTuneCohereInput**](FineTuneCohereInput.md)|  | 

### Return type

[**FineTuneDto**](FineTuneDto.md)

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

# **finetune_controller_create_fine_tune**
> FineTuneDto finetune_controller_create_fine_tune(dataset_id, create_fine_tune_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.create_fine_tune_input import CreateFineTuneInput
from openapi_client.models.fine_tune_dto import FineTuneDto
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
    api_instance = openapi_client.FineTuningApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    create_fine_tune_input = openapi_client.CreateFineTuneInput() # CreateFineTuneInput | 

    try:
        api_response = api_instance.finetune_controller_create_fine_tune(dataset_id, create_fine_tune_input)
        print("The response of FineTuningApi->finetune_controller_create_fine_tune:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningApi->finetune_controller_create_fine_tune: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **create_fine_tune_input** | [**CreateFineTuneInput**](CreateFineTuneInput.md)|  | 

### Return type

[**FineTuneDto**](FineTuneDto.md)

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

# **finetune_controller_create_open_ai_fine_tune**
> FineTuneDto finetune_controller_create_open_ai_fine_tune(dataset_id, fine_tune_openai_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.fine_tune_dto import FineTuneDto
from openapi_client.models.fine_tune_openai_input import FineTuneOpenaiInput
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
    api_instance = openapi_client.FineTuningApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    fine_tune_openai_input = openapi_client.FineTuneOpenaiInput() # FineTuneOpenaiInput | 

    try:
        api_response = api_instance.finetune_controller_create_open_ai_fine_tune(dataset_id, fine_tune_openai_input)
        print("The response of FineTuningApi->finetune_controller_create_open_ai_fine_tune:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningApi->finetune_controller_create_open_ai_fine_tune: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **fine_tune_openai_input** | [**FineTuneOpenaiInput**](FineTuneOpenaiInput.md)|  | 

### Return type

[**FineTuneDto**](FineTuneDto.md)

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

# **finetune_controller_get_fine_tunes_for_env**
> List[FineTuneWithDatasetDto] finetune_controller_get_fine_tunes_for_env(env_id)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.fine_tune_with_dataset_dto import FineTuneWithDatasetDto
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
    api_instance = openapi_client.FineTuningApi(api_client)
    env_id = 'env_id_example' # str | 

    try:
        api_response = api_instance.finetune_controller_get_fine_tunes_for_env(env_id)
        print("The response of FineTuningApi->finetune_controller_get_fine_tunes_for_env:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningApi->finetune_controller_get_fine_tunes_for_env: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_id** | **str**|  | 

### Return type

[**List[FineTuneWithDatasetDto]**](FineTuneWithDatasetDto.md)

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

# **finetune_controller_get_finetune_cost_estimate**
> FinetuneCostEstimateDto finetune_controller_get_finetune_cost_estimate(dataset_id, model, epochs)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.finetune_cost_estimate_dto import FinetuneCostEstimateDto
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
    api_instance = openapi_client.FineTuningApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    model = 'model_example' # str | 
    epochs = 'epochs_example' # str | 

    try:
        api_response = api_instance.finetune_controller_get_finetune_cost_estimate(dataset_id, model, epochs)
        print("The response of FineTuningApi->finetune_controller_get_finetune_cost_estimate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningApi->finetune_controller_get_finetune_cost_estimate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **model** | **str**|  | 
 **epochs** | **str**|  | 

### Return type

[**FinetuneCostEstimateDto**](FinetuneCostEstimateDto.md)

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

