# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class NegativeCacheRuleForBatchUpdateCdnConfigInput(object):
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
        'action': 'str',
        'ignore_case': 'bool',
        'status_code': 'str',
        'ttl': 'int'
    }

    attribute_map = {
        'action': 'Action',
        'ignore_case': 'IgnoreCase',
        'status_code': 'StatusCode',
        'ttl': 'Ttl'
    }

    def __init__(self, action=None, ignore_case=None, status_code=None, ttl=None, _configuration=None):  # noqa: E501
        """NegativeCacheRuleForBatchUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._ignore_case = None
        self._status_code = None
        self._ttl = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if ignore_case is not None:
            self.ignore_case = ignore_case
        if status_code is not None:
            self.status_code = status_code
        if ttl is not None:
            self.ttl = ttl

    @property
    def action(self):
        """Gets the action of this NegativeCacheRuleForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The action of this NegativeCacheRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NegativeCacheRuleForBatchUpdateCdnConfigInput.


        :param action: The action of this NegativeCacheRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def ignore_case(self):
        """Gets the ignore_case of this NegativeCacheRuleForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The ignore_case of this NegativeCacheRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_case

    @ignore_case.setter
    def ignore_case(self, ignore_case):
        """Sets the ignore_case of this NegativeCacheRuleForBatchUpdateCdnConfigInput.


        :param ignore_case: The ignore_case of this NegativeCacheRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: bool
        """

        self._ignore_case = ignore_case

    @property
    def status_code(self):
        """Gets the status_code of this NegativeCacheRuleForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The status_code of this NegativeCacheRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this NegativeCacheRuleForBatchUpdateCdnConfigInput.


        :param status_code: The status_code of this NegativeCacheRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._status_code = status_code

    @property
    def ttl(self):
        """Gets the ttl of this NegativeCacheRuleForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The ttl of this NegativeCacheRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this NegativeCacheRuleForBatchUpdateCdnConfigInput.


        :param ttl: The ttl of this NegativeCacheRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

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
        if issubclass(NegativeCacheRuleForBatchUpdateCdnConfigInput, dict):
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
        if not isinstance(other, NegativeCacheRuleForBatchUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NegativeCacheRuleForBatchUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
