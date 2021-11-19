# AppsCorsPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_origins** | [**[AppsStringMatch]**](AppsStringMatch.md) | The set of allowed CORS origins. | [optional] 
**allow_methods** | **[str]** | The set of allowed HTTP methods. This configures the &#x60;Access-Control-Allow-Methods&#x60; header. | [optional] 
**allow_headers** | **[str]** | The set of allowed HTTP request headers. This configures the &#x60;Access-Control-Allow-Headers&#x60; header. | [optional] 
**expose_headers** | **[str]** | The set of HTTP response headers that browsers are allowed to access. This configures the &#x60;Access-Control-Expose-Headers&#x60; header. | [optional] 
**max_age** | **str** | An optional duration specifying how long browsers can cache the results of a preflight request. This configures the &#x60;Access-Control-Max-Age&#x60; header. | [optional] 
**allow_credentials** | **bool** | Whether browsers should expose the response to the client-side JavaScript code when the request’s credentials mode is include. This configures the &#x60;Access-Control-Allow-Credentials&#x60; header. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


