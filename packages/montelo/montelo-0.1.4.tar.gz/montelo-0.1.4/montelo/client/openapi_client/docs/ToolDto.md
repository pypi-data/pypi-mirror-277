# ToolDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**function** | [**ToolFunctionDto**](ToolFunctionDto.md) |  | 

## Example

```python
from openapi_client.models.tool_dto import ToolDto

# TODO update the JSON string below
json = "{}"
# create an instance of ToolDto from a JSON string
tool_dto_instance = ToolDto.from_json(json)
# print the JSON string representation of the object
print ToolDto.to_json()

# convert the object into a dict
tool_dto_dict = tool_dto_instance.to_dict()
# create an instance of ToolDto from a dict
tool_dto_form_dict = tool_dto.from_dict(tool_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


