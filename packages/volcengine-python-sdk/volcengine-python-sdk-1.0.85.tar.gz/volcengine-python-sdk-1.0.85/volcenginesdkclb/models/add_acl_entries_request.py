# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AddAclEntriesRequest(object):
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
        'acl_entries': 'list[AclEntryForAddAclEntriesInput]',
        'acl_id': 'str'
    }

    attribute_map = {
        'acl_entries': 'AclEntries',
        'acl_id': 'AclId'
    }

    def __init__(self, acl_entries=None, acl_id=None, _configuration=None):  # noqa: E501
        """AddAclEntriesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._acl_entries = None
        self._acl_id = None
        self.discriminator = None

        if acl_entries is not None:
            self.acl_entries = acl_entries
        self.acl_id = acl_id

    @property
    def acl_entries(self):
        """Gets the acl_entries of this AddAclEntriesRequest.  # noqa: E501


        :return: The acl_entries of this AddAclEntriesRequest.  # noqa: E501
        :rtype: list[AclEntryForAddAclEntriesInput]
        """
        return self._acl_entries

    @acl_entries.setter
    def acl_entries(self, acl_entries):
        """Sets the acl_entries of this AddAclEntriesRequest.


        :param acl_entries: The acl_entries of this AddAclEntriesRequest.  # noqa: E501
        :type: list[AclEntryForAddAclEntriesInput]
        """

        self._acl_entries = acl_entries

    @property
    def acl_id(self):
        """Gets the acl_id of this AddAclEntriesRequest.  # noqa: E501


        :return: The acl_id of this AddAclEntriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._acl_id

    @acl_id.setter
    def acl_id(self, acl_id):
        """Sets the acl_id of this AddAclEntriesRequest.


        :param acl_id: The acl_id of this AddAclEntriesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and acl_id is None:
            raise ValueError("Invalid value for `acl_id`, must not be `None`")  # noqa: E501

        self._acl_id = acl_id

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
        if issubclass(AddAclEntriesRequest, dict):
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
        if not isinstance(other, AddAclEntriesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddAclEntriesRequest):
            return True

        return self.to_dict() != other.to_dict()
