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


class DataForListSystemBotConfigOutput(object):
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
        'bot_type': 'str',
        'description': 'str',
        'enable': 'int',
        'rule_tag': 'str'
    }

    attribute_map = {
        'action': 'Action',
        'bot_type': 'BotType',
        'description': 'Description',
        'enable': 'Enable',
        'rule_tag': 'RuleTag'
    }

    def __init__(self, action=None, bot_type=None, description=None, enable=None, rule_tag=None, _configuration=None):  # noqa: E501
        """DataForListSystemBotConfigOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._bot_type = None
        self._description = None
        self._enable = None
        self._rule_tag = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if bot_type is not None:
            self.bot_type = bot_type
        if description is not None:
            self.description = description
        if enable is not None:
            self.enable = enable
        if rule_tag is not None:
            self.rule_tag = rule_tag

    @property
    def action(self):
        """Gets the action of this DataForListSystemBotConfigOutput.  # noqa: E501


        :return: The action of this DataForListSystemBotConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this DataForListSystemBotConfigOutput.


        :param action: The action of this DataForListSystemBotConfigOutput.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def bot_type(self):
        """Gets the bot_type of this DataForListSystemBotConfigOutput.  # noqa: E501


        :return: The bot_type of this DataForListSystemBotConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._bot_type

    @bot_type.setter
    def bot_type(self, bot_type):
        """Sets the bot_type of this DataForListSystemBotConfigOutput.


        :param bot_type: The bot_type of this DataForListSystemBotConfigOutput.  # noqa: E501
        :type: str
        """

        self._bot_type = bot_type

    @property
    def description(self):
        """Gets the description of this DataForListSystemBotConfigOutput.  # noqa: E501


        :return: The description of this DataForListSystemBotConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataForListSystemBotConfigOutput.


        :param description: The description of this DataForListSystemBotConfigOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enable(self):
        """Gets the enable of this DataForListSystemBotConfigOutput.  # noqa: E501


        :return: The enable of this DataForListSystemBotConfigOutput.  # noqa: E501
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this DataForListSystemBotConfigOutput.


        :param enable: The enable of this DataForListSystemBotConfigOutput.  # noqa: E501
        :type: int
        """

        self._enable = enable

    @property
    def rule_tag(self):
        """Gets the rule_tag of this DataForListSystemBotConfigOutput.  # noqa: E501


        :return: The rule_tag of this DataForListSystemBotConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._rule_tag

    @rule_tag.setter
    def rule_tag(self, rule_tag):
        """Sets the rule_tag of this DataForListSystemBotConfigOutput.


        :param rule_tag: The rule_tag of this DataForListSystemBotConfigOutput.  # noqa: E501
        :type: str
        """

        self._rule_tag = rule_tag

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
        if issubclass(DataForListSystemBotConfigOutput, dict):
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
        if not isinstance(other, DataForListSystemBotConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListSystemBotConfigOutput):
            return True

        return self.to_dict() != other.to_dict()
