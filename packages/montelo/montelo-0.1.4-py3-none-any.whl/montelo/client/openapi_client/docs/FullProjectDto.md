# FullProjectDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**org_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**openai_api_key** | **str** |  | 
**cohere_api_key** | **str** |  | 
**environments** | [**List[EnvironmentDto]**](EnvironmentDto.md) |  | 

## Example

```python
from openapi_client.models.full_project_dto import FullProjectDto

# TODO update the JSON string below
json = "{}"
# create an instance of FullProjectDto from a JSON string
full_project_dto_instance = FullProjectDto.from_json(json)
# print the JSON string representation of the object
print FullProjectDto.to_json()

# convert the object into a dict
full_project_dto_dict = full_project_dto_instance.to_dict()
# create an instance of FullProjectDto from a dict
full_project_dto_form_dict = full_project_dto.from_dict(full_project_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


