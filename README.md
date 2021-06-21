# ReliasAPIClient


## Requirements.

Python 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/bryanbrunetti/reliasapiclient.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/bryanbrunetti/reliasapiclient.git`)

Then import the package:
```python
import relias_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import relias_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import relias_api_client

# Create an instance of the Assignment API class
api_instance = relias_api_client.AssignmentsApi()
username = 'atravelnurse@nomadhealth.com' # str | The username (email) of the applicant.
# Get a list of assignable assessments for a user:
assessments = api_instance.get_user_assignments(username)

# Create an assessment for a user:
assignments = relias_api_client.CreateAssignmentRequest(assessment_ids=[1449], expiration=todays_date)
api_instance.create_assignments_for_user(username, assignments)
# [{"assignmentId":3800327,"userId":18461195,"expiration":"2021-06-21T23:59:59","assessmentId":1449}]'
```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicantsApi* | [**convert_to_learner**](docs/ApplicantsApi.md#convert_to_learner) | **POST** /v1/applicants/{username}/convert | Converts an applicant based on the username provided to a learner with the new username supplied
*ApplicantsApi* | [**create_applicant**](docs/ApplicantsApi.md#create_applicant) | **POST** /v1/applicants | Creates an applicant with the supplied information
*ApplicantsApi* | [**get_applicant**](docs/ApplicantsApi.md#get_applicant) | **GET** /v1/applicants/{username} | Retrieves an applicant based on the username provided
*ApplicantsApi* | [**update_applicant**](docs/ApplicantsApi.md#update_applicant) | **PATCH** /v1/applicants/{username} | Update an applicant using JSON patch documents.
*AssessmentsApi* | [**get_user_assignable_assessments**](docs/AssessmentsApi.md#get_user_assignable_assessments) | **GET** /v1/users/{username}/assignable-assessments | Retrieves a paginated list of assignable assessments for the user corresponding to the username provided
*AssignmentsApi* | [**create_assignments_for_user**](docs/AssignmentsApi.md#create_assignments_for_user) | **POST** /v1/users/{username}/assignments | Assigns multiple assessments to one user
*AssignmentsApi* | [**get_user_assignments**](docs/AssignmentsApi.md#get_user_assignments) | **GET** /v1/users/{username}/assignments | Retrieves a paginated list of assignments for the provided username
*AssignmentsApi* | [**get_users_behavioral_assignment**](docs/AssignmentsApi.md#get_users_behavioral_assignment) | **GET** /v1/users/{username}/behavioral-assignments/{assignmentId} | Retrieves behavioral assignment results for a provided username and assignment ID
*AssignmentsApi* | [**get_users_behavioral_assignment_result_pdf**](docs/AssignmentsApi.md#get_users_behavioral_assignment_result_pdf) | **GET** /v1/users/{username}/behavioral-assignments/{assignmentId}/results | Retrieves a behavioral assignment results pdf for a provided username and assignment ID
*AssignmentsApi* | [**get_users_clinical_assignment**](docs/AssignmentsApi.md#get_users_clinical_assignment) | **GET** /v1/users/{username}/clinical-assignments/{assignmentId} | Retrieves clinical assignment results for a provided username and assignment ID
*AssignmentsApi* | [**get_users_clinical_assignment_result_pdf**](docs/AssignmentsApi.md#get_users_clinical_assignment_result_pdf) | **GET** /v1/users/{username}/clinical-assignments/{assignmentId}/results | Retrieves a clinical assignment results pdf for a provided username and assignment ID
*AssignmentsApi* | [**get_users_self_assignment**](docs/AssignmentsApi.md#get_users_self_assignment) | **GET** /v1/users/{username}/self-assignments/{assignmentId} | Retrieves self assignment results for a provided username and assignment ID
*AssignmentsApi* | [**get_users_self_assignment_result_pdf**](docs/AssignmentsApi.md#get_users_self_assignment_result_pdf) | **GET** /v1/users/{username}/self-assignments/{assignmentId}/results | Retrieves a self assignment results pdf for a provided username and assignment ID
*AssignmentsApi* | [**get_users_situational_assignment**](docs/AssignmentsApi.md#get_users_situational_assignment) | **GET** /v1/users/{username}/situational-assignments/{assignmentId} | Retrieves a situational assignment results for a provided username and assignment ID
*AssignmentsApi* | [**get_users_situational_assignment_result_pdf**](docs/AssignmentsApi.md#get_users_situational_assignment_result_pdf) | **GET** /v1/users/{username}/situational-assignments/{assignmentId}/results | Retrieves a situational assignment results pdf for a provided username and assignment ID
*AuthenticationApi* | [**authenticate**](docs/AuthenticationApi.md#authenticate) | **POST** /v1/authenticate | Get an authentication token.
*BundleAssignmentsApi* | [**create_bundle_assignments_for_user**](docs/BundleAssignmentsApi.md#create_bundle_assignments_for_user) | **POST** /v1/users/{username}/bundle-assignments | Assigns one or multiple bundles to one user
*BundlesApi* | [**matching_bundles_by_profile**](docs/BundlesApi.md#matching_bundles_by_profile) | **GET** /v1/users/{username}/matching-bundles-by-profile | Returns user&#39;s Matching Bundles by Profile
*DepartmentsApi* | [**get_departments**](docs/DepartmentsApi.md#get_departments) | **GET** /v1/departments | Retrieves a paginated list of departments for the current user&#39;s organization or provided org ID
*HierarchiesApi* | [**get_hierarchies**](docs/HierarchiesApi.md#get_hierarchies) | **GET** /v1/hierarchies | Retrieves a list of hierarchies for the current user&#39;s organization or provided org ID
*JobTitlesApi* | [**get_job_titles**](docs/JobTitlesApi.md#get_job_titles) | **GET** /v1/job-titles | Retrieves a paginated list of job titles for the current user&#39;s organization or provided org ID
*LocationsApi* | [**get_locations**](docs/LocationsApi.md#get_locations) | **GET** /v1/locations | Retrieves a paginated list of locations for the current user&#39;s organization or provided org ID
*ScorecardsApi* | [**get_users_scorecard_result_pdf**](docs/ScorecardsApi.md#get_users_scorecard_result_pdf) | **GET** /v1/users/{username}/scorecards/{scorecardId}/results | Retrieves a scorecard results pdf for a provided username and scorecard ID
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /v1/users | Creates a user with the supplied information
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /v1/users/{username} | Retrieves a user based on the username provided
*UsersApi* | [**update_user**](docs/UsersApi.md#update_user) | **PATCH** /v1/users/{username} | Update a user using JSON patch documents.
*WebhooksApi* | [**create_assignment_completed_webhook**](docs/WebhooksApi.md#create_assignment_completed_webhook) | **POST** /v1/webhooks/assignment-completed | Creates the Assignment Completed Webhook with the supplied Callback URL and optional authentication information
*WebhooksApi* | [**delete_assignment_completed_webhook**](docs/WebhooksApi.md#delete_assignment_completed_webhook) | **DELETE** /v1/webhooks/assignment-completed | Deletes the Assignment Completed Webhook
*WebhooksApi* | [**get_assignment_completed_webhook**](docs/WebhooksApi.md#get_assignment_completed_webhook) | **GET** /v1/webhooks/assignment-completed | Retrieves the Assignment Completed Webhook
*WebhooksApi* | [**update_assignment_completed_webhook**](docs/WebhooksApi.md#update_assignment_completed_webhook) | **PUT** /v1/webhooks/assignment-completed | Updates the Assignment Completed Webhook


## Documentation For Models

 - [AssignableAssessmentModel](docs/AssignableAssessmentModel.md)
 - [AssignmentAssessmentModel](docs/AssignmentAssessmentModel.md)
 - [AssignmentModel](docs/AssignmentModel.md)
 - [AuthenticateRequest](docs/AuthenticateRequest.md)
 - [AuthenticateResponse](docs/AuthenticateResponse.md)
 - [BehavioralResult](docs/BehavioralResult.md)
 - [ClinicalResult](docs/ClinicalResult.md)
 - [ConvertToLearnerRequest](docs/ConvertToLearnerRequest.md)
 - [CreateApplicantRequest](docs/CreateApplicantRequest.md)
 - [CreateApplicantResponse](docs/CreateApplicantResponse.md)
 - [CreateAssignmentCompletedWebhookRequest](docs/CreateAssignmentCompletedWebhookRequest.md)
 - [CreateAssignmentCompletedWebhookResponse](docs/CreateAssignmentCompletedWebhookResponse.md)
 - [CreateAssignmentRequest](docs/CreateAssignmentRequest.md)
 - [CreateAssignmentResponse](docs/CreateAssignmentResponse.md)
 - [CreateBundleAssignmentRequest](docs/CreateBundleAssignmentRequest.md)
 - [CreateBundleAssignmentResponse](docs/CreateBundleAssignmentResponse.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [CreateUserResponse](docs/CreateUserResponse.md)
 - [DepartmentModel](docs/DepartmentModel.md)
 - [EntityTagHeaderValue](docs/EntityTagHeaderValue.md)
 - [FileStreamResult](docs/FileStreamResult.md)
 - [GetApplicantModel](docs/GetApplicantModel.md)
 - [GetAssignmentCompletedWebhookResponse](docs/GetAssignmentCompletedWebhookResponse.md)
 - [GetUserModel](docs/GetUserModel.md)
 - [HierarchyModel](docs/HierarchyModel.md)
 - [JobTitleModel](docs/JobTitleModel.md)
 - [LocationModel](docs/LocationModel.md)
 - [MatchingBundleResponse](docs/MatchingBundleResponse.md)
 - [MatchingProfileResponse](docs/MatchingProfileResponse.md)
 - [Operation](docs/Operation.md)
 - [PaginatedListOfAssignableAssessmentModel](docs/PaginatedListOfAssignableAssessmentModel.md)
 - [PaginatedListOfAssignmentModel](docs/PaginatedListOfAssignmentModel.md)
 - [PaginatedListOfDepartmentModel](docs/PaginatedListOfDepartmentModel.md)
 - [PaginatedListOfJobTitleModel](docs/PaginatedListOfJobTitleModel.md)
 - [PaginatedListOfLocationModel](docs/PaginatedListOfLocationModel.md)
 - [PreviousAndNextLinks](docs/PreviousAndNextLinks.md)
 - [SelfResult](docs/SelfResult.md)
 - [SituationalResult](docs/SituationalResult.md)
 - [StatusCodeDetails](docs/StatusCodeDetails.md)
 - [Stream](docs/Stream.md)
 - [StringSegment](docs/StringSegment.md)
 - [UpdateAssignmentCompletedWebhookRequest](docs/UpdateAssignmentCompletedWebhookRequest.md)
