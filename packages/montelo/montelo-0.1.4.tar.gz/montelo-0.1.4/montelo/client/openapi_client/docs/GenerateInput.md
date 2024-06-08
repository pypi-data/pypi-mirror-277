# GenerateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generation** | [**GenerationInput**](GenerationInput.md) |  | 
**variables** | [**VariablesInput**](VariablesInput.md) |  | 
**dataset** | [**DatasetInput**](DatasetInput.md) |  | 

## Example

```python
from openapi_client.models.generate_input import GenerateInput

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateInput from a JSON string
generate_input_instance = GenerateInput.from_json(json)
# print the JSON string representation of the object
print GenerateInput.to_json()

# convert the object into a dict
generate_input_dict = generate_input_instance.to_dict()
# create an instance of GenerateInput from a dict
generate_input_form_dict = generate_input.from_dict(generate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


