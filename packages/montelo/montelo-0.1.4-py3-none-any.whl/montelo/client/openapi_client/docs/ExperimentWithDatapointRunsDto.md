# ExperimentWithDatapointRunsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**dataset_id** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created_at** | **str** |  | 
**dataset** | [**DatasetDto**](DatasetDto.md) |  | 
**datapoint_runs** | [**List[FullDatapointRunDto]**](FullDatapointRunDto.md) |  | 

## Example

```python
from openapi_client.models.experiment_with_datapoint_runs_dto import ExperimentWithDatapointRunsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentWithDatapointRunsDto from a JSON string
experiment_with_datapoint_runs_dto_instance = ExperimentWithDatapointRunsDto.from_json(json)
# print the JSON string representation of the object
print ExperimentWithDatapointRunsDto.to_json()

# convert the object into a dict
experiment_with_datapoint_runs_dto_dict = experiment_with_datapoint_runs_dto_instance.to_dict()
# create an instance of ExperimentWithDatapointRunsDto from a dict
experiment_with_datapoint_runs_dto_form_dict = experiment_with_datapoint_runs_dto.from_dict(experiment_with_datapoint_runs_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


