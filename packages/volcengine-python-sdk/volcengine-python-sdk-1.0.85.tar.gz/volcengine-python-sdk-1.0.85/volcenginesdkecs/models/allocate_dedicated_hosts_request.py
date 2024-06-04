# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AllocateDedicatedHostsRequest(object):
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
        'auto_placement': 'str',
        'auto_renew': 'bool',
        'auto_renew_period': 'int',
        'charge_type': 'str',
        'client_token': 'str',
        'count': 'int',
        'cpu_overcommit_ratio': 'float',
        'dedicated_host_name': 'str',
        'dedicated_host_recovery': 'str',
        'dedicated_host_type_id': 'str',
        'description': 'str',
        'period': 'int',
        'period_unit': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'auto_placement': 'AutoPlacement',
        'auto_renew': 'AutoRenew',
        'auto_renew_period': 'AutoRenewPeriod',
        'charge_type': 'ChargeType',
        'client_token': 'ClientToken',
        'count': 'Count',
        'cpu_overcommit_ratio': 'CpuOvercommitRatio',
        'dedicated_host_name': 'DedicatedHostName',
        'dedicated_host_recovery': 'DedicatedHostRecovery',
        'dedicated_host_type_id': 'DedicatedHostTypeId',
        'description': 'Description',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'zone_id': 'ZoneId'
    }

    def __init__(self, auto_placement=None, auto_renew=None, auto_renew_period=None, charge_type=None, client_token=None, count=None, cpu_overcommit_ratio=None, dedicated_host_name=None, dedicated_host_recovery=None, dedicated_host_type_id=None, description=None, period=None, period_unit=None, zone_id=None, _configuration=None):  # noqa: E501
        """AllocateDedicatedHostsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_placement = None
        self._auto_renew = None
        self._auto_renew_period = None
        self._charge_type = None
        self._client_token = None
        self._count = None
        self._cpu_overcommit_ratio = None
        self._dedicated_host_name = None
        self._dedicated_host_recovery = None
        self._dedicated_host_type_id = None
        self._description = None
        self._period = None
        self._period_unit = None
        self._zone_id = None
        self.discriminator = None

        if auto_placement is not None:
            self.auto_placement = auto_placement
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if auto_renew_period is not None:
            self.auto_renew_period = auto_renew_period
        if charge_type is not None:
            self.charge_type = charge_type
        if client_token is not None:
            self.client_token = client_token
        if count is not None:
            self.count = count
        if cpu_overcommit_ratio is not None:
            self.cpu_overcommit_ratio = cpu_overcommit_ratio
        self.dedicated_host_name = dedicated_host_name
        if dedicated_host_recovery is not None:
            self.dedicated_host_recovery = dedicated_host_recovery
        self.dedicated_host_type_id = dedicated_host_type_id
        if description is not None:
            self.description = description
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit
        self.zone_id = zone_id

    @property
    def auto_placement(self):
        """Gets the auto_placement of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The auto_placement of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_placement

    @auto_placement.setter
    def auto_placement(self, auto_placement):
        """Sets the auto_placement of this AllocateDedicatedHostsRequest.


        :param auto_placement: The auto_placement of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: str
        """

        self._auto_placement = auto_placement

    @property
    def auto_renew(self):
        """Gets the auto_renew of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The auto_renew of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this AllocateDedicatedHostsRequest.


        :param auto_renew: The auto_renew of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def auto_renew_period(self):
        """Gets the auto_renew_period of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The auto_renew_period of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: int
        """
        return self._auto_renew_period

    @auto_renew_period.setter
    def auto_renew_period(self, auto_renew_period):
        """Sets the auto_renew_period of this AllocateDedicatedHostsRequest.


        :param auto_renew_period: The auto_renew_period of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: int
        """

        self._auto_renew_period = auto_renew_period

    @property
    def charge_type(self):
        """Gets the charge_type of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The charge_type of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this AllocateDedicatedHostsRequest.


        :param charge_type: The charge_type of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def client_token(self):
        """Gets the client_token of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The client_token of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this AllocateDedicatedHostsRequest.


        :param client_token: The client_token of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def count(self):
        """Gets the count of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The count of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AllocateDedicatedHostsRequest.


        :param count: The count of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def cpu_overcommit_ratio(self):
        """Gets the cpu_overcommit_ratio of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The cpu_overcommit_ratio of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: float
        """
        return self._cpu_overcommit_ratio

    @cpu_overcommit_ratio.setter
    def cpu_overcommit_ratio(self, cpu_overcommit_ratio):
        """Sets the cpu_overcommit_ratio of this AllocateDedicatedHostsRequest.


        :param cpu_overcommit_ratio: The cpu_overcommit_ratio of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: float
        """

        self._cpu_overcommit_ratio = cpu_overcommit_ratio

    @property
    def dedicated_host_name(self):
        """Gets the dedicated_host_name of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The dedicated_host_name of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_name

    @dedicated_host_name.setter
    def dedicated_host_name(self, dedicated_host_name):
        """Sets the dedicated_host_name of this AllocateDedicatedHostsRequest.


        :param dedicated_host_name: The dedicated_host_name of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and dedicated_host_name is None:
            raise ValueError("Invalid value for `dedicated_host_name`, must not be `None`")  # noqa: E501

        self._dedicated_host_name = dedicated_host_name

    @property
    def dedicated_host_recovery(self):
        """Gets the dedicated_host_recovery of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The dedicated_host_recovery of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_recovery

    @dedicated_host_recovery.setter
    def dedicated_host_recovery(self, dedicated_host_recovery):
        """Sets the dedicated_host_recovery of this AllocateDedicatedHostsRequest.


        :param dedicated_host_recovery: The dedicated_host_recovery of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: str
        """

        self._dedicated_host_recovery = dedicated_host_recovery

    @property
    def dedicated_host_type_id(self):
        """Gets the dedicated_host_type_id of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The dedicated_host_type_id of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_type_id

    @dedicated_host_type_id.setter
    def dedicated_host_type_id(self, dedicated_host_type_id):
        """Sets the dedicated_host_type_id of this AllocateDedicatedHostsRequest.


        :param dedicated_host_type_id: The dedicated_host_type_id of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and dedicated_host_type_id is None:
            raise ValueError("Invalid value for `dedicated_host_type_id`, must not be `None`")  # noqa: E501

        self._dedicated_host_type_id = dedicated_host_type_id

    @property
    def description(self):
        """Gets the description of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The description of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AllocateDedicatedHostsRequest.


        :param description: The description of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def period(self):
        """Gets the period of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The period of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this AllocateDedicatedHostsRequest.


        :param period: The period of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The period_unit of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this AllocateDedicatedHostsRequest.


        :param period_unit: The period_unit of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: str
        """

        self._period_unit = period_unit

    @property
    def zone_id(self):
        """Gets the zone_id of this AllocateDedicatedHostsRequest.  # noqa: E501


        :return: The zone_id of this AllocateDedicatedHostsRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this AllocateDedicatedHostsRequest.


        :param zone_id: The zone_id of this AllocateDedicatedHostsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and zone_id is None:
            raise ValueError("Invalid value for `zone_id`, must not be `None`")  # noqa: E501

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
        if issubclass(AllocateDedicatedHostsRequest, dict):
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
        if not isinstance(other, AllocateDedicatedHostsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllocateDedicatedHostsRequest):
            return True

        return self.to_dict() != other.to_dict()
