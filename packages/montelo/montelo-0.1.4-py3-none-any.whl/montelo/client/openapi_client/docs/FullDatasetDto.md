# FullDatasetDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**env_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**is_generating** | **bool** |  | 
**datapoints** | [**List[DatapointDto]**](DatapointDto.md) |  | 

## Example

```python
from openapi_client.models.full_dataset_dto import FullDatasetDto

# TODO update the JSON string below
json = "{}"
# create an instance of FullDatasetDto from a JSON string
full_dataset_dto_instance = FullDatasetDto.from_json(json)
# print the JSON string representation of the object
print FullDatasetDto.to_json()

# convert the object into a dict
full_dataset_dto_dict = full_dataset_dto_instance.to_dict()
# create an instance of FullDatasetDto from a dict
full_dataset_dto_form_dict = full_dataset_dto.from_dict(full_dataset_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


