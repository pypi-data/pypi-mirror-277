# SubscriptionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**stripe_customer_id** | **str** |  | 
**stripe_subscription_id** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from openapi_client.models.subscription_dto import SubscriptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDto from a JSON string
subscription_dto_instance = SubscriptionDto.from_json(json)
# print the JSON string representation of the object
print SubscriptionDto.to_json()

# convert the object into a dict
subscription_dto_dict = subscription_dto_instance.to_dict()
# create an instance of SubscriptionDto from a dict
subscription_dto_form_dict = subscription_dto.from_dict(subscription_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


