# coding: utf-8

"""
    storage_ebs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateVolumeRequest(object):
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
        'client_token': 'str',
        'description': 'str',
        'instance_id': 'str',
        'kind': 'str',
        'project_name': 'str',
        'size': 'str',
        'snapshot_id': 'str',
        'tags': 'list[TagForCreateVolumeInput]',
        'volume_charge_type': 'str',
        'volume_name': 'str',
        'volume_type': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'description': 'Description',
        'instance_id': 'InstanceId',
        'kind': 'Kind',
        'project_name': 'ProjectName',
        'size': 'Size',
        'snapshot_id': 'SnapshotId',
        'tags': 'Tags',
        'volume_charge_type': 'VolumeChargeType',
        'volume_name': 'VolumeName',
        'volume_type': 'VolumeType',
        'zone_id': 'ZoneId'
    }

    def __init__(self, client_token=None, description=None, instance_id=None, kind=None, project_name=None, size=None, snapshot_id=None, tags=None, volume_charge_type=None, volume_name=None, volume_type=None, zone_id=None, _configuration=None):  # noqa: E501
        """CreateVolumeRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._description = None
        self._instance_id = None
        self._kind = None
        self._project_name = None
        self._size = None
        self._snapshot_id = None
        self._tags = None
        self._volume_charge_type = None
        self._volume_name = None
        self._volume_type = None
        self._zone_id = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        if instance_id is not None:
            self.instance_id = instance_id
        if kind is not None:
            self.kind = kind
        if project_name is not None:
            self.project_name = project_name
        self.size = size
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        if tags is not None:
            self.tags = tags
        if volume_charge_type is not None:
            self.volume_charge_type = volume_charge_type
        self.volume_name = volume_name
        self.volume_type = volume_type
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def client_token(self):
        """Gets the client_token of this CreateVolumeRequest.  # noqa: E501


        :return: The client_token of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateVolumeRequest.


        :param client_token: The client_token of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this CreateVolumeRequest.  # noqa: E501


        :return: The description of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateVolumeRequest.


        :param description: The description of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateVolumeRequest.  # noqa: E501


        :return: The instance_id of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateVolumeRequest.


        :param instance_id: The instance_id of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def kind(self):
        """Gets the kind of this CreateVolumeRequest.  # noqa: E501


        :return: The kind of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this CreateVolumeRequest.


        :param kind: The kind of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def project_name(self):
        """Gets the project_name of this CreateVolumeRequest.  # noqa: E501


        :return: The project_name of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateVolumeRequest.


        :param project_name: The project_name of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def size(self):
        """Gets the size of this CreateVolumeRequest.  # noqa: E501


        :return: The size of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateVolumeRequest.


        :param size: The size of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this CreateVolumeRequest.  # noqa: E501


        :return: The snapshot_id of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this CreateVolumeRequest.


        :param snapshot_id: The snapshot_id of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._snapshot_id = snapshot_id

    @property
    def tags(self):
        """Gets the tags of this CreateVolumeRequest.  # noqa: E501


        :return: The tags of this CreateVolumeRequest.  # noqa: E501
        :rtype: list[TagForCreateVolumeInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateVolumeRequest.


        :param tags: The tags of this CreateVolumeRequest.  # noqa: E501
        :type: list[TagForCreateVolumeInput]
        """

        self._tags = tags

    @property
    def volume_charge_type(self):
        """Gets the volume_charge_type of this CreateVolumeRequest.  # noqa: E501


        :return: The volume_charge_type of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_charge_type

    @volume_charge_type.setter
    def volume_charge_type(self, volume_charge_type):
        """Sets the volume_charge_type of this CreateVolumeRequest.


        :param volume_charge_type: The volume_charge_type of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """

        self._volume_charge_type = volume_charge_type

    @property
    def volume_name(self):
        """Gets the volume_name of this CreateVolumeRequest.  # noqa: E501


        :return: The volume_name of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this CreateVolumeRequest.


        :param volume_name: The volume_name of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and volume_name is None:
            raise ValueError("Invalid value for `volume_name`, must not be `None`")  # noqa: E501

        self._volume_name = volume_name

    @property
    def volume_type(self):
        """Gets the volume_type of this CreateVolumeRequest.  # noqa: E501


        :return: The volume_type of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this CreateVolumeRequest.


        :param volume_type: The volume_type of this CreateVolumeRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and volume_type is None:
            raise ValueError("Invalid value for `volume_type`, must not be `None`")  # noqa: E501

        self._volume_type = volume_type

    @property
    def zone_id(self):
        """Gets the zone_id of this CreateVolumeRequest.  # noqa: E501


        :return: The zone_id of this CreateVolumeRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this CreateVolumeRequest.


        :param zone_id: The zone_id of this CreateVolumeRequest.  # noqa: E501
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
        if issubclass(CreateVolumeRequest, dict):
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
        if not isinstance(other, CreateVolumeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateVolumeRequest):
            return True

        return self.to_dict() != other.to_dict()
