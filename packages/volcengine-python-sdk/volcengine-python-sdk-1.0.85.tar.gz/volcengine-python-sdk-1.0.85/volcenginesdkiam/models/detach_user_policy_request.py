# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DetachUserPolicyRequest(object):
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
        'policy_name': 'str',
        'policy_type': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'policy_name': 'PolicyName',
        'policy_type': 'PolicyType',
        'user_name': 'UserName'
    }

    def __init__(self, policy_name=None, policy_type=None, user_name=None, _configuration=None):  # noqa: E501
        """DetachUserPolicyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._policy_name = None
        self._policy_type = None
        self._user_name = None
        self.discriminator = None

        self.policy_name = policy_name
        self.policy_type = policy_type
        self.user_name = user_name

    @property
    def policy_name(self):
        """Gets the policy_name of this DetachUserPolicyRequest.  # noqa: E501


        :return: The policy_name of this DetachUserPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this DetachUserPolicyRequest.


        :param policy_name: The policy_name of this DetachUserPolicyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and policy_name is None:
            raise ValueError("Invalid value for `policy_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                policy_name is not None and len(policy_name) > 64):
            raise ValueError("Invalid value for `policy_name`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                policy_name is not None and len(policy_name) < 1):
            raise ValueError("Invalid value for `policy_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._policy_name = policy_name

    @property
    def policy_type(self):
        """Gets the policy_type of this DetachUserPolicyRequest.  # noqa: E501


        :return: The policy_type of this DetachUserPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """Sets the policy_type of this DetachUserPolicyRequest.


        :param policy_type: The policy_type of this DetachUserPolicyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and policy_type is None:
            raise ValueError("Invalid value for `policy_type`, must not be `None`")  # noqa: E501
        allowed_values = ["System", "Custom"]  # noqa: E501
        if (self._configuration.client_side_validation and
                policy_type not in allowed_values):
            raise ValueError(
                "Invalid value for `policy_type` ({0}), must be one of {1}"  # noqa: E501
                .format(policy_type, allowed_values)
            )

        self._policy_type = policy_type

    @property
    def user_name(self):
        """Gets the user_name of this DetachUserPolicyRequest.  # noqa: E501


        :return: The user_name of this DetachUserPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this DetachUserPolicyRequest.


        :param user_name: The user_name of this DetachUserPolicyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                user_name is not None and len(user_name) > 64):
            raise ValueError("Invalid value for `user_name`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                user_name is not None and len(user_name) < 1):
            raise ValueError("Invalid value for `user_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_name = user_name

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
        if issubclass(DetachUserPolicyRequest, dict):
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
        if not isinstance(other, DetachUserPolicyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetachUserPolicyRequest):
            return True

        return self.to_dict() != other.to_dict()
