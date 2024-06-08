# GenerationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompts** | [**Prompt**](Prompt.md) |  | 
**model_config** | [**ModelConfig**](ModelConfig.md) |  | 

## Example

```python
from openapi_client.models.generation_input import GenerationInput

# TODO update the JSON string below
json = "{}"
# create an instance of GenerationInput from a JSON string
generation_input_instance = GenerationInput.from_json(json)
# print the JSON string representation of the object
print GenerationInput.to_json()

# convert the object into a dict
generation_input_dict = generation_input_instance.to_dict()
# create an instance of GenerationInput from a dict
generation_input_form_dict = generation_input.from_dict(generation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


