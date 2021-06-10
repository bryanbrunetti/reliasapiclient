# relias_api_client.AssessmentsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_assignable_assessments**](AssessmentsApi.md#get_user_assignable_assessments) | **GET** /v1/users/{username}/assignable-assessments | Retrieves a paginated list of assignable assessments for the user corresponding to the username provided


# **get_user_assignable_assessments**
> PaginatedListOfAssignableAssessmentModel get_user_assignable_assessments(username, page_number=page_number, page_size=page_size, org_id=org_id)

Retrieves a paginated list of assignable assessments for the user corresponding to the username provided

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.AssessmentsApi()
username = 'username_example' # str | the username of the user whose assignable assessments are wanted
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Retrieves a paginated list of assignable assessments for the user corresponding to the username provided
    api_response = api_instance.get_user_assignable_assessments(username, page_number=page_number, page_size=page_size, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssessmentsApi->get_user_assignable_assessments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user whose assignable assessments are wanted | 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**PaginatedListOfAssignableAssessmentModel**](PaginatedListOfAssignableAssessmentModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

