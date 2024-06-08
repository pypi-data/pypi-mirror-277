# FineTuneWithDatasetDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**provider** | **str** |  | 
**model** | **str** |  | 
**identifier** | **str** |  | 
**status** | **str** |  | 
**started_at** | **str** |  | 
**ended_at** | **str** |  | 
**metadata** | **object** |  | 
**dataset_id** | **str** |  | 
**dataset** | [**DatasetDto**](DatasetDto.md) |  | 

## Example

```python
from openapi_client.models.fine_tune_with_dataset_dto import FineTuneWithDatasetDto

# TODO update the JSON string below
json = "{}"
# create an instance of FineTuneWithDatasetDto from a JSON string
fine_tune_with_dataset_dto_instance = FineTuneWithDatasetDto.from_json(json)
# print the JSON string representation of the object
print FineTuneWithDatasetDto.to_json()

# convert the object into a dict
fine_tune_with_dataset_dto_dict = fine_tune_with_dataset_dto_instance.to_dict()
# create an instance of FineTuneWithDatasetDto from a dict
fine_tune_with_dataset_dto_form_dict = fine_tune_with_dataset_dto.from_dict(fine_tune_with_dataset_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


