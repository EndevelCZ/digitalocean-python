# AppServiceSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. Must be unique across all components within the same app. | 
**git** | [**AppsGitSourceSpec**](AppsGitSourceSpec.md) |  | [optional] 
**github** | [**AppsGithubSourceSpec**](AppsGithubSourceSpec.md) |  | [optional] 
**gitlab** | [**AppsGitlabSourceSpec**](AppsGitlabSourceSpec.md) |  | [optional] 
**image** | [**AppsImageSourceSpec**](AppsImageSourceSpec.md) |  | [optional] 
**dockerfile_path** | **str** | The path to the Dockerfile relative to the root of the repo. If set, it will be used to build this component. Otherwise, App Platform will attempt to build it using buildpacks. | [optional] 
**build_command** | **str** | An optional build command to run while building this component from source. | [optional] 
**run_command** | **str** | An optional run command to override the component&#39;s default. | [optional] 
**source_dir** | **str** | An optional path to the working directory to use for the build. For Dockerfile builds, this will be used as the build context. Must be relative to the root of the repo. | [optional] 
**envs** | [**[AppVariableDefinition]**](AppVariableDefinition.md) | A list of environment variables made available to the component. | [optional] 
**environment_slug** | **str** | An environment slug describing the type of this app. For a full list, please refer to [the product documentation](https://www.digitalocean.com/docs/app-platform/). | [optional] 
**instance_count** | **int** | The amount of instances that this component should be scaled to. Default: 1 | [optional]  if omitted the server will use the default value of 1
**instance_size_slug** | **str** | The instance size to use for this component. Default: &#x60;basic-xxs&#x60; | [optional]  if omitted the server will use the default value of "basic-xxs"
**cors** | [**AppsCorsPolicy**](AppsCorsPolicy.md) |  | [optional] 
**health_check** | [**AppServiceSpecHealthCheck**](AppServiceSpecHealthCheck.md) |  | [optional] 
**http_port** | **int** | The internal port on which this service&#39;s run command will listen. Default: 8080 If there is not an environment variable with the name &#x60;PORT&#x60;, one will be automatically added with its value set to the value of this field. | [optional] 
**internal_ports** | **[int]** | The ports on which this service will listen for internal traffic. | [optional] 
**routes** | [**[AppRouteSpec]**](AppRouteSpec.md) | A list of HTTP routes that should be routed to this component. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


