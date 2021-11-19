# Account


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**droplet_limit** | **int** | The total number of Droplets current user or team may have active at one time. | 
**floating_ip_limit** | **int** | The total number of Floating IPs the current user or team may have. | 
**email** | **str** | The email address used by the current user to register for DigitalOcean. | 
**uuid** | **str** | The unique universal identifier for the current user. | 
**status_message** | **str** | A human-readable message giving more details about the status of the account. | 
**email_verified** | **bool** | If true, the user has verified their account via email. False otherwise. | defaults to False
**status** | **str** | This value is one of \&quot;active\&quot;, \&quot;warning\&quot; or \&quot;locked\&quot;. | defaults to "active"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


