# FullDatapointRunDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**output** | **object** |  | 
**evaluation** | **object** |  | 
**experiment_id** | **str** |  | 
**datapoint_id** | **str** |  | 
**created_at** | **str** |  | 
**datapoint** | [**DatapointDto**](DatapointDto.md) |  | 

## Example

```python
from openapi_client.models.full_datapoint_run_dto import FullDatapointRunDto

# TODO update the JSON string below
json = "{}"
# create an instance of FullDatapointRunDto from a JSON string
full_datapoint_run_dto_instance = FullDatapointRunDto.from_json(json)
# print the JSON string representation of the object
print FullDatapointRunDto.to_json()

# convert the object into a dict
full_datapoint_run_dto_dict = full_datapoint_run_dto_instance.to_dict()
# create an instance of FullDatapointRunDto from a dict
full_datapoint_run_dto_form_dict = full_datapoint_run_dto.from_dict(full_datapoint_run_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


