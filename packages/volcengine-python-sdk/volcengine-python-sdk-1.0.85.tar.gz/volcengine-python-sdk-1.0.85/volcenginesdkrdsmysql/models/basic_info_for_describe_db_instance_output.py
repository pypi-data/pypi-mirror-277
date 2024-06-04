# coding: utf-8

"""
    rds_mysql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class BasicInfoForDescribeDBInstanceOutput(object):
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
        'charge_status': 'str',
        'charge_type': 'str',
        'create_time': 'str',
        'db_engine': 'str',
        'db_engine_version': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_spec': 'InstanceSpecForDescribeDBInstanceOutput',
        'instance_status': 'str',
        'instance_type': 'str',
        'read_only_instance_ids': 'list[str]',
        'region': 'str',
        'storage_space_gb': 'int',
        'update_time': 'str',
        'vpc_id': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'charge_status': 'ChargeStatus',
        'charge_type': 'ChargeType',
        'create_time': 'CreateTime',
        'db_engine': 'DBEngine',
        'db_engine_version': 'DBEngineVersion',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'instance_spec': 'InstanceSpec',
        'instance_status': 'InstanceStatus',
        'instance_type': 'InstanceType',
        'read_only_instance_ids': 'ReadOnlyInstanceIds',
        'region': 'Region',
        'storage_space_gb': 'StorageSpaceGB',
        'update_time': 'UpdateTime',
        'vpc_id': 'VpcID',
        'zone': 'Zone'
    }

    def __init__(self, charge_status=None, charge_type=None, create_time=None, db_engine=None, db_engine_version=None, instance_id=None, instance_name=None, instance_spec=None, instance_status=None, instance_type=None, read_only_instance_ids=None, region=None, storage_space_gb=None, update_time=None, vpc_id=None, zone=None, _configuration=None):  # noqa: E501
        """BasicInfoForDescribeDBInstanceOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._charge_status = None
        self._charge_type = None
        self._create_time = None
        self._db_engine = None
        self._db_engine_version = None
        self._instance_id = None
        self._instance_name = None
        self._instance_spec = None
        self._instance_status = None
        self._instance_type = None
        self._read_only_instance_ids = None
        self._region = None
        self._storage_space_gb = None
        self._update_time = None
        self._vpc_id = None
        self._zone = None
        self.discriminator = None

        if charge_status is not None:
            self.charge_status = charge_status
        if charge_type is not None:
            self.charge_type = charge_type
        if create_time is not None:
            self.create_time = create_time
        if db_engine is not None:
            self.db_engine = db_engine
        if db_engine_version is not None:
            self.db_engine_version = db_engine_version
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_spec is not None:
            self.instance_spec = instance_spec
        if instance_status is not None:
            self.instance_status = instance_status
        if instance_type is not None:
            self.instance_type = instance_type
        if read_only_instance_ids is not None:
            self.read_only_instance_ids = read_only_instance_ids
        if region is not None:
            self.region = region
        if storage_space_gb is not None:
            self.storage_space_gb = storage_space_gb
        if update_time is not None:
            self.update_time = update_time
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if zone is not None:
            self.zone = zone

    @property
    def charge_status(self):
        """Gets the charge_status of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The charge_status of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_status

    @charge_status.setter
    def charge_status(self, charge_status):
        """Sets the charge_status of this BasicInfoForDescribeDBInstanceOutput.


        :param charge_status: The charge_status of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """
        allowed_values = ["Normal", "Overdue", "Unpaid"]  # noqa: E501
        if (self._configuration.client_side_validation and
                charge_status not in allowed_values):
            raise ValueError(
                "Invalid value for `charge_status` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_status, allowed_values)
            )

        self._charge_status = charge_status

    @property
    def charge_type(self):
        """Gets the charge_type of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The charge_type of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this BasicInfoForDescribeDBInstanceOutput.


        :param charge_type: The charge_type of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotEnabled", "PostPaid", "Prepaid"]  # noqa: E501
        if (self._configuration.client_side_validation and
                charge_type not in allowed_values):
            raise ValueError(
                "Invalid value for `charge_type` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_type, allowed_values)
            )

        self._charge_type = charge_type

    @property
    def create_time(self):
        """Gets the create_time of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The create_time of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BasicInfoForDescribeDBInstanceOutput.


        :param create_time: The create_time of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def db_engine(self):
        """Gets the db_engine of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The db_engine of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_engine

    @db_engine.setter
    def db_engine(self, db_engine):
        """Sets the db_engine of this BasicInfoForDescribeDBInstanceOutput.


        :param db_engine: The db_engine of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """
        allowed_values = ["MySQL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                db_engine not in allowed_values):
            raise ValueError(
                "Invalid value for `db_engine` ({0}), must be one of {1}"  # noqa: E501
                .format(db_engine, allowed_values)
            )

        self._db_engine = db_engine

    @property
    def db_engine_version(self):
        """Gets the db_engine_version of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The db_engine_version of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_engine_version

    @db_engine_version.setter
    def db_engine_version(self, db_engine_version):
        """Sets the db_engine_version of this BasicInfoForDescribeDBInstanceOutput.


        :param db_engine_version: The db_engine_version of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """
        allowed_values = ["MySQL_8_0", "MySQL_Community_5_7"]  # noqa: E501
        if (self._configuration.client_side_validation and
                db_engine_version not in allowed_values):
            raise ValueError(
                "Invalid value for `db_engine_version` ({0}), must be one of {1}"  # noqa: E501
                .format(db_engine_version, allowed_values)
            )

        self._db_engine_version = db_engine_version

    @property
    def instance_id(self):
        """Gets the instance_id of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The instance_id of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BasicInfoForDescribeDBInstanceOutput.


        :param instance_id: The instance_id of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The instance_name of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this BasicInfoForDescribeDBInstanceOutput.


        :param instance_name: The instance_name of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def instance_spec(self):
        """Gets the instance_spec of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The instance_spec of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: InstanceSpecForDescribeDBInstanceOutput
        """
        return self._instance_spec

    @instance_spec.setter
    def instance_spec(self, instance_spec):
        """Sets the instance_spec of this BasicInfoForDescribeDBInstanceOutput.


        :param instance_spec: The instance_spec of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: InstanceSpecForDescribeDBInstanceOutput
        """

        self._instance_spec = instance_spec

    @property
    def instance_status(self):
        """Gets the instance_status of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The instance_status of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this BasicInfoForDescribeDBInstanceOutput.


        :param instance_status: The instance_status of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """
        allowed_values = ["AllowListMaintaining", "Closed", "Closing", "CreateFailed", "Creating", "Deleting", "Destroyed", "Destroying", "Error", "Importing", "Maintaining", "MasterChanging", "Migrating", "Reclaiming", "Recycled", "Released", "Restarting", "Restoring", "Resuming", "Running", "SSLUpdating", "TDEUpdating", "Unknown", "Updating", "Upgrading", "WaitingPaid"]  # noqa: E501
        if (self._configuration.client_side_validation and
                instance_status not in allowed_values):
            raise ValueError(
                "Invalid value for `instance_status` ({0}), must be one of {1}"  # noqa: E501
                .format(instance_status, allowed_values)
            )

        self._instance_status = instance_status

    @property
    def instance_type(self):
        """Gets the instance_type of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The instance_type of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this BasicInfoForDescribeDBInstanceOutput.


        :param instance_type: The instance_type of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """
        allowed_values = ["HA"]  # noqa: E501
        if (self._configuration.client_side_validation and
                instance_type not in allowed_values):
            raise ValueError(
                "Invalid value for `instance_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instance_type, allowed_values)
            )

        self._instance_type = instance_type

    @property
    def read_only_instance_ids(self):
        """Gets the read_only_instance_ids of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The read_only_instance_ids of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._read_only_instance_ids

    @read_only_instance_ids.setter
    def read_only_instance_ids(self, read_only_instance_ids):
        """Sets the read_only_instance_ids of this BasicInfoForDescribeDBInstanceOutput.


        :param read_only_instance_ids: The read_only_instance_ids of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: list[str]
        """

        self._read_only_instance_ids = read_only_instance_ids

    @property
    def region(self):
        """Gets the region of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The region of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this BasicInfoForDescribeDBInstanceOutput.


        :param region: The region of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def storage_space_gb(self):
        """Gets the storage_space_gb of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The storage_space_gb of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: int
        """
        return self._storage_space_gb

    @storage_space_gb.setter
    def storage_space_gb(self, storage_space_gb):
        """Sets the storage_space_gb of this BasicInfoForDescribeDBInstanceOutput.


        :param storage_space_gb: The storage_space_gb of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: int
        """

        self._storage_space_gb = storage_space_gb

    @property
    def update_time(self):
        """Gets the update_time of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The update_time of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this BasicInfoForDescribeDBInstanceOutput.


        :param update_time: The update_time of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def vpc_id(self):
        """Gets the vpc_id of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The vpc_id of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this BasicInfoForDescribeDBInstanceOutput.


        :param vpc_id: The vpc_id of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def zone(self):
        """Gets the zone of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501


        :return: The zone of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this BasicInfoForDescribeDBInstanceOutput.


        :param zone: The zone of this BasicInfoForDescribeDBInstanceOutput.  # noqa: E501
        :type: str
        """

        self._zone = zone

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
        if issubclass(BasicInfoForDescribeDBInstanceOutput, dict):
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
        if not isinstance(other, BasicInfoForDescribeDBInstanceOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasicInfoForDescribeDBInstanceOutput):
            return True

        return self.to_dict() != other.to_dict()
