# EnvironmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**project_id** | **str** |  | 

## Example

```python
from openapi_client.models.environment_dto import EnvironmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentDto from a JSON string
environment_dto_instance = EnvironmentDto.from_json(json)
# print the JSON string representation of the object
print EnvironmentDto.to_json()

# convert the object into a dict
environment_dto_dict = environment_dto_instance.to_dict()
# create an instance of EnvironmentDto from a dict
environment_dto_form_dict = environment_dto.from_dict(environment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


