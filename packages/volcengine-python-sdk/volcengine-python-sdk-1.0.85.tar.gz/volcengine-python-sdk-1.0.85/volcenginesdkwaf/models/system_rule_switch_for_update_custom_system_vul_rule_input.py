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


class SystemRuleSwitchForUpdateCustomSystemVulRuleInput(object):
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
        'custom_system_rule_switch': 'int',
        'rule_id': 'int'
    }

    attribute_map = {
        'custom_system_rule_switch': 'CustomSystemRuleSwitch',
        'rule_id': 'RuleID'
    }

    def __init__(self, custom_system_rule_switch=None, rule_id=None, _configuration=None):  # noqa: E501
        """SystemRuleSwitchForUpdateCustomSystemVulRuleInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_system_rule_switch = None
        self._rule_id = None
        self.discriminator = None

        if custom_system_rule_switch is not None:
            self.custom_system_rule_switch = custom_system_rule_switch
        if rule_id is not None:
            self.rule_id = rule_id

    @property
    def custom_system_rule_switch(self):
        """Gets the custom_system_rule_switch of this SystemRuleSwitchForUpdateCustomSystemVulRuleInput.  # noqa: E501


        :return: The custom_system_rule_switch of this SystemRuleSwitchForUpdateCustomSystemVulRuleInput.  # noqa: E501
        :rtype: int
        """
        return self._custom_system_rule_switch

    @custom_system_rule_switch.setter
    def custom_system_rule_switch(self, custom_system_rule_switch):
        """Sets the custom_system_rule_switch of this SystemRuleSwitchForUpdateCustomSystemVulRuleInput.


        :param custom_system_rule_switch: The custom_system_rule_switch of this SystemRuleSwitchForUpdateCustomSystemVulRuleInput.  # noqa: E501
        :type: int
        """

        self._custom_system_rule_switch = custom_system_rule_switch

    @property
    def rule_id(self):
        """Gets the rule_id of this SystemRuleSwitchForUpdateCustomSystemVulRuleInput.  # noqa: E501


        :return: The rule_id of this SystemRuleSwitchForUpdateCustomSystemVulRuleInput.  # noqa: E501
        :rtype: int
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this SystemRuleSwitchForUpdateCustomSystemVulRuleInput.


        :param rule_id: The rule_id of this SystemRuleSwitchForUpdateCustomSystemVulRuleInput.  # noqa: E501
        :type: int
        """

        self._rule_id = rule_id

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
        if issubclass(SystemRuleSwitchForUpdateCustomSystemVulRuleInput, dict):
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
        if not isinstance(other, SystemRuleSwitchForUpdateCustomSystemVulRuleInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemRuleSwitchForUpdateCustomSystemVulRuleInput):
            return True

        return self.to_dict() != other.to_dict()
