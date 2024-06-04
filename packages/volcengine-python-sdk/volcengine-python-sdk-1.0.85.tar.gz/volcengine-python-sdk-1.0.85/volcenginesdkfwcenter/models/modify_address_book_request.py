# coding: utf-8

"""
    fwcenter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyAddressBookRequest(object):
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
        'address_list': 'list[str]',
        'description': 'str',
        'group_name': 'str',
        'group_uuid': 'str'
    }

    attribute_map = {
        'address_list': 'AddressList',
        'description': 'Description',
        'group_name': 'GroupName',
        'group_uuid': 'GroupUuid'
    }

    def __init__(self, address_list=None, description=None, group_name=None, group_uuid=None, _configuration=None):  # noqa: E501
        """ModifyAddressBookRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address_list = None
        self._description = None
        self._group_name = None
        self._group_uuid = None
        self.discriminator = None

        if address_list is not None:
            self.address_list = address_list
        if description is not None:
            self.description = description
        self.group_name = group_name
        self.group_uuid = group_uuid

    @property
    def address_list(self):
        """Gets the address_list of this ModifyAddressBookRequest.  # noqa: E501


        :return: The address_list of this ModifyAddressBookRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_list

    @address_list.setter
    def address_list(self, address_list):
        """Sets the address_list of this ModifyAddressBookRequest.


        :param address_list: The address_list of this ModifyAddressBookRequest.  # noqa: E501
        :type: list[str]
        """

        self._address_list = address_list

    @property
    def description(self):
        """Gets the description of this ModifyAddressBookRequest.  # noqa: E501


        :return: The description of this ModifyAddressBookRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyAddressBookRequest.


        :param description: The description of this ModifyAddressBookRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def group_name(self):
        """Gets the group_name of this ModifyAddressBookRequest.  # noqa: E501


        :return: The group_name of this ModifyAddressBookRequest.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ModifyAddressBookRequest.


        :param group_name: The group_name of this ModifyAddressBookRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and group_name is None:
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def group_uuid(self):
        """Gets the group_uuid of this ModifyAddressBookRequest.  # noqa: E501


        :return: The group_uuid of this ModifyAddressBookRequest.  # noqa: E501
        :rtype: str
        """
        return self._group_uuid

    @group_uuid.setter
    def group_uuid(self, group_uuid):
        """Sets the group_uuid of this ModifyAddressBookRequest.


        :param group_uuid: The group_uuid of this ModifyAddressBookRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and group_uuid is None:
            raise ValueError("Invalid value for `group_uuid`, must not be `None`")  # noqa: E501

        self._group_uuid = group_uuid

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
        if issubclass(ModifyAddressBookRequest, dict):
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
        if not isinstance(other, ModifyAddressBookRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyAddressBookRequest):
            return True

        return self.to_dict() != other.to_dict()
