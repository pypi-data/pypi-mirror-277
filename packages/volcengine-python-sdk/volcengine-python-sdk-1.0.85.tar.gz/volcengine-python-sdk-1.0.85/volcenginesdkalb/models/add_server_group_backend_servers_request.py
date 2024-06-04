# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AddServerGroupBackendServersRequest(object):
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
        'server_group_id': 'str',
        'servers': 'list[ServerForAddServerGroupBackendServersInput]'
    }

    attribute_map = {
        'server_group_id': 'ServerGroupId',
        'servers': 'Servers'
    }

    def __init__(self, server_group_id=None, servers=None, _configuration=None):  # noqa: E501
        """AddServerGroupBackendServersRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._server_group_id = None
        self._servers = None
        self.discriminator = None

        self.server_group_id = server_group_id
        if servers is not None:
            self.servers = servers

    @property
    def server_group_id(self):
        """Gets the server_group_id of this AddServerGroupBackendServersRequest.  # noqa: E501


        :return: The server_group_id of this AddServerGroupBackendServersRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this AddServerGroupBackendServersRequest.


        :param server_group_id: The server_group_id of this AddServerGroupBackendServersRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and server_group_id is None:
            raise ValueError("Invalid value for `server_group_id`, must not be `None`")  # noqa: E501

        self._server_group_id = server_group_id

    @property
    def servers(self):
        """Gets the servers of this AddServerGroupBackendServersRequest.  # noqa: E501


        :return: The servers of this AddServerGroupBackendServersRequest.  # noqa: E501
        :rtype: list[ServerForAddServerGroupBackendServersInput]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this AddServerGroupBackendServersRequest.


        :param servers: The servers of this AddServerGroupBackendServersRequest.  # noqa: E501
        :type: list[ServerForAddServerGroupBackendServersInput]
        """

        self._servers = servers

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
        if issubclass(AddServerGroupBackendServersRequest, dict):
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
        if not isinstance(other, AddServerGroupBackendServersRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddServerGroupBackendServersRequest):
            return True

        return self.to_dict() != other.to_dict()
