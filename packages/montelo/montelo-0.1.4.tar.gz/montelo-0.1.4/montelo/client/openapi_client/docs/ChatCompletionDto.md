# ChatCompletionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**created** | **float** |  | 
**model** | **str** |  | 
**choices** | [**List[ChoiceDto]**](ChoiceDto.md) |  | 
**usage** | [**UsageDataDto**](UsageDataDto.md) |  | 

## Example

```python
from openapi_client.models.chat_completion_dto import ChatCompletionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionDto from a JSON string
chat_completion_dto_instance = ChatCompletionDto.from_json(json)
# print the JSON string representation of the object
print ChatCompletionDto.to_json()

# convert the object into a dict
chat_completion_dto_dict = chat_completion_dto_instance.to_dict()
# create an instance of ChatCompletionDto from a dict
chat_completion_dto_form_dict = chat_completion_dto.from_dict(chat_completion_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


