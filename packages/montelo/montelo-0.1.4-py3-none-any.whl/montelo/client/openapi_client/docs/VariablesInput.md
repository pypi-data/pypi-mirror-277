# VariablesInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system** | [**List[Config]**](Config.md) |  | 
**user** | [**List[Config]**](Config.md) |  | 

## Example

```python
from openapi_client.models.variables_input import VariablesInput

# TODO update the JSON string below
json = "{}"
# create an instance of VariablesInput from a JSON string
variables_input_instance = VariablesInput.from_json(json)
# print the JSON string representation of the object
print VariablesInput.to_json()

# convert the object into a dict
variables_input_dict = variables_input_instance.to_dict()
# create an instance of VariablesInput from a dict
variables_input_form_dict = variables_input.from_dict(variables_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


