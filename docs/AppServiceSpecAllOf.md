# AppServiceSpecAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cors** | [**AppsCorsPolicy**](AppsCorsPolicy.md) |  | [optional] 
**health_check** | [**AppServiceSpecHealthCheck**](AppServiceSpecHealthCheck.md) |  | [optional] 
**http_port** | **int** | The internal port on which this service&#39;s run command will listen. Default: 8080 If there is not an environment variable with the name &#x60;PORT&#x60;, one will be automatically added with its value set to the value of this field. | [optional] 
**internal_ports** | **[int]** | The ports on which this service will listen for internal traffic. | [optional] 
**routes** | [**[AppRouteSpec]**](AppRouteSpec.md) | A list of HTTP routes that should be routed to this component. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


