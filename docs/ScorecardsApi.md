# relias_api_client.ScorecardsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_users_scorecard_result_pdf**](ScorecardsApi.md#get_users_scorecard_result_pdf) | **GET** /v1/users/{username}/scorecards/{scorecardId}/results | Retrieves a scorecard results pdf for a provided username and scorecard ID


# **get_users_scorecard_result_pdf**
> FileStreamResult get_users_scorecard_result_pdf(username, scorecard_id, org_id=org_id)

Retrieves a scorecard results pdf for a provided username and scorecard ID

When providing username, be sure to URL encode the value if it contains any special characters.

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.ScorecardsApi()
username = 'username_example' # str | the username of the user whose scorecard is wanted
scorecard_id = 56 # int | the ID of the scorecard
org_id = 56 # int | organization ID of the user (defaults to current organization ID) (optional)

try:
    # Retrieves a scorecard results pdf for a provided username and scorecard ID
    api_response = api_instance.get_users_scorecard_result_pdf(username, scorecard_id, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScorecardsApi->get_users_scorecard_result_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username of the user whose scorecard is wanted | 
 **scorecard_id** | **int**| the ID of the scorecard | 
 **org_id** | **int**| organization ID of the user (defaults to current organization ID) | [optional] 

### Return type

[**FileStreamResult**](FileStreamResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

