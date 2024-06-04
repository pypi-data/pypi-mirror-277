# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class NodeInfoForRestoreToNewInstanceInput(object):
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
        'node_id': 'str',
        'node_operate_type': 'str',
        'node_spec': 'str',
        'node_type': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'node_id': 'NodeId',
        'node_operate_type': 'NodeOperateType',
        'node_spec': 'NodeSpec',
        'node_type': 'NodeType',
        'zone_id': 'ZoneId'
    }

    def __init__(self, node_id=None, node_operate_type=None, node_spec=None, node_type=None, zone_id=None, _configuration=None):  # noqa: E501
        """NodeInfoForRestoreToNewInstanceInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._node_id = None
        self._node_operate_type = None
        self._node_spec = None
        self._node_type = None
        self._zone_id = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if node_operate_type is not None:
            self.node_operate_type = node_operate_type
        if node_spec is not None:
            self.node_spec = node_spec
        if node_type is not None:
            self.node_type = node_type
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def node_id(self):
        """Gets the node_id of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501


        :return: The node_id of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this NodeInfoForRestoreToNewInstanceInput.


        :param node_id: The node_id of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def node_operate_type(self):
        """Gets the node_operate_type of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501


        :return: The node_operate_type of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._node_operate_type

    @node_operate_type.setter
    def node_operate_type(self, node_operate_type):
        """Sets the node_operate_type of this NodeInfoForRestoreToNewInstanceInput.


        :param node_operate_type: The node_operate_type of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501
        :type: str
        """

        self._node_operate_type = node_operate_type

    @property
    def node_spec(self):
        """Gets the node_spec of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501


        :return: The node_spec of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._node_spec

    @node_spec.setter
    def node_spec(self, node_spec):
        """Sets the node_spec of this NodeInfoForRestoreToNewInstanceInput.


        :param node_spec: The node_spec of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501
        :type: str
        """

        self._node_spec = node_spec

    @property
    def node_type(self):
        """Gets the node_type of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501


        :return: The node_type of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this NodeInfoForRestoreToNewInstanceInput.


        :param node_type: The node_type of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501
        :type: str
        """

        self._node_type = node_type

    @property
    def zone_id(self):
        """Gets the zone_id of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501


        :return: The zone_id of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this NodeInfoForRestoreToNewInstanceInput.


        :param zone_id: The zone_id of this NodeInfoForRestoreToNewInstanceInput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(NodeInfoForRestoreToNewInstanceInput, dict):
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
        if not isinstance(other, NodeInfoForRestoreToNewInstanceInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeInfoForRestoreToNewInstanceInput):
            return True

        return self.to_dict() != other.to_dict()
