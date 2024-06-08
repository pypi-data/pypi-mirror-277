# ToolFunctionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**parameters** | **object** |  | 

## Example

```python
from openapi_client.models.tool_function_dto import ToolFunctionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ToolFunctionDto from a JSON string
tool_function_dto_instance = ToolFunctionDto.from_json(json)
# print the JSON string representation of the object
print ToolFunctionDto.to_json()

# convert the object into a dict
tool_function_dto_dict = tool_function_dto_instance.to_dict()
# create an instance of ToolFunctionDto from a dict
tool_function_dto_form_dict = tool_function_dto.from_dict(tool_function_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


