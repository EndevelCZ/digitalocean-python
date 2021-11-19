# CdnEndpoint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | **str** | The fully qualified domain name (FQDN) for the origin server which provides the content for the CDN. This is currently restricted to a Space. | 
**id** | **str** | A unique ID that can be used to identify and reference a CDN endpoint. | [optional] [readonly] 
**endpoint** | **str** | The fully qualified domain name (FQDN) from which the CDN-backed content is served. | [optional] [readonly] 
**ttl** | **int** | The amount of time the content is cached by the CDN&#39;s edge servers in seconds. TTL must be one of 60, 600, 3600, 86400, or 604800. Defaults to 3600 (one hour) when excluded. | [optional]  if omitted the server will use the default value of 3600
**certificate_id** | **str** | The ID of a DigitalOcean managed TLS certificate used for SSL when a custom subdomain is provided. | [optional] 
**custom_domain** | **str** | The fully qualified domain name (FQDN) of the custom subdomain used with the CDN endpoint. | [optional] 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the CDN endpoint was created. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


