# coding: utf-8

"""
    directconnect

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyBgpPeerAttributesRequest(object):
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
        'bgp_peer_id': 'str',
        'bgp_peer_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'bgp_peer_id': 'BgpPeerId',
        'bgp_peer_name': 'BgpPeerName',
        'description': 'Description'
    }

    def __init__(self, bgp_peer_id=None, bgp_peer_name=None, description=None, _configuration=None):  # noqa: E501
        """ModifyBgpPeerAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bgp_peer_id = None
        self._bgp_peer_name = None
        self._description = None
        self.discriminator = None

        self.bgp_peer_id = bgp_peer_id
        if bgp_peer_name is not None:
            self.bgp_peer_name = bgp_peer_name
        if description is not None:
            self.description = description

    @property
    def bgp_peer_id(self):
        """Gets the bgp_peer_id of this ModifyBgpPeerAttributesRequest.  # noqa: E501


        :return: The bgp_peer_id of this ModifyBgpPeerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._bgp_peer_id

    @bgp_peer_id.setter
    def bgp_peer_id(self, bgp_peer_id):
        """Sets the bgp_peer_id of this ModifyBgpPeerAttributesRequest.


        :param bgp_peer_id: The bgp_peer_id of this ModifyBgpPeerAttributesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bgp_peer_id is None:
            raise ValueError("Invalid value for `bgp_peer_id`, must not be `None`")  # noqa: E501

        self._bgp_peer_id = bgp_peer_id

    @property
    def bgp_peer_name(self):
        """Gets the bgp_peer_name of this ModifyBgpPeerAttributesRequest.  # noqa: E501


        :return: The bgp_peer_name of this ModifyBgpPeerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._bgp_peer_name

    @bgp_peer_name.setter
    def bgp_peer_name(self, bgp_peer_name):
        """Sets the bgp_peer_name of this ModifyBgpPeerAttributesRequest.


        :param bgp_peer_name: The bgp_peer_name of this ModifyBgpPeerAttributesRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bgp_peer_name is not None and len(bgp_peer_name) > 128):
            raise ValueError("Invalid value for `bgp_peer_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bgp_peer_name is not None and len(bgp_peer_name) < 1):
            raise ValueError("Invalid value for `bgp_peer_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._bgp_peer_name = bgp_peer_name

    @property
    def description(self):
        """Gets the description of this ModifyBgpPeerAttributesRequest.  # noqa: E501


        :return: The description of this ModifyBgpPeerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyBgpPeerAttributesRequest.


        :param description: The description of this ModifyBgpPeerAttributesRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

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
        if issubclass(ModifyBgpPeerAttributesRequest, dict):
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
        if not isinstance(other, ModifyBgpPeerAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyBgpPeerAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()
