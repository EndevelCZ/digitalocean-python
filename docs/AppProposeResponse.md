# AppProposeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_is_static** | **bool** | Indicates whether the app is a static app. | [optional] 
**app_name_available** | **bool** | Indicates whether the app name is available. | [optional] 
**app_name_suggestion** | **str** | The suggested name if the proposed app name is unavailable. | [optional] 
**existing_static_apps** | **str** | The maximum number of free static apps the account can have. We will charge you for any additional static apps. | [optional] 
**spec** | [**AppSpec**](AppSpec.md) |  | [optional] 
**app_cost** | **int** | The monthly cost of the proposed app in USD using the next pricing plan tier. For example, if you propose an app that uses the Basic tier, the &#x60;app_tier_upgrade_cost&#x60; field displays the monthly cost of the app if it were to use the Professional tier. If the proposed app already uses the most expensive tier, the field is empty. | [optional] 
**app_tier_downgrade_cost** | **int** | The monthly cost of the proposed app in USD using the previous pricing plan tier. For example, if you propose an app that uses the Professional tier, the &#x60;app_tier_downgrade_cost&#x60; field displays the monthly cost of the app if it were to use the Basic tier. If the proposed app already uses the lest expensive tier, the field is empty. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


