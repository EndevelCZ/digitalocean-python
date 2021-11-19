# AppDomainSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The hostname for the domain | 
**type** | **str** | - DEFAULT: The default &#x60;.ondigitalocean.app&#x60; domain assigned to this app - PRIMARY: The primary domain for this app that is displayed as the default in the control panel, used in bindable environment variables, and any other places that reference an app&#39;s live URL. Only one domain may be set as primary. - ALIAS: A non-primary domain | [optional]  if omitted the server will use the default value of "UNSPECIFIED"
**wildcard** | **bool** | Indicates whether the domain includes all sub-domains, in addition to the given domain | [optional] 
**zone** | **str** | Optional. If the domain uses DigitalOcean DNS and you would like App Platform to automatically manage it for you, set this to the name of the domain on your account.  For example, If the domain you are adding is &#x60;app.domain.com&#x60;, the zone could be &#x60;domain.com&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


