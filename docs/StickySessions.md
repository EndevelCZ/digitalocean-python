# StickySessions

An object specifying sticky sessions settings for the load balancer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | An attribute indicating how and if requests from a client will be persistently served by the same backend Droplet. The possible values are &#x60;cookies&#x60; or &#x60;none&#x60;. | [optional]  if omitted the server will use the default value of "none"
**cookie_name** | **str** | The name of the cookie sent to the client. This attribute is only returned when using &#x60;cookies&#x60; for the sticky sessions type. | [optional] 
**cookie_ttl_seconds** | **int** | The number of seconds until the cookie set by the load balancer expires. This attribute is only returned when using &#x60;cookies&#x60; for the sticky sessions type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


