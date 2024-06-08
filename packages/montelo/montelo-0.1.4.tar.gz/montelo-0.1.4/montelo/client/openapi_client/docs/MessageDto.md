# MessageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content** | **str** |  | 

## Example

```python
from openapi_client.models.message_dto import MessageDto

# TODO update the JSON string below
json = "{}"
# create an instance of MessageDto from a JSON string
message_dto_instance = MessageDto.from_json(json)
# print the JSON string representation of the object
print MessageDto.to_json()

# convert the object into a dict
message_dto_dict = message_dto_instance.to_dict()
# create an instance of MessageDto from a dict
message_dto_form_dict = message_dto.from_dict(message_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


