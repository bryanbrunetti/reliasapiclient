# coding: utf-8

"""
    Relias API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from relias_api_client.configuration import Configuration


class CreateBundleAssignmentResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bundle_assignment_id': 'int',
        'user_id': 'int',
        'bundle_id': 'int',
        'expiration': 'datetime'
    }

    attribute_map = {
        'bundle_assignment_id': 'bundleAssignmentId',
        'user_id': 'userId',
        'bundle_id': 'bundleId',
        'expiration': 'expiration'
    }

    def __init__(self, bundle_assignment_id=None, user_id=None, bundle_id=None, expiration=None, _configuration=None):  # noqa: E501
        """CreateBundleAssignmentResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bundle_assignment_id = None
        self._user_id = None
        self._bundle_id = None
        self._expiration = None
        self.discriminator = None

        if bundle_assignment_id is not None:
            self.bundle_assignment_id = bundle_assignment_id
        if user_id is not None:
            self.user_id = user_id
        if bundle_id is not None:
            self.bundle_id = bundle_id
        if expiration is not None:
            self.expiration = expiration

    @property
    def bundle_assignment_id(self):
        """Gets the bundle_assignment_id of this CreateBundleAssignmentResponse.  # noqa: E501


        :return: The bundle_assignment_id of this CreateBundleAssignmentResponse.  # noqa: E501
        :rtype: int
        """
        return self._bundle_assignment_id

    @bundle_assignment_id.setter
    def bundle_assignment_id(self, bundle_assignment_id):
        """Sets the bundle_assignment_id of this CreateBundleAssignmentResponse.


        :param bundle_assignment_id: The bundle_assignment_id of this CreateBundleAssignmentResponse.  # noqa: E501
        :type: int
        """

        self._bundle_assignment_id = bundle_assignment_id

    @property
    def user_id(self):
        """Gets the user_id of this CreateBundleAssignmentResponse.  # noqa: E501


        :return: The user_id of this CreateBundleAssignmentResponse.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateBundleAssignmentResponse.


        :param user_id: The user_id of this CreateBundleAssignmentResponse.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def bundle_id(self):
        """Gets the bundle_id of this CreateBundleAssignmentResponse.  # noqa: E501


        :return: The bundle_id of this CreateBundleAssignmentResponse.  # noqa: E501
        :rtype: int
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this CreateBundleAssignmentResponse.


        :param bundle_id: The bundle_id of this CreateBundleAssignmentResponse.  # noqa: E501
        :type: int
        """

        self._bundle_id = bundle_id

    @property
    def expiration(self):
        """Gets the expiration of this CreateBundleAssignmentResponse.  # noqa: E501


        :return: The expiration of this CreateBundleAssignmentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this CreateBundleAssignmentResponse.


        :param expiration: The expiration of this CreateBundleAssignmentResponse.  # noqa: E501
        :type: datetime
        """

        self._expiration = expiration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CreateBundleAssignmentResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateBundleAssignmentResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateBundleAssignmentResponse):
            return True

        return self.to_dict() != other.to_dict()
