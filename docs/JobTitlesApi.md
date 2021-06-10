# relias_api_client.JobTitlesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_titles**](JobTitlesApi.md#get_job_titles) | **GET** /v1/job-titles | Retrieves a paginated list of job titles for the current user&#39;s organization or provided org ID


# **get_job_titles**
> PaginatedListOfJobTitleModel get_job_titles(org_id=org_id, page_number=page_number, page_size=page_size)

Retrieves a paginated list of job titles for the current user's organization or provided org ID

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.JobTitlesApi()
org_id = 56 # int |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Retrieves a paginated list of job titles for the current user's organization or provided org ID
    api_response = api_instance.get_job_titles(org_id=org_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTitlesApi->get_job_titles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**PaginatedListOfJobTitleModel**](PaginatedListOfJobTitleModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

