# AppStaticSiteSpec


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
**index_document** | **str** | The name of the index document to use when serving this static site. Default: index.html | [optional]  if omitted the server will use the default value of "index.html"
**error_document** | **str** | The name of the error document to use when serving this static site. Default: 404.html. If no such file exists within the built assets, App Platform will supply one. | [optional]  if omitted the server will use the default value of "404.html"
**catchall_document** | **str** | The name of the document to use as the fallback for any requests to documents that are not found when serving this static site. Only 1 of &#x60;catchall_document&#x60; or &#x60;error_document&#x60; can be set. | [optional] 
**output_dir** | **str** | An optional path to where the built assets will be located, relative to the build context. If not set, App Platform will automatically scan for these directory names: &#x60;_static&#x60;, &#x60;dist&#x60;, &#x60;public&#x60;, &#x60;build&#x60;. | [optional] 
**cors** | [**AppsCorsPolicy**](AppsCorsPolicy.md) |  | [optional] 
**routes** | [**[AppRouteSpec]**](AppRouteSpec.md) | A list of HTTP routes that should be routed to this component. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


