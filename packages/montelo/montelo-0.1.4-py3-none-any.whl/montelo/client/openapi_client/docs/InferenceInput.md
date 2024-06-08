# InferenceInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[MessageDto]**](MessageDto.md) |  | 
**tools** | [**List[ToolDto]**](ToolDto.md) |  | [optional] 
**max_tokens** | **float** |  | [optional] 
**prompt_truncate_len** | **float** |  | [optional] 
**temperature** | **float** |  | [optional] 
**top_p** | **float** |  | [optional] 
**top_k** | **float** |  | [optional] 
**frequency_penalty** | **float** |  | [optional] 
**presence_penalty** | **float** |  | [optional] 
**n** | **float** |  | [optional] 
**response_format** | [**ResponseFormatDto**](ResponseFormatDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.inference_input import InferenceInput

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceInput from a JSON string
inference_input_instance = InferenceInput.from_json(json)
# print the JSON string representation of the object
print InferenceInput.to_json()

# convert the object into a dict
inference_input_dict = inference_input_instance.to_dict()
# create an instance of InferenceInput from a dict
inference_input_form_dict = inference_input.from_dict(inference_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


