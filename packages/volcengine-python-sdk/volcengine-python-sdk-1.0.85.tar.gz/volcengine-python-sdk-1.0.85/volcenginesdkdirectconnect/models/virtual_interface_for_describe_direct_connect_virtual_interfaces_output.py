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


class VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput(object):
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
        'account_id': 'str',
        'bandwidth': 'int',
        'bfd_detect_interval': 'int',
        'bfd_detect_multiplier': 'int',
        'creation_time': 'str',
        'description': 'str',
        'direct_connect_connection_id': 'str',
        'direct_connect_gateway_id': 'str',
        'enable_bfd': 'bool',
        'enable_nqa': 'bool',
        'local_ip': 'str',
        'local_ipv6_ip': 'str',
        'nqa_detect_interval': 'int',
        'nqa_detect_multiplier': 'int',
        'peer_ip': 'str',
        'peer_ipv6_ip': 'str',
        'route_type': 'str',
        'status': 'str',
        'tags': 'list[TagForDescribeDirectConnectVirtualInterfacesOutput]',
        'update_time': 'str',
        'virtual_interface_id': 'str',
        'virtual_interface_name': 'str',
        'vlan_id': 'int'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'bandwidth': 'Bandwidth',
        'bfd_detect_interval': 'BfdDetectInterval',
        'bfd_detect_multiplier': 'BfdDetectMultiplier',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'direct_connect_connection_id': 'DirectConnectConnectionId',
        'direct_connect_gateway_id': 'DirectConnectGatewayId',
        'enable_bfd': 'EnableBfd',
        'enable_nqa': 'EnableNqa',
        'local_ip': 'LocalIp',
        'local_ipv6_ip': 'LocalIpv6Ip',
        'nqa_detect_interval': 'NqaDetectInterval',
        'nqa_detect_multiplier': 'NqaDetectMultiplier',
        'peer_ip': 'PeerIp',
        'peer_ipv6_ip': 'PeerIpv6Ip',
        'route_type': 'RouteType',
        'status': 'Status',
        'tags': 'Tags',
        'update_time': 'UpdateTime',
        'virtual_interface_id': 'VirtualInterfaceId',
        'virtual_interface_name': 'VirtualInterfaceName',
        'vlan_id': 'VlanId'
    }

    def __init__(self, account_id=None, bandwidth=None, bfd_detect_interval=None, bfd_detect_multiplier=None, creation_time=None, description=None, direct_connect_connection_id=None, direct_connect_gateway_id=None, enable_bfd=None, enable_nqa=None, local_ip=None, local_ipv6_ip=None, nqa_detect_interval=None, nqa_detect_multiplier=None, peer_ip=None, peer_ipv6_ip=None, route_type=None, status=None, tags=None, update_time=None, virtual_interface_id=None, virtual_interface_name=None, vlan_id=None, _configuration=None):  # noqa: E501
        """VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._bandwidth = None
        self._bfd_detect_interval = None
        self._bfd_detect_multiplier = None
        self._creation_time = None
        self._description = None
        self._direct_connect_connection_id = None
        self._direct_connect_gateway_id = None
        self._enable_bfd = None
        self._enable_nqa = None
        self._local_ip = None
        self._local_ipv6_ip = None
        self._nqa_detect_interval = None
        self._nqa_detect_multiplier = None
        self._peer_ip = None
        self._peer_ipv6_ip = None
        self._route_type = None
        self._status = None
        self._tags = None
        self._update_time = None
        self._virtual_interface_id = None
        self._virtual_interface_name = None
        self._vlan_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if bfd_detect_interval is not None:
            self.bfd_detect_interval = bfd_detect_interval
        if bfd_detect_multiplier is not None:
            self.bfd_detect_multiplier = bfd_detect_multiplier
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if direct_connect_connection_id is not None:
            self.direct_connect_connection_id = direct_connect_connection_id
        if direct_connect_gateway_id is not None:
            self.direct_connect_gateway_id = direct_connect_gateway_id
        if enable_bfd is not None:
            self.enable_bfd = enable_bfd
        if enable_nqa is not None:
            self.enable_nqa = enable_nqa
        if local_ip is not None:
            self.local_ip = local_ip
        if local_ipv6_ip is not None:
            self.local_ipv6_ip = local_ipv6_ip
        if nqa_detect_interval is not None:
            self.nqa_detect_interval = nqa_detect_interval
        if nqa_detect_multiplier is not None:
            self.nqa_detect_multiplier = nqa_detect_multiplier
        if peer_ip is not None:
            self.peer_ip = peer_ip
        if peer_ipv6_ip is not None:
            self.peer_ipv6_ip = peer_ipv6_ip
        if route_type is not None:
            self.route_type = route_type
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if update_time is not None:
            self.update_time = update_time
        if virtual_interface_id is not None:
            self.virtual_interface_id = virtual_interface_id
        if virtual_interface_name is not None:
            self.virtual_interface_name = virtual_interface_name
        if vlan_id is not None:
            self.vlan_id = vlan_id

    @property
    def account_id(self):
        """Gets the account_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The account_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param account_id: The account_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def bandwidth(self):
        """Gets the bandwidth of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The bandwidth of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param bandwidth: The bandwidth of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

    @property
    def bfd_detect_interval(self):
        """Gets the bfd_detect_interval of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The bfd_detect_interval of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: int
        """
        return self._bfd_detect_interval

    @bfd_detect_interval.setter
    def bfd_detect_interval(self, bfd_detect_interval):
        """Sets the bfd_detect_interval of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param bfd_detect_interval: The bfd_detect_interval of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: int
        """

        self._bfd_detect_interval = bfd_detect_interval

    @property
    def bfd_detect_multiplier(self):
        """Gets the bfd_detect_multiplier of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The bfd_detect_multiplier of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: int
        """
        return self._bfd_detect_multiplier

    @bfd_detect_multiplier.setter
    def bfd_detect_multiplier(self, bfd_detect_multiplier):
        """Sets the bfd_detect_multiplier of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param bfd_detect_multiplier: The bfd_detect_multiplier of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: int
        """

        self._bfd_detect_multiplier = bfd_detect_multiplier

    @property
    def creation_time(self):
        """Gets the creation_time of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The creation_time of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param creation_time: The creation_time of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The description of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param description: The description of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def direct_connect_connection_id(self):
        """Gets the direct_connect_connection_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The direct_connect_connection_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._direct_connect_connection_id

    @direct_connect_connection_id.setter
    def direct_connect_connection_id(self, direct_connect_connection_id):
        """Sets the direct_connect_connection_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param direct_connect_connection_id: The direct_connect_connection_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._direct_connect_connection_id = direct_connect_connection_id

    @property
    def direct_connect_gateway_id(self):
        """Gets the direct_connect_gateway_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The direct_connect_gateway_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._direct_connect_gateway_id

    @direct_connect_gateway_id.setter
    def direct_connect_gateway_id(self, direct_connect_gateway_id):
        """Sets the direct_connect_gateway_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param direct_connect_gateway_id: The direct_connect_gateway_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._direct_connect_gateway_id = direct_connect_gateway_id

    @property
    def enable_bfd(self):
        """Gets the enable_bfd of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The enable_bfd of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_bfd

    @enable_bfd.setter
    def enable_bfd(self, enable_bfd):
        """Sets the enable_bfd of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param enable_bfd: The enable_bfd of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: bool
        """

        self._enable_bfd = enable_bfd

    @property
    def enable_nqa(self):
        """Gets the enable_nqa of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The enable_nqa of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_nqa

    @enable_nqa.setter
    def enable_nqa(self, enable_nqa):
        """Sets the enable_nqa of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param enable_nqa: The enable_nqa of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: bool
        """

        self._enable_nqa = enable_nqa

    @property
    def local_ip(self):
        """Gets the local_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The local_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._local_ip

    @local_ip.setter
    def local_ip(self, local_ip):
        """Sets the local_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param local_ip: The local_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._local_ip = local_ip

    @property
    def local_ipv6_ip(self):
        """Gets the local_ipv6_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The local_ipv6_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._local_ipv6_ip

    @local_ipv6_ip.setter
    def local_ipv6_ip(self, local_ipv6_ip):
        """Sets the local_ipv6_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param local_ipv6_ip: The local_ipv6_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._local_ipv6_ip = local_ipv6_ip

    @property
    def nqa_detect_interval(self):
        """Gets the nqa_detect_interval of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The nqa_detect_interval of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: int
        """
        return self._nqa_detect_interval

    @nqa_detect_interval.setter
    def nqa_detect_interval(self, nqa_detect_interval):
        """Sets the nqa_detect_interval of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param nqa_detect_interval: The nqa_detect_interval of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: int
        """

        self._nqa_detect_interval = nqa_detect_interval

    @property
    def nqa_detect_multiplier(self):
        """Gets the nqa_detect_multiplier of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The nqa_detect_multiplier of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: int
        """
        return self._nqa_detect_multiplier

    @nqa_detect_multiplier.setter
    def nqa_detect_multiplier(self, nqa_detect_multiplier):
        """Sets the nqa_detect_multiplier of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param nqa_detect_multiplier: The nqa_detect_multiplier of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: int
        """

        self._nqa_detect_multiplier = nqa_detect_multiplier

    @property
    def peer_ip(self):
        """Gets the peer_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The peer_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._peer_ip

    @peer_ip.setter
    def peer_ip(self, peer_ip):
        """Sets the peer_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param peer_ip: The peer_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._peer_ip = peer_ip

    @property
    def peer_ipv6_ip(self):
        """Gets the peer_ipv6_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The peer_ipv6_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._peer_ipv6_ip

    @peer_ipv6_ip.setter
    def peer_ipv6_ip(self, peer_ipv6_ip):
        """Sets the peer_ipv6_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param peer_ipv6_ip: The peer_ipv6_ip of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._peer_ipv6_ip = peer_ipv6_ip

    @property
    def route_type(self):
        """Gets the route_type of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The route_type of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._route_type

    @route_type.setter
    def route_type(self, route_type):
        """Sets the route_type of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param route_type: The route_type of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._route_type = route_type

    @property
    def status(self):
        """Gets the status of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The status of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param status: The status of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The tags of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: list[TagForDescribeDirectConnectVirtualInterfacesOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param tags: The tags of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: list[TagForDescribeDirectConnectVirtualInterfacesOutput]
        """

        self._tags = tags

    @property
    def update_time(self):
        """Gets the update_time of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The update_time of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param update_time: The update_time of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def virtual_interface_id(self):
        """Gets the virtual_interface_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The virtual_interface_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._virtual_interface_id

    @virtual_interface_id.setter
    def virtual_interface_id(self, virtual_interface_id):
        """Sets the virtual_interface_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param virtual_interface_id: The virtual_interface_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._virtual_interface_id = virtual_interface_id

    @property
    def virtual_interface_name(self):
        """Gets the virtual_interface_name of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The virtual_interface_name of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._virtual_interface_name

    @virtual_interface_name.setter
    def virtual_interface_name(self, virtual_interface_name):
        """Sets the virtual_interface_name of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param virtual_interface_name: The virtual_interface_name of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: str
        """

        self._virtual_interface_name = virtual_interface_name

    @property
    def vlan_id(self):
        """Gets the vlan_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501


        :return: The vlan_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.


        :param vlan_id: The vlan_id of this VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput.  # noqa: E501
        :type: int
        """

        self._vlan_id = vlan_id

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
        if issubclass(VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput, dict):
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
        if not isinstance(other, VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualInterfaceForDescribeDirectConnectVirtualInterfacesOutput):
            return True

        return self.to_dict() != other.to_dict()
