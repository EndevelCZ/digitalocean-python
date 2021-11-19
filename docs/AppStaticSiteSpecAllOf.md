# AppStaticSiteSpecAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_document** | **str** | The name of the index document to use when serving this static site. Default: index.html | [optional]  if omitted the server will use the default value of "index.html"
**error_document** | **str** | The name of the error document to use when serving this static site. Default: 404.html. If no such file exists within the built assets, App Platform will supply one. | [optional]  if omitted the server will use the default value of "404.html"
**catchall_document** | **str** | The name of the document to use as the fallback for any requests to documents that are not found when serving this static site. Only 1 of &#x60;catchall_document&#x60; or &#x60;error_document&#x60; can be set. | [optional] 
**output_dir** | **str** | An optional path to where the built assets will be located, relative to the build context. If not set, App Platform will automatically scan for these directory names: &#x60;_static&#x60;, &#x60;dist&#x60;, &#x60;public&#x60;, &#x60;build&#x60;. | [optional] 
**cors** | [**AppsCorsPolicy**](AppsCorsPolicy.md) |  | [optional] 
**routes** | [**[AppRouteSpec]**](AppRouteSpec.md) | A list of HTTP routes that should be routed to this component. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


