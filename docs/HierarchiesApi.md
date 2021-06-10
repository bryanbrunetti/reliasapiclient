# relias_api_client.HierarchiesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hierarchies**](HierarchiesApi.md#get_hierarchies) | **GET** /v1/hierarchies | Retrieves a list of hierarchies for the current user&#39;s organization or provided org ID


# **get_hierarchies**
> list[HierarchyModel] get_hierarchies(org_id=org_id)

Retrieves a list of hierarchies for the current user's organization or provided org ID

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.HierarchiesApi()
org_id = 56 # int |  (optional)

try:
    # Retrieves a list of hierarchies for the current user's organization or provided org ID
    api_response = api_instance.get_hierarchies(org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HierarchiesApi->get_hierarchies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | [optional] 

### Return type

[**list[HierarchyModel]**](HierarchyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

