# SubscriptionTierBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the subscription tier. | [optional] 
**slug** | **str** | The slug identifier of the subscription tier. | [optional] 
**included_repositories** | **int** | The number of repositories included in the subscription tier. &#x60;0&#x60; indicates that the subscription tier includes unlimited repositories. | [optional] 
**included_storage_bytes** | **int** | The amount of storage included in the subscription tier in bytes. | [optional] 
**allow_storage_overage** | **bool** | A boolean indicating whether the subscription tier supports additional storage above what is included in the base plan at an additional cost per GiB used. | [optional] 
**included_bandwidth_bytes** | **int** | The amount of outbound data transfer included in the subscription tier in bytes. | [optional] 
**monthly_price_in_cents** | **int** | The monthly cost of the subscription tier in cents. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


