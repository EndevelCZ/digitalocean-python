# DropletMultiCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **[str]** | An array of human human-readable strings you wish to use when displaying the Droplet name. Each name, if set to a domain name managed in the DigitalOcean DNS management system, will configure a PTR record for the Droplet. Each name set during creation will also determine the hostname for the Droplet in its internal configuration. | 
**region** | **str** | The slug identifier for the region that you wish to deploy the Droplet in. | 
**size** | **str** | The slug identifier for the size that you wish to select for this Droplet. | 
**image** | **bool, date, datetime, dict, float, int, list, str, none_type** | The image ID of a public or private image or the slug identifier for a public image. This image will be the base image for your Droplet. | 
**ssh_keys** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | An array containing the IDs or fingerprints of the SSH keys that you wish to embed in the Droplet&#39;s root account upon creation. | [optional]  if omitted the server will use the default value of []
**backups** | **bool** | A boolean indicating whether automated backups should be enabled for the Droplet. | [optional]  if omitted the server will use the default value of False
**ipv6** | **bool** | A boolean indicating whether to enable IPv6 on the Droplet. | [optional]  if omitted the server will use the default value of False
**monitoring** | **bool** | A boolean indicating whether to install the DigitalOcean agent for monitoring. | [optional]  if omitted the server will use the default value of False
**tags** | **[str], none_type** | A flat array of tag names as strings to apply to the Droplet after it is created. Tag names can either be existing or new tags. | [optional]  if omitted the server will use the default value of []
**user_data** | **str** | A string containing &#39;user data&#39; which may be used to configure the Droplet on first boot, often a &#39;cloud-config&#39; file or Bash script. It must be plain text and may not exceed 64 KiB in size. | [optional] 
**private_networking** | **bool** | This parameter has been deprecated. Use &#x60;vpc_uuid&#x60; instead to specify a VPC network for the Droplet. If no &#x60;vpc_uuid&#x60; is provided, the Droplet will be placed in your account&#39;s default VPC for the region. | [optional]  if omitted the server will use the default value of False
**vpc_uuid** | **str** | A string specifying the UUID of the VPC to which the Droplet will be assigned. If excluded, the Droplet will be assigned to your account&#39;s default VPC for the region. | [optional] 
**with_droplet_agent** | **bool** | A boolean indicating whether to install the DigitalOcean agent used for providing access to the Droplet web console in the control panel. By default, the agent is installed on new Droplets but installation errors (i.e. OS not supported) are ignored. To prevent it from being installed, set to &#x60;false&#x60;. To make installation errors fatal, explicitly set it to &#x60;true&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


