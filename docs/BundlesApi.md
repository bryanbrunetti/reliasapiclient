# relias_api_client.BundlesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matching_bundles_by_profile**](BundlesApi.md#matching_bundles_by_profile) | **GET** /v1/users/{username}/matching-bundles-by-profile | Returns user&#39;s Matching Bundles by Profile


# **matching_bundles_by_profile**
> list[MatchingBundleResponse] matching_bundles_by_profile(username, org_id=org_id)

Returns user's Matching Bundles by Profile

MatchingBundleResponse:    Contains the List of Matching Bundle Profiles  <ul><li>BundleId is the ID for the Bundle.</li><li>Title is the Title for the Bundle.</li><li>Description is the Description for the Bundle.</li><li>MatchingProfiles is a List of MatchingProfileResponse.</li></ul>    MatchingProfileResponse:  <ul><li>Title is the Title for the Profile.</li><li>Description is the Description for the Profile.</li><li>DueDateInDaysAfterAssignment is the Number of Days after assignment for the Due Date.</li><li>Attributes is a list of Attributes, values are:    <ul><li>Locations.</li><li>JobTitles.</li><li>Hierarchies.</li><li>Departments.</li><li>UserTypes.</li></ul></li></ul>

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.BundlesApi()
username = 'username_example' # str | the username of the user
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Returns user's Matching Bundles by Profile
    api_response = api_instance.matching_bundles_by_profile(username, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundlesApi->matching_bundles_by_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user | 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**list[MatchingBundleResponse]**](MatchingBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

