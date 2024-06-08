# CreateFineTuneInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**epochs** | **float** |  | 

## Example

```python
from openapi_client.models.create_fine_tune_input import CreateFineTuneInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFineTuneInput from a JSON string
create_fine_tune_input_instance = CreateFineTuneInput.from_json(json)
# print the JSON string representation of the object
print CreateFineTuneInput.to_json()

# convert the object into a dict
create_fine_tune_input_dict = create_fine_tune_input_instance.to_dict()
# create an instance of CreateFineTuneInput from a dict
create_fine_tune_input_form_dict = create_fine_tune_input.from_dict(create_fine_tune_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


