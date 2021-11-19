# Cluster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-readable name for a Kubernetes cluster. | 
**region** | **str** | The slug identifier for the region where the Kubernetes cluster is located. | 
**version** | **str** | The slug identifier for the version of Kubernetes used for the cluster. If set to a minor version (e.g. \&quot;1.14\&quot;), the latest version within it will be used (e.g. \&quot;1.14.6-do.1\&quot;); if set to \&quot;latest\&quot;, the latest published version will be used. See the &#x60;/v2/kubernetes/options&#x60; endpoint to find all currently available versions. | 
**node_pools** | [**[KubernetesNodePool]**](KubernetesNodePool.md) | An object specifying the details of the worker nodes available to the Kubernetes cluster. | 
**id** | **str** | A unique ID that can be used to identify and reference a Kubernetes cluster. | [optional] [readonly] 
**cluster_subnet** | **str** | The range of IP addresses in the overlay network of the Kubernetes cluster in CIDR notation. | [optional] [readonly] 
**service_subnet** | **str** | The range of assignable IP addresses for services running in the Kubernetes cluster in CIDR notation. | [optional] [readonly] 
**vpc_uuid** | **str** | A string specifying the UUID of the VPC to which the Kubernetes cluster is assigned. | [optional] 
**ipv4** | **str** | The public IPv4 address of the Kubernetes master node. This will not be set if high availability is configured on the cluster (v1.21+) | [optional] [readonly] 
**endpoint** | **str** | The base URL of the API server on the Kubernetes master node. | [optional] [readonly] 
**tags** | **[str]** | An array of tags applied to the Kubernetes cluster. All clusters are automatically tagged &#x60;k8s&#x60; and &#x60;k8s:$K8S_CLUSTER_ID&#x60;. | [optional] 
**maintenance_policy** | [**MaintenancePolicy**](MaintenancePolicy.md) |  | [optional] 
**auto_upgrade** | **bool** | A boolean value indicating whether the cluster will be automatically upgraded to new patch releases during its maintenance window. | [optional]  if omitted the server will use the default value of False
**status** | [**ClusterStatus**](ClusterStatus.md) |  | [optional] 
**created_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the Kubernetes cluster was created. | [optional] [readonly] 
**updated_at** | **datetime** | A time value given in ISO8601 combined date and time format that represents when the Kubernetes cluster was last updated. | [optional] [readonly] 
**surge_upgrade** | **bool** | A boolean value indicating whether surge upgrade is enabled/disabled for the cluster. Surge upgrade makes cluster upgrades fast and reliable by bringing up new nodes before destroying the outdated nodes. | [optional]  if omitted the server will use the default value of False
**ha** | **bool** | A boolean value indicating whether the control plane is run in a highly available configuration in the cluster. Highly available control planes incur less downtime. | [optional]  if omitted the server will use the default value of False
**registry_enabled** | **bool** | A read-only boolean value indicating if a container registry is integrated with the cluster. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


