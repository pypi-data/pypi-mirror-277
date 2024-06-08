# ModelConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**temperature** | **float** |  | 
**maximum_tokens** | **float** |  | 
**json_mode** | **bool** |  | 

## Example

```python
from openapi_client.models.model_config import ModelConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ModelConfig from a JSON string
model_config_instance = ModelConfig.from_json(json)
# print the JSON string representation of the object
print ModelConfig.to_json()

# convert the object into a dict
model_config_dict = model_config_instance.to_dict()
# create an instance of ModelConfig from a dict
model_config_form_dict = model_config.from_dict(model_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


