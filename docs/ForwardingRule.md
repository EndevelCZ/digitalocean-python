# ForwardingRule

An object specifying a forwarding rule for a load balancer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_protocol** | **str** | The protocol used for traffic to the load balancer. The possible values are: &#x60;http&#x60;, &#x60;https&#x60;, &#x60;http2&#x60;, or &#x60;tcp&#x60;.  | 
**entry_port** | **int** | An integer representing the port on which the load balancer instance will listen. | 
**target_protocol** | **str** | The protocol used for traffic from the load balancer to the backend Droplets. The possible values are: &#x60;http&#x60;, &#x60;https&#x60;, &#x60;http2&#x60;, or &#x60;tcp&#x60;.  | 
**target_port** | **int** | An integer representing the port on the backend Droplets to which the load balancer will send traffic. | 
**certificate_id** | **str** | The ID of the TLS certificate used for SSL termination if enabled. | [optional] 
**tls_passthrough** | **bool** | A boolean value indicating whether SSL encrypted traffic will be passed through to the backend Droplets. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


