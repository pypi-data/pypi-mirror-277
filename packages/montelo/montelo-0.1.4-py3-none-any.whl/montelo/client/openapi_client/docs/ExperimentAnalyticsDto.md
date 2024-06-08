# ExperimentAnalyticsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_duration** | **str** |  | 
**avg_duration** | **str** |  | 

## Example

```python
from openapi_client.models.experiment_analytics_dto import ExperimentAnalyticsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentAnalyticsDto from a JSON string
experiment_analytics_dto_instance = ExperimentAnalyticsDto.from_json(json)
# print the JSON string representation of the object
print ExperimentAnalyticsDto.to_json()

# convert the object into a dict
experiment_analytics_dto_dict = experiment_analytics_dto_instance.to_dict()
# create an instance of ExperimentAnalyticsDto from a dict
experiment_analytics_dto_form_dict = experiment_analytics_dto.from_dict(experiment_analytics_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


