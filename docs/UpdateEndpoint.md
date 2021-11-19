# UpdateEndpoint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **int** | The amount of time the content is cached by the CDN&#39;s edge servers in seconds. TTL must be one of 60, 600, 3600, 86400, or 604800. Defaults to 3600 (one hour) when excluded. | [optional]  if omitted the server will use the default value of 3600
**certificate_id** | **str** | The ID of a DigitalOcean managed TLS certificate used for SSL when a custom subdomain is provided. | [optional] 
**custom_domain** | **str** | The fully qualified domain name (FQDN) of the custom subdomain used with the CDN endpoint. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


