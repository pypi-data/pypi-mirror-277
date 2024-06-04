# coding: utf-8

"""
    redis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class InstanceForDescribeDBInstancesOutput(object):
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
        'capacity': 'CapacityForDescribeDBInstancesOutput',
        'charge_type': 'str',
        'create_time': 'str',
        'deletion_protection': 'str',
        'engine_version': 'str',
        'expired_time': 'str',
        'instance_class': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'multi_az': 'str',
        'node_number': 'int',
        'project_name': 'str',
        'region_id': 'str',
        'service_type': 'str',
        'shard_capacity': 'float',
        'shard_number': 'int',
        'sharded_cluster': 'int',
        'status': 'str',
        'tags': 'list[TagForDescribeDBInstancesOutput]',
        'vpc_id': 'str',
        'zone_ids': 'list[str]'
    }

    attribute_map = {
        'capacity': 'Capacity',
        'charge_type': 'ChargeType',
        'create_time': 'CreateTime',
        'deletion_protection': 'DeletionProtection',
        'engine_version': 'EngineVersion',
        'expired_time': 'ExpiredTime',
        'instance_class': 'InstanceClass',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'multi_az': 'MultiAZ',
        'node_number': 'NodeNumber',
        'project_name': 'ProjectName',
        'region_id': 'RegionId',
        'service_type': 'ServiceType',
        'shard_capacity': 'ShardCapacity',
        'shard_number': 'ShardNumber',
        'sharded_cluster': 'ShardedCluster',
        'status': 'Status',
        'tags': 'Tags',
        'vpc_id': 'VpcId',
        'zone_ids': 'ZoneIds'
    }

    def __init__(self, capacity=None, charge_type=None, create_time=None, deletion_protection=None, engine_version=None, expired_time=None, instance_class=None, instance_id=None, instance_name=None, multi_az=None, node_number=None, project_name=None, region_id=None, service_type=None, shard_capacity=None, shard_number=None, sharded_cluster=None, status=None, tags=None, vpc_id=None, zone_ids=None, _configuration=None):  # noqa: E501
        """InstanceForDescribeDBInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._capacity = None
        self._charge_type = None
        self._create_time = None
        self._deletion_protection = None
        self._engine_version = None
        self._expired_time = None
        self._instance_class = None
        self._instance_id = None
        self._instance_name = None
        self._multi_az = None
        self._node_number = None
        self._project_name = None
        self._region_id = None
        self._service_type = None
        self._shard_capacity = None
        self._shard_number = None
        self._sharded_cluster = None
        self._status = None
        self._tags = None
        self._vpc_id = None
        self._zone_ids = None
        self.discriminator = None

        if capacity is not None:
            self.capacity = capacity
        if charge_type is not None:
            self.charge_type = charge_type
        if create_time is not None:
            self.create_time = create_time
        if deletion_protection is not None:
            self.deletion_protection = deletion_protection
        if engine_version is not None:
            self.engine_version = engine_version
        if expired_time is not None:
            self.expired_time = expired_time
        if instance_class is not None:
            self.instance_class = instance_class
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if multi_az is not None:
            self.multi_az = multi_az
        if node_number is not None:
            self.node_number = node_number
        if project_name is not None:
            self.project_name = project_name
        if region_id is not None:
            self.region_id = region_id
        if service_type is not None:
            self.service_type = service_type
        if shard_capacity is not None:
            self.shard_capacity = shard_capacity
        if shard_number is not None:
            self.shard_number = shard_number
        if sharded_cluster is not None:
            self.sharded_cluster = sharded_cluster
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if zone_ids is not None:
            self.zone_ids = zone_ids

    @property
    def capacity(self):
        """Gets the capacity of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The capacity of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: CapacityForDescribeDBInstancesOutput
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this InstanceForDescribeDBInstancesOutput.


        :param capacity: The capacity of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: CapacityForDescribeDBInstancesOutput
        """

        self._capacity = capacity

    @property
    def charge_type(self):
        """Gets the charge_type of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The charge_type of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this InstanceForDescribeDBInstancesOutput.


        :param charge_type: The charge_type of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def create_time(self):
        """Gets the create_time of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The create_time of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this InstanceForDescribeDBInstancesOutput.


        :param create_time: The create_time of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def deletion_protection(self):
        """Gets the deletion_protection of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The deletion_protection of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._deletion_protection

    @deletion_protection.setter
    def deletion_protection(self, deletion_protection):
        """Sets the deletion_protection of this InstanceForDescribeDBInstancesOutput.


        :param deletion_protection: The deletion_protection of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._deletion_protection = deletion_protection

    @property
    def engine_version(self):
        """Gets the engine_version of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The engine_version of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this InstanceForDescribeDBInstancesOutput.


        :param engine_version: The engine_version of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._engine_version = engine_version

    @property
    def expired_time(self):
        """Gets the expired_time of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The expired_time of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this InstanceForDescribeDBInstancesOutput.


        :param expired_time: The expired_time of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._expired_time = expired_time

    @property
    def instance_class(self):
        """Gets the instance_class of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The instance_class of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_class

    @instance_class.setter
    def instance_class(self, instance_class):
        """Sets the instance_class of this InstanceForDescribeDBInstancesOutput.


        :param instance_class: The instance_class of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_class = instance_class

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The instance_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceForDescribeDBInstancesOutput.


        :param instance_id: The instance_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The instance_name of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstanceForDescribeDBInstancesOutput.


        :param instance_name: The instance_name of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def multi_az(self):
        """Gets the multi_az of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The multi_az of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._multi_az

    @multi_az.setter
    def multi_az(self, multi_az):
        """Sets the multi_az of this InstanceForDescribeDBInstancesOutput.


        :param multi_az: The multi_az of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._multi_az = multi_az

    @property
    def node_number(self):
        """Gets the node_number of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The node_number of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._node_number

    @node_number.setter
    def node_number(self, node_number):
        """Sets the node_number of this InstanceForDescribeDBInstancesOutput.


        :param node_number: The node_number of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: int
        """

        self._node_number = node_number

    @property
    def project_name(self):
        """Gets the project_name of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The project_name of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this InstanceForDescribeDBInstancesOutput.


        :param project_name: The project_name of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The region_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this InstanceForDescribeDBInstancesOutput.


        :param region_id: The region_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def service_type(self):
        """Gets the service_type of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The service_type of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this InstanceForDescribeDBInstancesOutput.


        :param service_type: The service_type of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._service_type = service_type

    @property
    def shard_capacity(self):
        """Gets the shard_capacity of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The shard_capacity of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: float
        """
        return self._shard_capacity

    @shard_capacity.setter
    def shard_capacity(self, shard_capacity):
        """Sets the shard_capacity of this InstanceForDescribeDBInstancesOutput.


        :param shard_capacity: The shard_capacity of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: float
        """

        self._shard_capacity = shard_capacity

    @property
    def shard_number(self):
        """Gets the shard_number of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The shard_number of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._shard_number

    @shard_number.setter
    def shard_number(self, shard_number):
        """Sets the shard_number of this InstanceForDescribeDBInstancesOutput.


        :param shard_number: The shard_number of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: int
        """

        self._shard_number = shard_number

    @property
    def sharded_cluster(self):
        """Gets the sharded_cluster of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The sharded_cluster of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._sharded_cluster

    @sharded_cluster.setter
    def sharded_cluster(self, sharded_cluster):
        """Sets the sharded_cluster of this InstanceForDescribeDBInstancesOutput.


        :param sharded_cluster: The sharded_cluster of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: int
        """

        self._sharded_cluster = sharded_cluster

    @property
    def status(self):
        """Gets the status of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The status of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceForDescribeDBInstancesOutput.


        :param status: The status of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The tags of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: list[TagForDescribeDBInstancesOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InstanceForDescribeDBInstancesOutput.


        :param tags: The tags of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: list[TagForDescribeDBInstancesOutput]
        """

        self._tags = tags

    @property
    def vpc_id(self):
        """Gets the vpc_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The vpc_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this InstanceForDescribeDBInstancesOutput.


        :param vpc_id: The vpc_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def zone_ids(self):
        """Gets the zone_ids of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The zone_ids of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        """Sets the zone_ids of this InstanceForDescribeDBInstancesOutput.


        :param zone_ids: The zone_ids of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: list[str]
        """

        self._zone_ids = zone_ids

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
        if issubclass(InstanceForDescribeDBInstancesOutput, dict):
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
        if not isinstance(other, InstanceForDescribeDBInstancesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceForDescribeDBInstancesOutput):
            return True

        return self.to_dict() != other.to_dict()
