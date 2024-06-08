# ExperimentEvalsChartDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**var_property** | **str** |  | 
**values** | [**List[ExperimentEvalsValueDto]**](ExperimentEvalsValueDto.md) |  | 

## Example

```python
from openapi_client.models.experiment_evals_chart_dto import ExperimentEvalsChartDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentEvalsChartDto from a JSON string
experiment_evals_chart_dto_instance = ExperimentEvalsChartDto.from_json(json)
# print the JSON string representation of the object
print ExperimentEvalsChartDto.to_json()

# convert the object into a dict
experiment_evals_chart_dto_dict = experiment_evals_chart_dto_instance.to_dict()
# create an instance of ExperimentEvalsChartDto from a dict
experiment_evals_chart_dto_form_dict = experiment_evals_chart_dto.from_dict(experiment_evals_chart_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


