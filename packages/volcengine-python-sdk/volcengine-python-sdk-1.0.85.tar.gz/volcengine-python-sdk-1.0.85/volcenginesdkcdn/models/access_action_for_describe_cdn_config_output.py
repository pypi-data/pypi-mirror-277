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


class AccessActionForDescribeCdnConfigOutput(object):
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
        'allow_empty': 'bool',
        'list_rules': 'list[str]',
        'request_header': 'str',
        'rule_type': 'str'
    }

    attribute_map = {
        'allow_empty': 'AllowEmpty',
        'list_rules': 'ListRules',
        'request_header': 'RequestHeader',
        'rule_type': 'RuleType'
    }

    def __init__(self, allow_empty=None, list_rules=None, request_header=None, rule_type=None, _configuration=None):  # noqa: E501
        """AccessActionForDescribeCdnConfigOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_empty = None
        self._list_rules = None
        self._request_header = None
        self._rule_type = None
        self.discriminator = None

        if allow_empty is not None:
            self.allow_empty = allow_empty
        if list_rules is not None:
            self.list_rules = list_rules
        if request_header is not None:
            self.request_header = request_header
        if rule_type is not None:
            self.rule_type = rule_type

    @property
    def allow_empty(self):
        """Gets the allow_empty of this AccessActionForDescribeCdnConfigOutput.  # noqa: E501


        :return: The allow_empty of this AccessActionForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: bool
        """
        return self._allow_empty

    @allow_empty.setter
    def allow_empty(self, allow_empty):
        """Sets the allow_empty of this AccessActionForDescribeCdnConfigOutput.


        :param allow_empty: The allow_empty of this AccessActionForDescribeCdnConfigOutput.  # noqa: E501
        :type: bool
        """

        self._allow_empty = allow_empty

    @property
    def list_rules(self):
        """Gets the list_rules of this AccessActionForDescribeCdnConfigOutput.  # noqa: E501


        :return: The list_rules of this AccessActionForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._list_rules

    @list_rules.setter
    def list_rules(self, list_rules):
        """Sets the list_rules of this AccessActionForDescribeCdnConfigOutput.


        :param list_rules: The list_rules of this AccessActionForDescribeCdnConfigOutput.  # noqa: E501
        :type: list[str]
        """

        self._list_rules = list_rules

    @property
    def request_header(self):
        """Gets the request_header of this AccessActionForDescribeCdnConfigOutput.  # noqa: E501


        :return: The request_header of this AccessActionForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._request_header

    @request_header.setter
    def request_header(self, request_header):
        """Sets the request_header of this AccessActionForDescribeCdnConfigOutput.


        :param request_header: The request_header of this AccessActionForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._request_header = request_header

    @property
    def rule_type(self):
        """Gets the rule_type of this AccessActionForDescribeCdnConfigOutput.  # noqa: E501


        :return: The rule_type of this AccessActionForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this AccessActionForDescribeCdnConfigOutput.


        :param rule_type: The rule_type of this AccessActionForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._rule_type = rule_type

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
        if issubclass(AccessActionForDescribeCdnConfigOutput, dict):
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
        if not isinstance(other, AccessActionForDescribeCdnConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessActionForDescribeCdnConfigOutput):
            return True

        return self.to_dict() != other.to_dict()
