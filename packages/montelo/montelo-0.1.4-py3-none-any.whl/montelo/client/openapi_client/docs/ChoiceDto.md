# ChoiceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** |  | 
**message** | [**MessageDto**](MessageDto.md) |  | 
**finish_reason** | **str** |  | 

## Example

```python
from openapi_client.models.choice_dto import ChoiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceDto from a JSON string
choice_dto_instance = ChoiceDto.from_json(json)
# print the JSON string representation of the object
print ChoiceDto.to_json()

# convert the object into a dict
choice_dto_dict = choice_dto_instance.to_dict()
# create an instance of ChoiceDto from a dict
choice_dto_form_dict = choice_dto.from_dict(choice_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


