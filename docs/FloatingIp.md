# FloatingIp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | The public IP address of the floating IP. It also serves as its identifier. | [optional] 
**region** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**droplet** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Droplet that the floating IP has been assigned to. When you query a floating IP, if it is assigned to a Droplet, the entire Droplet object will be returned. If it is not assigned, the value will be null. | [optional] 
**locked** | **bool** | A boolean value indicating whether or not the floating IP has pending actions preventing new ones from being submitted. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


