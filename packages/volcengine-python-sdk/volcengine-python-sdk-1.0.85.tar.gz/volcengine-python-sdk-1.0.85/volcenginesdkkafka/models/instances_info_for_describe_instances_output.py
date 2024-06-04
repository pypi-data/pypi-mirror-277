# coding: utf-8

"""
    kafka

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class InstancesInfoForDescribeInstancesOutput(object):
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
        'charge_detail': 'ChargeDetailForDescribeInstancesOutput',
        'compute_spec': 'str',
        'create_time': 'str',
        'eip_id': 'str',
        'instance_description': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'private_domain_on_public': 'bool',
        'project_name': 'str',
        'region_id': 'str',
        'storage_space': 'int',
        'storage_type': 'str',
        'subnet_id': 'str',
        'tags': 'TagsForDescribeInstancesOutput',
        'usable_group_number': 'int',
        'usable_partition_number': 'int',
        'used_group_number': 'int',
        'used_partition_number': 'int',
        'used_storage_space': 'int',
        'used_topic_number': 'int',
        'version': 'str',
        'vpc_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'charge_detail': 'ChargeDetail',
        'compute_spec': 'ComputeSpec',
        'create_time': 'CreateTime',
        'eip_id': 'EipId',
        'instance_description': 'InstanceDescription',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'instance_status': 'InstanceStatus',
        'private_domain_on_public': 'PrivateDomainOnPublic',
        'project_name': 'ProjectName',
        'region_id': 'RegionId',
        'storage_space': 'StorageSpace',
        'storage_type': 'StorageType',
        'subnet_id': 'SubnetId',
        'tags': 'Tags',
        'usable_group_number': 'UsableGroupNumber',
        'usable_partition_number': 'UsablePartitionNumber',
        'used_group_number': 'UsedGroupNumber',
        'used_partition_number': 'UsedPartitionNumber',
        'used_storage_space': 'UsedStorageSpace',
        'used_topic_number': 'UsedTopicNumber',
        'version': 'Version',
        'vpc_id': 'VpcId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, account_id=None, charge_detail=None, compute_spec=None, create_time=None, eip_id=None, instance_description=None, instance_id=None, instance_name=None, instance_status=None, private_domain_on_public=None, project_name=None, region_id=None, storage_space=None, storage_type=None, subnet_id=None, tags=None, usable_group_number=None, usable_partition_number=None, used_group_number=None, used_partition_number=None, used_storage_space=None, used_topic_number=None, version=None, vpc_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """InstancesInfoForDescribeInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._charge_detail = None
        self._compute_spec = None
        self._create_time = None
        self._eip_id = None
        self._instance_description = None
        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._private_domain_on_public = None
        self._project_name = None
        self._region_id = None
        self._storage_space = None
        self._storage_type = None
        self._subnet_id = None
        self._tags = None
        self._usable_group_number = None
        self._usable_partition_number = None
        self._used_group_number = None
        self._used_partition_number = None
        self._used_storage_space = None
        self._used_topic_number = None
        self._version = None
        self._vpc_id = None
        self._zone_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if charge_detail is not None:
            self.charge_detail = charge_detail
        if compute_spec is not None:
            self.compute_spec = compute_spec
        if create_time is not None:
            self.create_time = create_time
        if eip_id is not None:
            self.eip_id = eip_id
        if instance_description is not None:
            self.instance_description = instance_description
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if private_domain_on_public is not None:
            self.private_domain_on_public = private_domain_on_public
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
        if usable_group_number is not None:
            self.usable_group_number = usable_group_number
        if usable_partition_number is not None:
            self.usable_partition_number = usable_partition_number
        if used_group_number is not None:
            self.used_group_number = used_group_number
        if used_partition_number is not None:
            self.used_partition_number = used_partition_number
        if used_storage_space is not None:
            self.used_storage_space = used_storage_space
        if used_topic_number is not None:
            self.used_topic_number = used_topic_number
        if version is not None:
            self.version = version
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def account_id(self):
        """Gets the account_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The account_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InstancesInfoForDescribeInstancesOutput.


        :param account_id: The account_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def charge_detail(self):
        """Gets the charge_detail of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The charge_detail of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: ChargeDetailForDescribeInstancesOutput
        """
        return self._charge_detail

    @charge_detail.setter
    def charge_detail(self, charge_detail):
        """Sets the charge_detail of this InstancesInfoForDescribeInstancesOutput.


        :param charge_detail: The charge_detail of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: ChargeDetailForDescribeInstancesOutput
        """

        self._charge_detail = charge_detail

    @property
    def compute_spec(self):
        """Gets the compute_spec of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The compute_spec of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._compute_spec

    @compute_spec.setter
    def compute_spec(self, compute_spec):
        """Sets the compute_spec of this InstancesInfoForDescribeInstancesOutput.


        :param compute_spec: The compute_spec of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._compute_spec = compute_spec

    @property
    def create_time(self):
        """Gets the create_time of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The create_time of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this InstancesInfoForDescribeInstancesOutput.


        :param create_time: The create_time of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def eip_id(self):
        """Gets the eip_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The eip_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this InstancesInfoForDescribeInstancesOutput.


        :param eip_id: The eip_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._eip_id = eip_id

    @property
    def instance_description(self):
        """Gets the instance_description of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The instance_description of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_description

    @instance_description.setter
    def instance_description(self, instance_description):
        """Sets the instance_description of this InstancesInfoForDescribeInstancesOutput.


        :param instance_description: The instance_description of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_description = instance_description

    @property
    def instance_id(self):
        """Gets the instance_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The instance_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstancesInfoForDescribeInstancesOutput.


        :param instance_id: The instance_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The instance_name of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstancesInfoForDescribeInstancesOutput.


        :param instance_name: The instance_name of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def instance_status(self):
        """Gets the instance_status of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The instance_status of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this InstancesInfoForDescribeInstancesOutput.


        :param instance_status: The instance_status of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_status = instance_status

    @property
    def private_domain_on_public(self):
        """Gets the private_domain_on_public of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The private_domain_on_public of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._private_domain_on_public

    @private_domain_on_public.setter
    def private_domain_on_public(self, private_domain_on_public):
        """Sets the private_domain_on_public of this InstancesInfoForDescribeInstancesOutput.


        :param private_domain_on_public: The private_domain_on_public of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: bool
        """

        self._private_domain_on_public = private_domain_on_public

    @property
    def project_name(self):
        """Gets the project_name of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The project_name of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this InstancesInfoForDescribeInstancesOutput.


        :param project_name: The project_name of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The region_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this InstancesInfoForDescribeInstancesOutput.


        :param region_id: The region_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def storage_space(self):
        """Gets the storage_space of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The storage_space of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this InstancesInfoForDescribeInstancesOutput.


        :param storage_space: The storage_space of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._storage_space = storage_space

    @property
    def storage_type(self):
        """Gets the storage_type of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The storage_type of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this InstancesInfoForDescribeInstancesOutput.


        :param storage_type: The storage_type of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._storage_type = storage_type

    @property
    def subnet_id(self):
        """Gets the subnet_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The subnet_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this InstancesInfoForDescribeInstancesOutput.


        :param subnet_id: The subnet_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def tags(self):
        """Gets the tags of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The tags of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: TagsForDescribeInstancesOutput
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InstancesInfoForDescribeInstancesOutput.


        :param tags: The tags of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: TagsForDescribeInstancesOutput
        """

        self._tags = tags

    @property
    def usable_group_number(self):
        """Gets the usable_group_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The usable_group_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._usable_group_number

    @usable_group_number.setter
    def usable_group_number(self, usable_group_number):
        """Sets the usable_group_number of this InstancesInfoForDescribeInstancesOutput.


        :param usable_group_number: The usable_group_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._usable_group_number = usable_group_number

    @property
    def usable_partition_number(self):
        """Gets the usable_partition_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The usable_partition_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._usable_partition_number

    @usable_partition_number.setter
    def usable_partition_number(self, usable_partition_number):
        """Sets the usable_partition_number of this InstancesInfoForDescribeInstancesOutput.


        :param usable_partition_number: The usable_partition_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._usable_partition_number = usable_partition_number

    @property
    def used_group_number(self):
        """Gets the used_group_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The used_group_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._used_group_number

    @used_group_number.setter
    def used_group_number(self, used_group_number):
        """Sets the used_group_number of this InstancesInfoForDescribeInstancesOutput.


        :param used_group_number: The used_group_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._used_group_number = used_group_number

    @property
    def used_partition_number(self):
        """Gets the used_partition_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The used_partition_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._used_partition_number

    @used_partition_number.setter
    def used_partition_number(self, used_partition_number):
        """Sets the used_partition_number of this InstancesInfoForDescribeInstancesOutput.


        :param used_partition_number: The used_partition_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._used_partition_number = used_partition_number

    @property
    def used_storage_space(self):
        """Gets the used_storage_space of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The used_storage_space of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._used_storage_space

    @used_storage_space.setter
    def used_storage_space(self, used_storage_space):
        """Sets the used_storage_space of this InstancesInfoForDescribeInstancesOutput.


        :param used_storage_space: The used_storage_space of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._used_storage_space = used_storage_space

    @property
    def used_topic_number(self):
        """Gets the used_topic_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The used_topic_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._used_topic_number

    @used_topic_number.setter
    def used_topic_number(self, used_topic_number):
        """Sets the used_topic_number of this InstancesInfoForDescribeInstancesOutput.


        :param used_topic_number: The used_topic_number of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._used_topic_number = used_topic_number

    @property
    def version(self):
        """Gets the version of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The version of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstancesInfoForDescribeInstancesOutput.


        :param version: The version of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def vpc_id(self):
        """Gets the vpc_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The vpc_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this InstancesInfoForDescribeInstancesOutput.


        :param vpc_id: The vpc_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def zone_id(self):
        """Gets the zone_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501


        :return: The zone_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this InstancesInfoForDescribeInstancesOutput.


        :param zone_id: The zone_id of this InstancesInfoForDescribeInstancesOutput.  # noqa: E501
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
        if issubclass(InstancesInfoForDescribeInstancesOutput, dict):
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
        if not isinstance(other, InstancesInfoForDescribeInstancesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstancesInfoForDescribeInstancesOutput):
            return True

        return self.to_dict() != other.to_dict()
