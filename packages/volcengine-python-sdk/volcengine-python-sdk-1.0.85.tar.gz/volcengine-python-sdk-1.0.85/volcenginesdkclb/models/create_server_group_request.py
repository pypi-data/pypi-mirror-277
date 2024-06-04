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


class CreateServerGroupRequest(object):
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
        'address_ip_version': 'str',
        'description': 'str',
        'load_balancer_id': 'str',
        'server_group_name': 'str',
        'servers': 'list[ServerForCreateServerGroupInput]',
        'tags': 'list[TagForCreateServerGroupInput]',
        'type': 'str'
    }

    attribute_map = {
        'address_ip_version': 'AddressIpVersion',
        'description': 'Description',
        'load_balancer_id': 'LoadBalancerId',
        'server_group_name': 'ServerGroupName',
        'servers': 'Servers',
        'tags': 'Tags',
        'type': 'Type'
    }

    def __init__(self, address_ip_version=None, description=None, load_balancer_id=None, server_group_name=None, servers=None, tags=None, type=None, _configuration=None):  # noqa: E501
        """CreateServerGroupRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address_ip_version = None
        self._description = None
        self._load_balancer_id = None
        self._server_group_name = None
        self._servers = None
        self._tags = None
        self._type = None
        self.discriminator = None

        if address_ip_version is not None:
            self.address_ip_version = address_ip_version
        if description is not None:
            self.description = description
        self.load_balancer_id = load_balancer_id
        if server_group_name is not None:
            self.server_group_name = server_group_name
        if servers is not None:
            self.servers = servers
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type

    @property
    def address_ip_version(self):
        """Gets the address_ip_version of this CreateServerGroupRequest.  # noqa: E501


        :return: The address_ip_version of this CreateServerGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_ip_version

    @address_ip_version.setter
    def address_ip_version(self, address_ip_version):
        """Sets the address_ip_version of this CreateServerGroupRequest.


        :param address_ip_version: The address_ip_version of this CreateServerGroupRequest.  # noqa: E501
        :type: str
        """

        self._address_ip_version = address_ip_version

    @property
    def description(self):
        """Gets the description of this CreateServerGroupRequest.  # noqa: E501


        :return: The description of this CreateServerGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateServerGroupRequest.


        :param description: The description of this CreateServerGroupRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def load_balancer_id(self):
        """Gets the load_balancer_id of this CreateServerGroupRequest.  # noqa: E501


        :return: The load_balancer_id of this CreateServerGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """Sets the load_balancer_id of this CreateServerGroupRequest.


        :param load_balancer_id: The load_balancer_id of this CreateServerGroupRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and load_balancer_id is None:
            raise ValueError("Invalid value for `load_balancer_id`, must not be `None`")  # noqa: E501

        self._load_balancer_id = load_balancer_id

    @property
    def server_group_name(self):
        """Gets the server_group_name of this CreateServerGroupRequest.  # noqa: E501


        :return: The server_group_name of this CreateServerGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_group_name

    @server_group_name.setter
    def server_group_name(self, server_group_name):
        """Sets the server_group_name of this CreateServerGroupRequest.


        :param server_group_name: The server_group_name of this CreateServerGroupRequest.  # noqa: E501
        :type: str
        """

        self._server_group_name = server_group_name

    @property
    def servers(self):
        """Gets the servers of this CreateServerGroupRequest.  # noqa: E501


        :return: The servers of this CreateServerGroupRequest.  # noqa: E501
        :rtype: list[ServerForCreateServerGroupInput]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this CreateServerGroupRequest.


        :param servers: The servers of this CreateServerGroupRequest.  # noqa: E501
        :type: list[ServerForCreateServerGroupInput]
        """

        self._servers = servers

    @property
    def tags(self):
        """Gets the tags of this CreateServerGroupRequest.  # noqa: E501


        :return: The tags of this CreateServerGroupRequest.  # noqa: E501
        :rtype: list[TagForCreateServerGroupInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateServerGroupRequest.


        :param tags: The tags of this CreateServerGroupRequest.  # noqa: E501
        :type: list[TagForCreateServerGroupInput]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this CreateServerGroupRequest.  # noqa: E501


        :return: The type of this CreateServerGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateServerGroupRequest.


        :param type: The type of this CreateServerGroupRequest.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(CreateServerGroupRequest, dict):
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
        if not isinstance(other, CreateServerGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateServerGroupRequest):
            return True

        return self.to_dict() != other.to_dict()
