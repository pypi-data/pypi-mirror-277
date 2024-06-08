# PaginatedExperimentWithDatapointRunsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment** | [**ExperimentWithDatapointRunsDto**](ExperimentWithDatapointRunsDto.md) |  | 
**total_datapoint_runs** | **float** |  | 

## Example

```python
from openapi_client.models.paginated_experiment_with_datapoint_runs_dto import PaginatedExperimentWithDatapointRunsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedExperimentWithDatapointRunsDto from a JSON string
paginated_experiment_with_datapoint_runs_dto_instance = PaginatedExperimentWithDatapointRunsDto.from_json(json)
# print the JSON string representation of the object
print PaginatedExperimentWithDatapointRunsDto.to_json()

# convert the object into a dict
paginated_experiment_with_datapoint_runs_dto_dict = paginated_experiment_with_datapoint_runs_dto_instance.to_dict()
# create an instance of PaginatedExperimentWithDatapointRunsDto from a dict
paginated_experiment_with_datapoint_runs_dto_form_dict = paginated_experiment_with_datapoint_runs_dto.from_dict(paginated_experiment_with_datapoint_runs_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


