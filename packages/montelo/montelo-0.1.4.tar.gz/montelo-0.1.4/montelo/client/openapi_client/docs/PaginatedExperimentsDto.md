# PaginatedExperimentsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiments** | [**List[ExperimentDto]**](ExperimentDto.md) |  | 
**total_count** | **float** |  | 

## Example

```python
from openapi_client.models.paginated_experiments_dto import PaginatedExperimentsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedExperimentsDto from a JSON string
paginated_experiments_dto_instance = PaginatedExperimentsDto.from_json(json)
# print the JSON string representation of the object
print PaginatedExperimentsDto.to_json()

# convert the object into a dict
paginated_experiments_dto_dict = paginated_experiments_dto_instance.to_dict()
# create an instance of PaginatedExperimentsDto from a dict
paginated_experiments_dto_form_dict = paginated_experiments_dto.from_dict(paginated_experiments_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


