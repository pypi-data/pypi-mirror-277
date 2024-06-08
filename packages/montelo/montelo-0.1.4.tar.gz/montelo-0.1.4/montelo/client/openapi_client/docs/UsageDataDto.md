# UsageDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_tokens** | **float** |  | 
**total_tokens** | **float** |  | 
**completion_tokens** | **float** |  | 

## Example

```python
from openapi_client.models.usage_data_dto import UsageDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of UsageDataDto from a JSON string
usage_data_dto_instance = UsageDataDto.from_json(json)
# print the JSON string representation of the object
print UsageDataDto.to_json()

# convert the object into a dict
usage_data_dto_dict = usage_data_dto_instance.to_dict()
# create an instance of UsageDataDto from a dict
usage_data_dto_form_dict = usage_data_dto.from_dict(usage_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


