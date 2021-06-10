# coding: utf-8

"""
    Relias API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from relias_api_client.api_client import ApiClient


class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_user(self, user_information, **kwargs):  # noqa: E501
        """Creates a user with the supplied information  # noqa: E501

        Notes:  <ul><li>Org ID is required and should be the ID of your organization.</li><li>First Name is required and must not exceed 50 characters.</li><li>Last Name is required and must not exceed 50 characters.</li><li>Username is required, must be unique within your organization and not exceed 255 characters.</li><li>Email is required when supplying User Roles other than learner and must not exceed 150 characters.</li><li>Password is required and must be at minimum 4 characters long.</li><li>Job Titles, Departments, Location and Hierarchy ID are optional.</li><li>Learner ID, optional, must be unique within your organization and not exceed 50 characters.</li><li>GUID, optional, must be unique within your organization and not exceed 50 characters.</li><li>User Roles are optional but may be supplied to provide additional roles beyond learner.<br />          Options Include:          <ul><li>Administrator</li><li>Report Supervisor</li><li>Enrollment Supervisor</li><li>User Supervisor</li><li>Instructor</li><li>Skills Checklist Observer</li><li>Skills Checklist Data Entry</li></ul></li></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user(user_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateUserRequest user_information: the information of the user (required)
        :return: CreateUserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_user_with_http_info(user_information, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_with_http_info(user_information, **kwargs)  # noqa: E501
            return data

    def create_user_with_http_info(self, user_information, **kwargs):  # noqa: E501
        """Creates a user with the supplied information  # noqa: E501

        Notes:  <ul><li>Org ID is required and should be the ID of your organization.</li><li>First Name is required and must not exceed 50 characters.</li><li>Last Name is required and must not exceed 50 characters.</li><li>Username is required, must be unique within your organization and not exceed 255 characters.</li><li>Email is required when supplying User Roles other than learner and must not exceed 150 characters.</li><li>Password is required and must be at minimum 4 characters long.</li><li>Job Titles, Departments, Location and Hierarchy ID are optional.</li><li>Learner ID, optional, must be unique within your organization and not exceed 50 characters.</li><li>GUID, optional, must be unique within your organization and not exceed 50 characters.</li><li>User Roles are optional but may be supplied to provide additional roles beyond learner.<br />          Options Include:          <ul><li>Administrator</li><li>Report Supervisor</li><li>Enrollment Supervisor</li><li>User Supervisor</li><li>Instructor</li><li>Skills Checklist Observer</li><li>Skills Checklist Data Entry</li></ul></li></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_with_http_info(user_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateUserRequest user_information: the information of the user (required)
        :return: CreateUserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_information']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_information' is set
        if self.api_client.client_side_validation and ('user_information' not in params or
                                                       params['user_information'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_information` when calling `create_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_information' in params:
            body_params = params['user_information']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateUserResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user(self, username, **kwargs):  # noqa: E501
        """Retrieves a user based on the username provided  # noqa: E501

        When providing username, be sure to URL encode the value if it contains any special characters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: the username of the user (required)
        :param int org_id: organization ID of the user (defaults to current organization ID)
        :return: GetUserModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def get_user_with_http_info(self, username, **kwargs):  # noqa: E501
        """Retrieves a user based on the username provided  # noqa: E501

        When providing username, be sure to URL encode the value if it contains any special characters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: the username of the user (required)
        :param int org_id: organization ID of the user (defaults to current organization ID)
        :return: GetUserModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []
        if 'org_id' in params:
            query_params.append(('orgId', params['org_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/users/{username}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetUserModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_user(self, username, request, **kwargs):  # noqa: E501
        """Update a user using JSON patch documents.  # noqa: E501

        When providing username, be sure to URL encode the value if it contains any special characters.  Provide a set of one or more JSON patch documents describing the changes to apply to the applicant.  See http://jsonpatch.com/ and below for examples.  <br />  Fields that can be updated include:  <ul><li>First name          <pre>{\"op\": \"replace\", \"path\": \"/FirstName\", \"value\": \"new name\"}</pre></li><br /><li>Last name          <pre>{\"op\": \"replace\", \"path\": \"/LastName\", \"value\": \"new name\"}</pre></li><br /><li>Username          <pre>{\"op\": \"replace\", \"path\": \"/UserName\", \"value\": \"new_username\"}</pre></li><br /><li>Email          <pre>{\"op\": \"replace\", \"path\": \"/Email\", \"value\": \"new@email.com\"}</pre></li><br /><li>Password          <pre>{\"op\": \"replace\", \"path\": \"/Password\", \"value\": \"new_password\"}</pre></li><br /><li>Job titles          <pre>{\"op\": \"replace\", \"path\": \"/JobTitles\", \"value\": [\"Job title 1\", \"Job title 2\"]}</pre></li><br /><li>Departments          <pre>{\"op\": \"replace\", \"path\": \"/Departments\", \"value\": [\"Department 1\", \"Department 2\"]}</pre></li><br /><li>Location          <pre>{\"op\": \"replace\", \"path\": \"/Location\", \"value\": \"new location\"}</pre></li><br /><li>Hierarchy ID          <pre>{\"op\": \"replace\", \"path\": \"/HierarchyId\", \"value\": 1}</pre></li><br /><li>Learner ID          <pre>{\"op\": \"replace\", \"path\": \"/LearnerId\", \"value\": \"new learner ID\"}</pre></li><br /><li>GUID          <pre>{\"op\": \"replace\", \"path\": \"/Guid\", \"value\": \"new GUID\"}</pre></li><br /><li>User roles          <pre>{\"op\": \"replace\", \"path\": \"/UserRoles\", \"value\": [\"Administrator\", \"Enrollment Supervisor\"]}</pre>          Options:          <ul><li>Administrator</li><li>Report Supervisor</li><li>Enrollment Supervisor</li><li>User Supervisor</li><li>Instructor</li><li>Skills Checklist Observer</li><li>Skills Checklist Data Entry</li></ul></li><br /><li>User status          <pre>{\"op\": \"replace\", \"path\": \"/UserStatus\", \"value\": \"Inactive\"}</pre>          Options:          <ul><li>Active</li><li>Inactive</li><li>OnLeave</li></ul></li><br /><li>Require password change          <pre>{\"op\": \"replace\", \"path\": \"/RequirePasswordChange\", \"value\": true}</pre>          Options:          <ul><li>True</li><li>False</li></ul></li></ul><p>  Note that the <b>path</b> parameter is case sensitive.  <br /><br />  Example: Changing a user's first name, last name, departments and user roles  </p><pre>  [      {\"op\": \"replace\", \"path\": \"/FirstName\", \"value\": \"new first name\"},      {\"op\": \"replace\", \"path\": \"/LastName\", \"value\": \"new last name\"},      {\"op\": \"replace\", \"path\": \"/Departments\", \"value\": [\"department1\", \"department2\"]},      {\"op\": \"replace\", \"path\": \"/UserRoles\", \"value\": [\"Instructor\", \"Skills Checklist Data Entry\"]}  ]  </pre>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user(username, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: The username of the user to update. (required)
        :param list[Operation] request: An array of JSON patch documents. (required)
        :param int org_id: Organization ID of the user (defaults to current organization ID)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_with_http_info(username, request, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_with_http_info(username, request, **kwargs)  # noqa: E501
            return data

    def update_user_with_http_info(self, username, request, **kwargs):  # noqa: E501
        """Update a user using JSON patch documents.  # noqa: E501

        When providing username, be sure to URL encode the value if it contains any special characters.  Provide a set of one or more JSON patch documents describing the changes to apply to the applicant.  See http://jsonpatch.com/ and below for examples.  <br />  Fields that can be updated include:  <ul><li>First name          <pre>{\"op\": \"replace\", \"path\": \"/FirstName\", \"value\": \"new name\"}</pre></li><br /><li>Last name          <pre>{\"op\": \"replace\", \"path\": \"/LastName\", \"value\": \"new name\"}</pre></li><br /><li>Username          <pre>{\"op\": \"replace\", \"path\": \"/UserName\", \"value\": \"new_username\"}</pre></li><br /><li>Email          <pre>{\"op\": \"replace\", \"path\": \"/Email\", \"value\": \"new@email.com\"}</pre></li><br /><li>Password          <pre>{\"op\": \"replace\", \"path\": \"/Password\", \"value\": \"new_password\"}</pre></li><br /><li>Job titles          <pre>{\"op\": \"replace\", \"path\": \"/JobTitles\", \"value\": [\"Job title 1\", \"Job title 2\"]}</pre></li><br /><li>Departments          <pre>{\"op\": \"replace\", \"path\": \"/Departments\", \"value\": [\"Department 1\", \"Department 2\"]}</pre></li><br /><li>Location          <pre>{\"op\": \"replace\", \"path\": \"/Location\", \"value\": \"new location\"}</pre></li><br /><li>Hierarchy ID          <pre>{\"op\": \"replace\", \"path\": \"/HierarchyId\", \"value\": 1}</pre></li><br /><li>Learner ID          <pre>{\"op\": \"replace\", \"path\": \"/LearnerId\", \"value\": \"new learner ID\"}</pre></li><br /><li>GUID          <pre>{\"op\": \"replace\", \"path\": \"/Guid\", \"value\": \"new GUID\"}</pre></li><br /><li>User roles          <pre>{\"op\": \"replace\", \"path\": \"/UserRoles\", \"value\": [\"Administrator\", \"Enrollment Supervisor\"]}</pre>          Options:          <ul><li>Administrator</li><li>Report Supervisor</li><li>Enrollment Supervisor</li><li>User Supervisor</li><li>Instructor</li><li>Skills Checklist Observer</li><li>Skills Checklist Data Entry</li></ul></li><br /><li>User status          <pre>{\"op\": \"replace\", \"path\": \"/UserStatus\", \"value\": \"Inactive\"}</pre>          Options:          <ul><li>Active</li><li>Inactive</li><li>OnLeave</li></ul></li><br /><li>Require password change          <pre>{\"op\": \"replace\", \"path\": \"/RequirePasswordChange\", \"value\": true}</pre>          Options:          <ul><li>True</li><li>False</li></ul></li></ul><p>  Note that the <b>path</b> parameter is case sensitive.  <br /><br />  Example: Changing a user's first name, last name, departments and user roles  </p><pre>  [      {\"op\": \"replace\", \"path\": \"/FirstName\", \"value\": \"new first name\"},      {\"op\": \"replace\", \"path\": \"/LastName\", \"value\": \"new last name\"},      {\"op\": \"replace\", \"path\": \"/Departments\", \"value\": [\"department1\", \"department2\"]},      {\"op\": \"replace\", \"path\": \"/UserRoles\", \"value\": [\"Instructor\", \"Skills Checklist Data Entry\"]}  ]  </pre>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_with_http_info(username, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: The username of the user to update. (required)
        :param list[Operation] request: An array of JSON patch documents. (required)
        :param int org_id: Organization ID of the user (defaults to current organization ID)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'request', 'org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `update_user`")  # noqa: E501
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in params or
                                                       params['request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `request` when calling `update_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []
        if 'org_id' in params:
            query_params.append(('orgId', params['org_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/users/{username}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)