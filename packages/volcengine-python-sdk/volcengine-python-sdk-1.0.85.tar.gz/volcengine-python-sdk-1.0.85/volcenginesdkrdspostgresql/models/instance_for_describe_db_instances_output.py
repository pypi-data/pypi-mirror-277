# coding: utf-8

"""
    rds_postgresql

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
        'address_object': 'list[AddressObjectForDescribeDBInstancesOutput]',
        'allow_list_version': 'str',
        'charge_detail': 'ChargeDetailForDescribeDBInstancesOutput',
        'create_time': 'str',
        'db_engine_version': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'instance_type': 'str',
        'node_number': 'int',
        'node_spec': 'str',
        'project_name': 'str',
        'region_id': 'str',
        'storage_space': 'int',
        'storage_type': 'str',
        'subnet_id': 'str',
        'tags': 'list[TagForDescribeDBInstancesOutput]',
        'vpc_id': 'str',
        'zone_id': 'str',
        'zone_ids': 'list[str]'
    }

    attribute_map = {
        'address_object': 'AddressObject',
        'allow_list_version': 'AllowListVersion',
        'charge_detail': 'ChargeDetail',
        'create_time': 'CreateTime',
        'db_engine_version': 'DBEngineVersion',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'instance_status': 'InstanceStatus',
        'instance_type': 'InstanceType',
        'node_number': 'NodeNumber',
        'node_spec': 'NodeSpec',
        'project_name': 'ProjectName',
        'region_id': 'RegionId',
        'storage_space': 'StorageSpace',
        'storage_type': 'StorageType',
        'subnet_id': 'SubnetId',
        'tags': 'Tags',
        'vpc_id': 'VpcId',
        'zone_id': 'ZoneId',
        'zone_ids': 'ZoneIds'
    }

    def __init__(self, address_object=None, allow_list_version=None, charge_detail=None, create_time=None, db_engine_version=None, instance_id=None, instance_name=None, instance_status=None, instance_type=None, node_number=None, node_spec=None, project_name=None, region_id=None, storage_space=None, storage_type=None, subnet_id=None, tags=None, vpc_id=None, zone_id=None, zone_ids=None, _configuration=None):  # noqa: E501
        """InstanceForDescribeDBInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address_object = None
        self._allow_list_version = None
        self._charge_detail = None
        self._create_time = None
        self._db_engine_version = None
        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._instance_type = None
        self._node_number = None
        self._node_spec = None
        self._project_name = None
        self._region_id = None
        self._storage_space = None
        self._storage_type = None
        self._subnet_id = None
        self._tags = None
        self._vpc_id = None
        self._zone_id = None
        self._zone_ids = None
        self.discriminator = None

        if address_object is not None:
            self.address_object = address_object
        if allow_list_version is not None:
            self.allow_list_version = allow_list_version
        if charge_detail is not None:
            self.charge_detail = charge_detail
        if create_time is not None:
            self.create_time = create_time
        if db_engine_version is not None:
            self.db_engine_version = db_engine_version
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if instance_type is not None:
            self.instance_type = instance_type
        if node_number is not None:
            self.node_number = node_number
        if node_spec is not None:
            self.node_spec = node_spec
        if project_name is not None:
            self.project_name = project_name
        if region_id is not None:
            self.region_id = region_id
        if storage_space is not None:
            self.storage_space = storage_space
        if storage_type is not None:
            self.storage_type = storage_type
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if tags is not None:
            self.tags = tags
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if zone_id is not None:
            self.zone_id = zone_id
        if zone_ids is not None:
            self.zone_ids = zone_ids

    @property
    def address_object(self):
        """Gets the address_object of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The address_object of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: list[AddressObjectForDescribeDBInstancesOutput]
        """
        return self._address_object

    @address_object.setter
    def address_object(self, address_object):
        """Sets the address_object of this InstanceForDescribeDBInstancesOutput.


        :param address_object: The address_object of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: list[AddressObjectForDescribeDBInstancesOutput]
        """

        self._address_object = address_object

    @property
    def allow_list_version(self):
        """Gets the allow_list_version of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The allow_list_version of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._allow_list_version

    @allow_list_version.setter
    def allow_list_version(self, allow_list_version):
        """Sets the allow_list_version of this InstanceForDescribeDBInstancesOutput.


        :param allow_list_version: The allow_list_version of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._allow_list_version = allow_list_version

    @property
    def charge_detail(self):
        """Gets the charge_detail of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The charge_detail of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: ChargeDetailForDescribeDBInstancesOutput
        """
        return self._charge_detail

    @charge_detail.setter
    def charge_detail(self, charge_detail):
        """Sets the charge_detail of this InstanceForDescribeDBInstancesOutput.


        :param charge_detail: The charge_detail of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: ChargeDetailForDescribeDBInstancesOutput
        """

        self._charge_detail = charge_detail

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
    def db_engine_version(self):
        """Gets the db_engine_version of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The db_engine_version of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_engine_version

    @db_engine_version.setter
    def db_engine_version(self, db_engine_version):
        """Sets the db_engine_version of this InstanceForDescribeDBInstancesOutput.


        :param db_engine_version: The db_engine_version of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._db_engine_version = db_engine_version

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
    def instance_status(self):
        """Gets the instance_status of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The instance_status of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this InstanceForDescribeDBInstancesOutput.


        :param instance_status: The instance_status of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_status = instance_status

    @property
    def instance_type(self):
        """Gets the instance_type of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The instance_type of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this InstanceForDescribeDBInstancesOutput.


        :param instance_type: The instance_type of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

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
    def node_spec(self):
        """Gets the node_spec of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The node_spec of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._node_spec

    @node_spec.setter
    def node_spec(self, node_spec):
        """Sets the node_spec of this InstanceForDescribeDBInstancesOutput.


        :param node_spec: The node_spec of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._node_spec = node_spec

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
    def storage_space(self):
        """Gets the storage_space of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The storage_space of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this InstanceForDescribeDBInstancesOutput.


        :param storage_space: The storage_space of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: int
        """

        self._storage_space = storage_space

    @property
    def storage_type(self):
        """Gets the storage_type of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The storage_type of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this InstanceForDescribeDBInstancesOutput.


        :param storage_type: The storage_type of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._storage_type = storage_type

    @property
    def subnet_id(self):
        """Gets the subnet_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The subnet_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this InstanceForDescribeDBInstancesOutput.


        :param subnet_id: The subnet_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

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
    def zone_id(self):
        """Gets the zone_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501


        :return: The zone_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this InstanceForDescribeDBInstancesOutput.


        :param zone_id: The zone_id of this InstanceForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
