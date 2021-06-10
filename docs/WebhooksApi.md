# relias_api_client.WebhooksApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_assignment_completed_webhook**](WebhooksApi.md#create_assignment_completed_webhook) | **POST** /v1/webhooks/assignment-completed | Creates the Assignment Completed Webhook with the supplied Callback URL and optional authentication information
[**delete_assignment_completed_webhook**](WebhooksApi.md#delete_assignment_completed_webhook) | **DELETE** /v1/webhooks/assignment-completed | Deletes the Assignment Completed Webhook
[**get_assignment_completed_webhook**](WebhooksApi.md#get_assignment_completed_webhook) | **GET** /v1/webhooks/assignment-completed | Retrieves the Assignment Completed Webhook
[**update_assignment_completed_webhook**](WebhooksApi.md#update_assignment_completed_webhook) | **PUT** /v1/webhooks/assignment-completed | Updates the Assignment Completed Webhook


# **create_assignment_completed_webhook**
> CreateAssignmentCompletedWebhookResponse create_assignment_completed_webhook(webhook_request=webhook_request, org_id=org_id)

Creates the Assignment Completed Webhook with the supplied Callback URL and optional authentication information

<p>    <b>Webhook Notes:</b>  </p>  <ul>    <li>Callback URL is required and must not exceed 2048 characters.</li>    <li>Username and Password are optional; however, both must be supplied if chosen.</li>    <li>Username must only contain alphanumeric characters when provided.</li>    <li>Username must not exceed 32 characters when provided.</li>    <li>Password must only contain alphanumeric characters when provided.</li>    <li>Password must not exceed 32 characters when provided.</li>  </ul>  <br />  <p>    <b>Callback URL Notes:</b>  </p>  <ul>    <li>Upon assignment completion, the provided Callback URL of the webhook will be called using a HTTP POST.</li>    <li>The Callback URL chosen will be based on the organization ID of the user who completed the assignment.</li>    <li>If username/password were provided, these will be implemented for the POST using Basic Authentication.</li>    <li>When using Basic Authentication, HTTPS should be used for the Callback URL and any redirect will remove the Authorization Header.</li>    <li>If a failure was to occur when communicating with the Callback URL, the POST will be reattempted up to 5 additional times before discarding the information regarding the assignment completion.</li>  </ul>  <br />  <p>    <b>Request Body for Assignment Completed Callback URL:</b>  </p>  <pre>              {                  \"sentOn\": \"2020-12-25T12:15:10.698154\",                  \"type\": \"assignment-completed\",                  \"webhookId\": 231,                  \"data\": {                      \"assignmentId\": 87,                      \"username\": \"murphy123\",                      \"completed\": \"2020-12-25T12:8:32.735701\",                      \"assessmentName\": \"CCU Exam A v4\",                      \"assessmentType\": \"Clinical\"                  }              }              </pre>  <ul>    <li>SentOn is a timestamp of when the call to the Callback URL is occurring.</li>    <li>Type is the name of the webhook call that is happening; for the Assignment Completed Webhook, this will be \"assignment-completed\".</li>    <li>Webhook ID is the ID of the Webhook that is returned after creation.</li>    <li>Data is information specific to the type of webhook call that is occurring. In this scenario, the Assignment Completed Webhook returns a subset of assignment related information that may be used at other endpoints to retrieve more.</li>  </ul>

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.WebhooksApi()
webhook_request = relias_api_client.CreateAssignmentCompletedWebhookRequest() # CreateAssignmentCompletedWebhookRequest | the information for the webhook (optional)
org_id = 56 # int | organization ID for the webhook (defaults to current organization ID) (optional)

try:
    # Creates the Assignment Completed Webhook with the supplied Callback URL and optional authentication information
    api_response = api_instance.create_assignment_completed_webhook(webhook_request=webhook_request, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->create_assignment_completed_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_request** | [**CreateAssignmentCompletedWebhookRequest**](CreateAssignmentCompletedWebhookRequest.md)| the information for the webhook | [optional] 
 **org_id** | **int**| organization ID for the webhook (defaults to current organization ID) | [optional] 

### Return type

[**CreateAssignmentCompletedWebhookResponse**](CreateAssignmentCompletedWebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assignment_completed_webhook**
> delete_assignment_completed_webhook(org_id=org_id)

Deletes the Assignment Completed Webhook

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.WebhooksApi()
org_id = 56 # int | organization ID for the webhook (defaults to current organization ID) (optional)

try:
    # Deletes the Assignment Completed Webhook
    api_instance.delete_assignment_completed_webhook(org_id=org_id)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_assignment_completed_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| organization ID for the webhook (defaults to current organization ID) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assignment_completed_webhook**
> GetAssignmentCompletedWebhookResponse get_assignment_completed_webhook(org_id=org_id)

Retrieves the Assignment Completed Webhook

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.WebhooksApi()
org_id = 56 # int | organization ID for the webhook (defaults to current organization ID) (optional)

try:
    # Retrieves the Assignment Completed Webhook
    api_response = api_instance.get_assignment_completed_webhook(org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_assignment_completed_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| organization ID for the webhook (defaults to current organization ID) | [optional] 

### Return type

[**GetAssignmentCompletedWebhookResponse**](GetAssignmentCompletedWebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assignment_completed_webhook**
> update_assignment_completed_webhook(webhook_request=webhook_request, org_id=org_id)

Updates the Assignment Completed Webhook

<p>    <b>Webhook Notes:</b>  </p>  <ul>    <li>Callback URL is required and must not exceed 2048 characters.</li>    <li>Username and Password are optional; however, both must be supplied if chosen.</li>    <li>Username must not exceed 32 characters when provided.</li>    <li>Password must not exceed 64 characters when provided.</li>  </ul>

### Example
```python
from __future__ import print_function
import time
import relias_api_client
from relias_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = relias_api_client.WebhooksApi()
webhook_request = relias_api_client.UpdateAssignmentCompletedWebhookRequest() # UpdateAssignmentCompletedWebhookRequest | the information for the webhook (optional)
org_id = 56 # int | organization ID for the webhook (defaults to current organization ID) (optional)

try:
    # Updates the Assignment Completed Webhook
    api_instance.update_assignment_completed_webhook(webhook_request=webhook_request, org_id=org_id)
except ApiException as e:
    print("Exception when calling WebhooksApi->update_assignment_completed_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_request** | [**UpdateAssignmentCompletedWebhookRequest**](UpdateAssignmentCompletedWebhookRequest.md)| the information for the webhook | [optional] 
 **org_id** | **int**| organization ID for the webhook (defaults to current organization ID) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

