# ExperimentEvalsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment** | [**ExperimentDto**](ExperimentDto.md) |  | 
**charts** | [**List[ExperimentEvalsChartDto]**](ExperimentEvalsChartDto.md) |  | 

## Example

```python
from openapi_client.models.experiment_evals_dto import ExperimentEvalsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentEvalsDto from a JSON string
experiment_evals_dto_instance = ExperimentEvalsDto.from_json(json)
# print the JSON string representation of the object
print ExperimentEvalsDto.to_json()

# convert the object into a dict
experiment_evals_dto_dict = experiment_evals_dto_instance.to_dict()
# create an instance of ExperimentEvalsDto from a dict
experiment_evals_dto_form_dict = experiment_evals_dto.from_dict(experiment_evals_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


