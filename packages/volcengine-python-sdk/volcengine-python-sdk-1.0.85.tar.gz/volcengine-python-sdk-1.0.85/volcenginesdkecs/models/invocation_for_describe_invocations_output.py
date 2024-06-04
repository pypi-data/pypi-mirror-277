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


class InvocationForDescribeInvocationsOutput(object):
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
        'command_content': 'str',
        'command_description': 'str',
        'command_id': 'str',
        'command_name': 'str',
        'command_provider': 'str',
        'command_type': 'str',
        'enable_parameter': 'bool',
        'end_time': 'str',
        'frequency': 'str',
        'instance_number': 'int',
        'invocation_description': 'str',
        'invocation_id': 'str',
        'invocation_name': 'str',
        'invocation_status': 'str',
        'launch_time': 'str',
        'parameter_definitions': 'list[ParameterDefinitionForDescribeInvocationsOutput]',
        'parameters': 'str',
        'recurrence_end_time': 'str',
        'repeat_mode': 'str',
        'start_time': 'str',
        'timeout': 'int',
        'username': 'str',
        'working_dir': 'str'
    }

    attribute_map = {
        'command_content': 'CommandContent',
        'command_description': 'CommandDescription',
        'command_id': 'CommandId',
        'command_name': 'CommandName',
        'command_provider': 'CommandProvider',
        'command_type': 'CommandType',
        'enable_parameter': 'EnableParameter',
        'end_time': 'EndTime',
        'frequency': 'Frequency',
        'instance_number': 'InstanceNumber',
        'invocation_description': 'InvocationDescription',
        'invocation_id': 'InvocationId',
        'invocation_name': 'InvocationName',
        'invocation_status': 'InvocationStatus',
        'launch_time': 'LaunchTime',
        'parameter_definitions': 'ParameterDefinitions',
        'parameters': 'Parameters',
        'recurrence_end_time': 'RecurrenceEndTime',
        'repeat_mode': 'RepeatMode',
        'start_time': 'StartTime',
        'timeout': 'Timeout',
        'username': 'Username',
        'working_dir': 'WorkingDir'
    }

    def __init__(self, command_content=None, command_description=None, command_id=None, command_name=None, command_provider=None, command_type=None, enable_parameter=None, end_time=None, frequency=None, instance_number=None, invocation_description=None, invocation_id=None, invocation_name=None, invocation_status=None, launch_time=None, parameter_definitions=None, parameters=None, recurrence_end_time=None, repeat_mode=None, start_time=None, timeout=None, username=None, working_dir=None, _configuration=None):  # noqa: E501
        """InvocationForDescribeInvocationsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._command_content = None
        self._command_description = None
        self._command_id = None
        self._command_name = None
        self._command_provider = None
        self._command_type = None
        self._enable_parameter = None
        self._end_time = None
        self._frequency = None
        self._instance_number = None
        self._invocation_description = None
        self._invocation_id = None
        self._invocation_name = None
        self._invocation_status = None
        self._launch_time = None
        self._parameter_definitions = None
        self._parameters = None
        self._recurrence_end_time = None
        self._repeat_mode = None
        self._start_time = None
        self._timeout = None
        self._username = None
        self._working_dir = None
        self.discriminator = None

        if command_content is not None:
            self.command_content = command_content
        if command_description is not None:
            self.command_description = command_description
        if command_id is not None:
            self.command_id = command_id
        if command_name is not None:
            self.command_name = command_name
        if command_provider is not None:
            self.command_provider = command_provider
        if command_type is not None:
            self.command_type = command_type
        if enable_parameter is not None:
            self.enable_parameter = enable_parameter
        if end_time is not None:
            self.end_time = end_time
        if frequency is not None:
            self.frequency = frequency
        if instance_number is not None:
            self.instance_number = instance_number
        if invocation_description is not None:
            self.invocation_description = invocation_description
        if invocation_id is not None:
            self.invocation_id = invocation_id
        if invocation_name is not None:
            self.invocation_name = invocation_name
        if invocation_status is not None:
            self.invocation_status = invocation_status
        if launch_time is not None:
            self.launch_time = launch_time
        if parameter_definitions is not None:
            self.parameter_definitions = parameter_definitions
        if parameters is not None:
            self.parameters = parameters
        if recurrence_end_time is not None:
            self.recurrence_end_time = recurrence_end_time
        if repeat_mode is not None:
            self.repeat_mode = repeat_mode
        if start_time is not None:
            self.start_time = start_time
        if timeout is not None:
            self.timeout = timeout
        if username is not None:
            self.username = username
        if working_dir is not None:
            self.working_dir = working_dir

    @property
    def command_content(self):
        """Gets the command_content of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The command_content of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._command_content

    @command_content.setter
    def command_content(self, command_content):
        """Sets the command_content of this InvocationForDescribeInvocationsOutput.


        :param command_content: The command_content of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._command_content = command_content

    @property
    def command_description(self):
        """Gets the command_description of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The command_description of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._command_description

    @command_description.setter
    def command_description(self, command_description):
        """Sets the command_description of this InvocationForDescribeInvocationsOutput.


        :param command_description: The command_description of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._command_description = command_description

    @property
    def command_id(self):
        """Gets the command_id of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The command_id of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this InvocationForDescribeInvocationsOutput.


        :param command_id: The command_id of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._command_id = command_id

    @property
    def command_name(self):
        """Gets the command_name of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The command_name of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """Sets the command_name of this InvocationForDescribeInvocationsOutput.


        :param command_name: The command_name of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._command_name = command_name

    @property
    def command_provider(self):
        """Gets the command_provider of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The command_provider of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._command_provider

    @command_provider.setter
    def command_provider(self, command_provider):
        """Sets the command_provider of this InvocationForDescribeInvocationsOutput.


        :param command_provider: The command_provider of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._command_provider = command_provider

    @property
    def command_type(self):
        """Gets the command_type of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The command_type of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """Sets the command_type of this InvocationForDescribeInvocationsOutput.


        :param command_type: The command_type of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._command_type = command_type

    @property
    def enable_parameter(self):
        """Gets the enable_parameter of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The enable_parameter of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_parameter

    @enable_parameter.setter
    def enable_parameter(self, enable_parameter):
        """Sets the enable_parameter of this InvocationForDescribeInvocationsOutput.


        :param enable_parameter: The enable_parameter of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: bool
        """

        self._enable_parameter = enable_parameter

    @property
    def end_time(self):
        """Gets the end_time of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The end_time of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InvocationForDescribeInvocationsOutput.


        :param end_time: The end_time of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def frequency(self):
        """Gets the frequency of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The frequency of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this InvocationForDescribeInvocationsOutput.


        :param frequency: The frequency of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._frequency = frequency

    @property
    def instance_number(self):
        """Gets the instance_number of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The instance_number of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: int
        """
        return self._instance_number

    @instance_number.setter
    def instance_number(self, instance_number):
        """Sets the instance_number of this InvocationForDescribeInvocationsOutput.


        :param instance_number: The instance_number of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: int
        """

        self._instance_number = instance_number

    @property
    def invocation_description(self):
        """Gets the invocation_description of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The invocation_description of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._invocation_description

    @invocation_description.setter
    def invocation_description(self, invocation_description):
        """Sets the invocation_description of this InvocationForDescribeInvocationsOutput.


        :param invocation_description: The invocation_description of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._invocation_description = invocation_description

    @property
    def invocation_id(self):
        """Gets the invocation_id of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The invocation_id of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._invocation_id

    @invocation_id.setter
    def invocation_id(self, invocation_id):
        """Sets the invocation_id of this InvocationForDescribeInvocationsOutput.


        :param invocation_id: The invocation_id of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._invocation_id = invocation_id

    @property
    def invocation_name(self):
        """Gets the invocation_name of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The invocation_name of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._invocation_name

    @invocation_name.setter
    def invocation_name(self, invocation_name):
        """Sets the invocation_name of this InvocationForDescribeInvocationsOutput.


        :param invocation_name: The invocation_name of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._invocation_name = invocation_name

    @property
    def invocation_status(self):
        """Gets the invocation_status of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The invocation_status of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._invocation_status

    @invocation_status.setter
    def invocation_status(self, invocation_status):
        """Sets the invocation_status of this InvocationForDescribeInvocationsOutput.


        :param invocation_status: The invocation_status of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._invocation_status = invocation_status

    @property
    def launch_time(self):
        """Gets the launch_time of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The launch_time of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._launch_time

    @launch_time.setter
    def launch_time(self, launch_time):
        """Sets the launch_time of this InvocationForDescribeInvocationsOutput.


        :param launch_time: The launch_time of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._launch_time = launch_time

    @property
    def parameter_definitions(self):
        """Gets the parameter_definitions of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The parameter_definitions of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: list[ParameterDefinitionForDescribeInvocationsOutput]
        """
        return self._parameter_definitions

    @parameter_definitions.setter
    def parameter_definitions(self, parameter_definitions):
        """Sets the parameter_definitions of this InvocationForDescribeInvocationsOutput.


        :param parameter_definitions: The parameter_definitions of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: list[ParameterDefinitionForDescribeInvocationsOutput]
        """

        self._parameter_definitions = parameter_definitions

    @property
    def parameters(self):
        """Gets the parameters of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The parameters of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this InvocationForDescribeInvocationsOutput.


        :param parameters: The parameters of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._parameters = parameters

    @property
    def recurrence_end_time(self):
        """Gets the recurrence_end_time of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The recurrence_end_time of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._recurrence_end_time

    @recurrence_end_time.setter
    def recurrence_end_time(self, recurrence_end_time):
        """Sets the recurrence_end_time of this InvocationForDescribeInvocationsOutput.


        :param recurrence_end_time: The recurrence_end_time of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._recurrence_end_time = recurrence_end_time

    @property
    def repeat_mode(self):
        """Gets the repeat_mode of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The repeat_mode of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._repeat_mode

    @repeat_mode.setter
    def repeat_mode(self, repeat_mode):
        """Sets the repeat_mode of this InvocationForDescribeInvocationsOutput.


        :param repeat_mode: The repeat_mode of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._repeat_mode = repeat_mode

    @property
    def start_time(self):
        """Gets the start_time of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The start_time of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InvocationForDescribeInvocationsOutput.


        :param start_time: The start_time of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def timeout(self):
        """Gets the timeout of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The timeout of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this InvocationForDescribeInvocationsOutput.


        :param timeout: The timeout of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def username(self):
        """Gets the username of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The username of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InvocationForDescribeInvocationsOutput.


        :param username: The username of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def working_dir(self):
        """Gets the working_dir of this InvocationForDescribeInvocationsOutput.  # noqa: E501


        :return: The working_dir of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """Sets the working_dir of this InvocationForDescribeInvocationsOutput.


        :param working_dir: The working_dir of this InvocationForDescribeInvocationsOutput.  # noqa: E501
        :type: str
        """

        self._working_dir = working_dir

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
        if issubclass(InvocationForDescribeInvocationsOutput, dict):
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
        if not isinstance(other, InvocationForDescribeInvocationsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvocationForDescribeInvocationsOutput):
            return True

        return self.to_dict() != other.to_dict()
