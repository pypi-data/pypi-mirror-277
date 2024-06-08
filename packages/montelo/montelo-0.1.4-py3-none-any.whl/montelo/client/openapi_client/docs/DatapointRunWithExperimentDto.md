# DatapointRunWithExperimentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**experiment_id** | **str** |  | 
**datapoint_id** | **str** |  | 
**output** | **object** |  | 
**started_at** | **str** |  | 
**ended_at** | **str** |  | 
**experiment** | [**ExperimentDto**](ExperimentDto.md) |  | 

## Example

```python
from openapi_client.models.datapoint_run_with_experiment_dto import DatapointRunWithExperimentDto

# TODO update the JSON string below
json = "{}"
# create an instance of DatapointRunWithExperimentDto from a JSON string
datapoint_run_with_experiment_dto_instance = DatapointRunWithExperimentDto.from_json(json)
# print the JSON string representation of the object
print DatapointRunWithExperimentDto.to_json()

# convert the object into a dict
datapoint_run_with_experiment_dto_dict = datapoint_run_with_experiment_dto_instance.to_dict()
# create an instance of DatapointRunWithExperimentDto from a dict
datapoint_run_with_experiment_dto_form_dict = datapoint_run_with_experiment_dto.from_dict(datapoint_run_with_experiment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


