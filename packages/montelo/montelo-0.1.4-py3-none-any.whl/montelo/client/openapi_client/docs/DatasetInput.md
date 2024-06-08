# DatasetInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**samples** | **float** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**train_split_ratio** | **float** |  | 

## Example

```python
from openapi_client.models.dataset_input import DatasetInput

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetInput from a JSON string
dataset_input_instance = DatasetInput.from_json(json)
# print the JSON string representation of the object
print DatasetInput.to_json()

# convert the object into a dict
dataset_input_dict = dataset_input_instance.to_dict()
# create an instance of DatasetInput from a dict
dataset_input_form_dict = dataset_input.from_dict(dataset_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


