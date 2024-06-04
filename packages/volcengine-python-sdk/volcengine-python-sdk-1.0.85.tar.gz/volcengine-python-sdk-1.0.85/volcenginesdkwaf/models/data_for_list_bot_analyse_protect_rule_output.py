# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForListBotAnalyseProtectRuleOutput(object):
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
        'enable_count': 'int',
        'path': 'str',
        'rule_group': 'list[RuleGroupForListBotAnalyseProtectRuleOutput]',
        'total_count': 'int'
    }

    attribute_map = {
        'enable_count': 'EnableCount',
        'path': 'Path',
        'rule_group': 'RuleGroup',
        'total_count': 'TotalCount'
    }

    def __init__(self, enable_count=None, path=None, rule_group=None, total_count=None, _configuration=None):  # noqa: E501
        """DataForListBotAnalyseProtectRuleOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable_count = None
        self._path = None
        self._rule_group = None
        self._total_count = None
        self.discriminator = None

        if enable_count is not None:
            self.enable_count = enable_count
        if path is not None:
            self.path = path
        if rule_group is not None:
            self.rule_group = rule_group
        if total_count is not None:
            self.total_count = total_count

    @property
    def enable_count(self):
        """Gets the enable_count of this DataForListBotAnalyseProtectRuleOutput.  # noqa: E501


        :return: The enable_count of this DataForListBotAnalyseProtectRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._enable_count

    @enable_count.setter
    def enable_count(self, enable_count):
        """Sets the enable_count of this DataForListBotAnalyseProtectRuleOutput.


        :param enable_count: The enable_count of this DataForListBotAnalyseProtectRuleOutput.  # noqa: E501
        :type: int
        """

        self._enable_count = enable_count

    @property
    def path(self):
        """Gets the path of this DataForListBotAnalyseProtectRuleOutput.  # noqa: E501


        :return: The path of this DataForListBotAnalyseProtectRuleOutput.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DataForListBotAnalyseProtectRuleOutput.


        :param path: The path of this DataForListBotAnalyseProtectRuleOutput.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def rule_group(self):
        """Gets the rule_group of this DataForListBotAnalyseProtectRuleOutput.  # noqa: E501


        :return: The rule_group of this DataForListBotAnalyseProtectRuleOutput.  # noqa: E501
        :rtype: list[RuleGroupForListBotAnalyseProtectRuleOutput]
        """
        return self._rule_group

    @rule_group.setter
    def rule_group(self, rule_group):
        """Sets the rule_group of this DataForListBotAnalyseProtectRuleOutput.


        :param rule_group: The rule_group of this DataForListBotAnalyseProtectRuleOutput.  # noqa: E501
        :type: list[RuleGroupForListBotAnalyseProtectRuleOutput]
        """

        self._rule_group = rule_group

    @property
    def total_count(self):
        """Gets the total_count of this DataForListBotAnalyseProtectRuleOutput.  # noqa: E501


        :return: The total_count of this DataForListBotAnalyseProtectRuleOutput.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this DataForListBotAnalyseProtectRuleOutput.


        :param total_count: The total_count of this DataForListBotAnalyseProtectRuleOutput.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(DataForListBotAnalyseProtectRuleOutput, dict):
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
        if not isinstance(other, DataForListBotAnalyseProtectRuleOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListBotAnalyseProtectRuleOutput):
            return True

        return self.to_dict() != other.to_dict()
