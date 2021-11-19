# LoadBalancerCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID that can be used to identify and reference a load balancer. | [optional] [readonly] 
**name** | **str** | A human-readable name for a load balancer instance. | [optional] 
**ip** | **str** | An attribute containing the public-facing IP address of the load balancer. | [optional] [readonly] 
**size_unit** | **int** | How many nodes the load balancer contains. Each additional node increases the load balancer&#39;s ability to manage more connections. Load balancers can be scaled up or down, and you can change the number of nodes after creation up to once per hour. This field is currently not available in the AMS2, NYC2, or SFO1 regions. Use the &#x60;size&#x60; field to scale load balancers that reside in these regions. | [optional]  if omitted the server will use the default value of 1
**size** | **str** | This field has been replaced by the &#x60;size_unit&#x60; field for all regions except in AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load balancer having a set number of nodes. * &#x60;lb-small&#x60; &#x3D; 1 node * &#x60;lb-medium&#x60; &#x3D; 3 nodes * &#x60;lb-large&#x60; &#x3D; 6 nodes  You can resize load balancers after creation up to once per hour. You cannot resize a load balancer within the first hour of its creation. | [optional]  if omitted the server will use the default value of "lb-small"
**algorithm** | **str** | This field has been deprecated. You can no longer specify an algorithm for load balancers. | [optional]  if omitted the server will use the default value of "round_robin"
**status** | **str** | A status string indicating the current state of the load balancer. This can be &#x60;new&#x60;, &#x60;active&#x60;, or &#x60;errored&#x60;. | [optional] [readonly] 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the load balancer was created. | [optional] [readonly] 
**health_check** | [**HealthCheck**](HealthCheck.md) |  | [optional] 
**sticky_sessions** | [**StickySessions**](StickySessions.md) |  | [optional] 
**redirect_http_to_https** | **bool** | A boolean value indicating whether HTTP requests to the load balancer on port 80 will be redirected to HTTPS on port 443. | [optional]  if omitted the server will use the default value of False
**enable_proxy_protocol** | **bool** | A boolean value indicating whether PROXY Protocol is in use. | [optional]  if omitted the server will use the default value of False
**enable_backend_keepalive** | **bool** | A boolean value indicating whether HTTP keepalive connections are maintained to target Droplets. | [optional]  if omitted the server will use the default value of False
**vpc_uuid** | **str** | A string specifying the UUID of the VPC to which the load balancer is assigned. | [optional] 
**disable_lets_encrypt_dns_records** | **bool** | A boolean value indicating whether to disable automatic DNS record creation for Let&#39;s Encrypt certificates that are added to the load balancer. | [optional]  if omitted the server will use the default value of False
**droplet_ids** | **[int]** | An array containing the IDs of the Droplets assigned to the load balancer. | [optional] 
**region** | [**RegionSlug**](RegionSlug.md) |  | [optional] 
**forwarding_rules** | [**[ForwardingRule]**](ForwardingRule.md) | An array of objects specifying the forwarding rules for a load balancer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


