# relias_api_client.BundleAssignmentsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bundle_assignments_for_user**](BundleAssignmentsApi.md#create_bundle_assignments_for_user) | **POST** /v1/users/{username}/bundle-assignments | Assigns one or multiple bundles to one user


# **create_bundle_assignments_for_user**
> list[CreateBundleAssignmentResponse] create_bundle_assignments_for_user(username, bundle_assignment_request, org_id=org_id)

Assigns one or multiple bundles to one user

Notes:                Create Bundle Assignment Request:  <ul><li>BundleIds is a required list of bundle IDS and the organization should have access to them.</li><li>Expiration is the expiration date for the Bundle Assignment. Time is always set to 11:59pm.</li><li>Availability is the date the bundle is available to the user.</li><li>Locked, if true, indicates that the user cannot take the bundled content until it is manually unlocked. Availability should be null when Locked is true.</li></ul>                Create Bundle Assignment Response:  <ul><li>BundleAssignmentId is the ID for the Bundle Assignment.</li><li>UserId is the ID of the User in the Assignment.</li><li>Expiration is the expiration date for the Bundle Assignment.</li><li>BundleId is the ID of the assigned bundles.</li></ul>

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.BundleAssignmentsApi()
username = 'username_example' # str | the username of the user receiving the Bundle Assignment
bundle_assignment_request = relias_api_client.CreateBundleAssignmentRequest() # CreateBundleAssignmentRequest | The assignment information
org_id = 56 # int | Organization ID of the user (defaults to current organization ID) (optional)

try:
    # Assigns one or multiple bundles to one user
    api_response = api_instance.create_bundle_assignments_for_user(username, bundle_assignment_request, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleAssignmentsApi->create_bundle_assignments_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user receiving the Bundle Assignment | 
 **bundle_assignment_request** | [**CreateBundleAssignmentRequest**](CreateBundleAssignmentRequest.md)| The assignment information | 
 **org_id** | **int**| Organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**list[CreateBundleAssignmentResponse]**](CreateBundleAssignmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

