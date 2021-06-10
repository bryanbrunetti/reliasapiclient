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


class AssignableAssessmentModel(object):
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
        'assessment_id': 'int',
        'name': 'str',
        'assessment_type': 'str'
    }

    attribute_map = {
        'assessment_id': 'assessmentId',
        'name': 'name',
        'assessment_type': 'assessmentType'
    }

    def __init__(self, assessment_id=None, name=None, assessment_type=None, _configuration=None):  # noqa: E501
        """AssignableAssessmentModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assessment_id = None
        self._name = None
        self._assessment_type = None
        self.discriminator = None

        if assessment_id is not None:
            self.assessment_id = assessment_id
        if name is not None:
            self.name = name
        if assessment_type is not None:
            self.assessment_type = assessment_type

    @property
    def assessment_id(self):
        """Gets the assessment_id of this AssignableAssessmentModel.  # noqa: E501


        :return: The assessment_id of this AssignableAssessmentModel.  # noqa: E501
        :rtype: int
        """
        return self._assessment_id

    @assessment_id.setter
    def assessment_id(self, assessment_id):
        """Sets the assessment_id of this AssignableAssessmentModel.


        :param assessment_id: The assessment_id of this AssignableAssessmentModel.  # noqa: E501
        :type: int
        """

        self._assessment_id = assessment_id

    @property
    def name(self):
        """Gets the name of this AssignableAssessmentModel.  # noqa: E501


        :return: The name of this AssignableAssessmentModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssignableAssessmentModel.


        :param name: The name of this AssignableAssessmentModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def assessment_type(self):
        """Gets the assessment_type of this AssignableAssessmentModel.  # noqa: E501


        :return: The assessment_type of this AssignableAssessmentModel.  # noqa: E501
        :rtype: str
        """
        return self._assessment_type

    @assessment_type.setter
    def assessment_type(self, assessment_type):
        """Sets the assessment_type of this AssignableAssessmentModel.


        :param assessment_type: The assessment_type of this AssignableAssessmentModel.  # noqa: E501
        :type: str
        """

        self._assessment_type = assessment_type

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
        if issubclass(AssignableAssessmentModel, dict):
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
        if not isinstance(other, AssignableAssessmentModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssignableAssessmentModel):
            return True

        return self.to_dict() != other.to_dict()
