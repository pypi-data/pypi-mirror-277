# openapi_client.InferenceApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inference_controller_inference**](InferenceApi.md#inference_controller_inference) | **POST** /inference/{model} | 


# **inference_controller_inference**
> ChatCompletionDto inference_controller_inference(model, inference_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.chat_completion_dto import ChatCompletionDto
from openapi_client.models.inference_input import InferenceInput
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
    api_instance = openapi_client.InferenceApi(api_client)
    model = 'model_example' # str | 
    inference_input = openapi_client.InferenceInput() # InferenceInput | 

    try:
        api_response = api_instance.inference_controller_inference(model, inference_input)
        print("The response of InferenceApi->inference_controller_inference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->inference_controller_inference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**|  | 
 **inference_input** | [**InferenceInput**](InferenceInput.md)|  | 

### Return type

[**ChatCompletionDto**](ChatCompletionDto.md)

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

