# Tag

A tag is a label that can be applied to a resource (currently Droplets, Images, Volumes, Volume Snapshots, and Database clusters) in order to better organize or facilitate the lookups and actions on it. Tags have two attributes: a user defined `name` attribute and an embedded `resources` attribute with information about resources that have been tagged.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the tag. Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag.  **Note:** Tag names are case stable, which means the capitalization you use when you first create a tag is canonical.  When working with tags in the API, you must use the tag&#39;s canonical capitalization. For example, if you create a tag named \&quot;PROD\&quot;, the URL to add that tag to a resource would be &#x60;https://api.digitalocean.com/v2/tags/PROD/resources&#x60; (not &#x60;/v2/tags/prod/resources&#x60;).  Tagged resources in the control panel will always display the canonical capitalization. For example, if you create a tag named \&quot;PROD\&quot;, you can tag resources in the control panel by entering \&quot;prod\&quot;. The tag will still display with its canonical capitalization, \&quot;PROD\&quot;.  | [optional] 
**resources** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | An embedded object containing key value pairs of resource type and resource statistics. It also includes a count of the total number of resources tagged with the current tag as well as a &#x60;last_tagged_uri&#x60; attribute set to the last resource tagged with the current tag. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


