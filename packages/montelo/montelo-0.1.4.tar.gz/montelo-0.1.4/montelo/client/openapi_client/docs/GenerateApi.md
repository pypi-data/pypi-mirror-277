# openapi_client.GenerateApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_controller_generate**](GenerateApi.md#generate_controller_generate) | **POST** /generate | 


# **generate_controller_generate**
> DatasetDto generate_controller_generate(generate_input)



### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.dataset_dto import DatasetDto
from openapi_client.models.generate_input import GenerateInput
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
    api_instance = openapi_client.GenerateApi(api_client)
    generate_input = openapi_client.GenerateInput() # GenerateInput | 

    try:
        api_response = api_instance.generate_controller_generate(generate_input)
        print("The response of GenerateApi->generate_controller_generate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerateApi->generate_controller_generate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_input** | [**GenerateInput**](GenerateInput.md)|  | 

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

