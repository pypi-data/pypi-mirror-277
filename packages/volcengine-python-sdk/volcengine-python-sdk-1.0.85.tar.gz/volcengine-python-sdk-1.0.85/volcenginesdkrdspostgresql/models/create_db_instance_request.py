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


class CreateDBInstanceRequest(object):
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
        'charge_info': 'ChargeInfoForCreateDBInstanceInput',
        'db_engine_version': 'str',
        'instance_name': 'str',
        'node_info': 'list[NodeInfoForCreateDBInstanceInput]',
        'project_name': 'str',
        'storage_space': 'int',
        'storage_type': 'str',
        'subnet_id': 'str',
        'tags': 'list[TagForCreateDBInstanceInput]',
        'vpc_id': 'str'
    }

    attribute_map = {
        'charge_info': 'ChargeInfo',
        'db_engine_version': 'DBEngineVersion',
        'instance_name': 'InstanceName',
        'node_info': 'NodeInfo',
        'project_name': 'ProjectName',
        'storage_space': 'StorageSpace',
        'storage_type': 'StorageType',
        'subnet_id': 'SubnetId',
        'tags': 'Tags',
        'vpc_id': 'VpcId'
    }

    def __init__(self, charge_info=None, db_engine_version=None, instance_name=None, node_info=None, project_name=None, storage_space=None, storage_type=None, subnet_id=None, tags=None, vpc_id=None, _configuration=None):  # noqa: E501
        """CreateDBInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._charge_info = None
        self._db_engine_version = None
        self._instance_name = None
        self._node_info = None
        self._project_name = None
        self._storage_space = None
        self._storage_type = None
        self._subnet_id = None
        self._tags = None
        self._vpc_id = None
        self.discriminator = None

        if charge_info is not None:
            self.charge_info = charge_info
        self.db_engine_version = db_engine_version
        if instance_name is not None:
            self.instance_name = instance_name
        if node_info is not None:
            self.node_info = node_info
        if project_name is not None:
            self.project_name = project_name
        if storage_space is not None:
            self.storage_space = storage_space
        self.storage_type = storage_type
        self.subnet_id = subnet_id
        if tags is not None:
            self.tags = tags
        self.vpc_id = vpc_id

    @property
    def charge_info(self):
        """Gets the charge_info of this CreateDBInstanceRequest.  # noqa: E501


        :return: The charge_info of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: ChargeInfoForCreateDBInstanceInput
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this CreateDBInstanceRequest.


        :param charge_info: The charge_info of this CreateDBInstanceRequest.  # noqa: E501
        :type: ChargeInfoForCreateDBInstanceInput
        """

        self._charge_info = charge_info

    @property
    def db_engine_version(self):
        """Gets the db_engine_version of this CreateDBInstanceRequest.  # noqa: E501


        :return: The db_engine_version of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_engine_version

    @db_engine_version.setter
    def db_engine_version(self, db_engine_version):
        """Sets the db_engine_version of this CreateDBInstanceRequest.


        :param db_engine_version: The db_engine_version of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and db_engine_version is None:
            raise ValueError("Invalid value for `db_engine_version`, must not be `None`")  # noqa: E501
        allowed_values = ["PostgreSQL_11", "PostgreSQL_12", "PostgreSQL_13"]  # noqa: E501
        if (self._configuration.client_side_validation and
                db_engine_version not in allowed_values):
            raise ValueError(
                "Invalid value for `db_engine_version` ({0}), must be one of {1}"  # noqa: E501
                .format(db_engine_version, allowed_values)
            )

        self._db_engine_version = db_engine_version

    @property
    def instance_name(self):
        """Gets the instance_name of this CreateDBInstanceRequest.  # noqa: E501


        :return: The instance_name of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this CreateDBInstanceRequest.


        :param instance_name: The instance_name of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def node_info(self):
        """Gets the node_info of this CreateDBInstanceRequest.  # noqa: E501


        :return: The node_info of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: list[NodeInfoForCreateDBInstanceInput]
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        """Sets the node_info of this CreateDBInstanceRequest.


        :param node_info: The node_info of this CreateDBInstanceRequest.  # noqa: E501
        :type: list[NodeInfoForCreateDBInstanceInput]
        """

        self._node_info = node_info

    @property
    def project_name(self):
        """Gets the project_name of this CreateDBInstanceRequest.  # noqa: E501


        :return: The project_name of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateDBInstanceRequest.


        :param project_name: The project_name of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def storage_space(self):
        """Gets the storage_space of this CreateDBInstanceRequest.  # noqa: E501


        :return: The storage_space of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this CreateDBInstanceRequest.


        :param storage_space: The storage_space of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                storage_space is not None and storage_space > 3000):  # noqa: E501
            raise ValueError("Invalid value for `storage_space`, must be a value less than or equal to `3000`")  # noqa: E501
        if (self._configuration.client_side_validation and
                storage_space is not None and storage_space < 20):  # noqa: E501
            raise ValueError("Invalid value for `storage_space`, must be a value greater than or equal to `20`")  # noqa: E501

        self._storage_space = storage_space

    @property
    def storage_type(self):
        """Gets the storage_type of this CreateDBInstanceRequest.  # noqa: E501


        :return: The storage_type of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this CreateDBInstanceRequest.


        :param storage_type: The storage_type of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and storage_type is None:
            raise ValueError("Invalid value for `storage_type`, must not be `None`")  # noqa: E501
        allowed_values = ["LocalSSD"]  # noqa: E501
        if (self._configuration.client_side_validation and
                storage_type not in allowed_values):
            raise ValueError(
                "Invalid value for `storage_type` ({0}), must be one of {1}"  # noqa: E501
                .format(storage_type, allowed_values)
            )

        self._storage_type = storage_type

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateDBInstanceRequest.  # noqa: E501


        :return: The subnet_id of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateDBInstanceRequest.


        :param subnet_id: The subnet_id of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subnet_id is None:
            raise ValueError("Invalid value for `subnet_id`, must not be `None`")  # noqa: E501

        self._subnet_id = subnet_id

    @property
    def tags(self):
        """Gets the tags of this CreateDBInstanceRequest.  # noqa: E501


        :return: The tags of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: list[TagForCreateDBInstanceInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateDBInstanceRequest.


        :param tags: The tags of this CreateDBInstanceRequest.  # noqa: E501
        :type: list[TagForCreateDBInstanceInput]
        """

        self._tags = tags

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateDBInstanceRequest.  # noqa: E501


        :return: The vpc_id of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateDBInstanceRequest.


        :param vpc_id: The vpc_id of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vpc_id is None:
            raise ValueError("Invalid value for `vpc_id`, must not be `None`")  # noqa: E501

        self._vpc_id = vpc_id

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
        if issubclass(CreateDBInstanceRequest, dict):
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
        if not isinstance(other, CreateDBInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDBInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()
