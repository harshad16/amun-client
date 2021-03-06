# coding: utf-8

"""
    Amun API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.6.0-dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amun.swagger_client.configuration import Configuration


class InspectionStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'build': 'InspectionStatusBuild',
        'data_stored': 'bool',
        'workflow': 'dict(str, object)'
    }

    attribute_map = {
        'build': 'build',
        'data_stored': 'data_stored',
        'workflow': 'workflow'
    }

    def __init__(self, build=None, data_stored=None, workflow=None, local_vars_configuration=None):  # noqa: E501
        """InspectionStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._build = None
        self._data_stored = None
        self._workflow = None
        self.discriminator = None

        self.build = build
        self.data_stored = data_stored
        self.workflow = workflow

    @property
    def build(self):
        """Gets the build of this InspectionStatus.  # noqa: E501


        :return: The build of this InspectionStatus.  # noqa: E501
        :rtype: InspectionStatusBuild
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this InspectionStatus.


        :param build: The build of this InspectionStatus.  # noqa: E501
        :type: InspectionStatusBuild
        """
        if self.local_vars_configuration.client_side_validation and build is None:  # noqa: E501
            raise ValueError("Invalid value for `build`, must not be `None`")  # noqa: E501

        self._build = build

    @property
    def data_stored(self):
        """Gets the data_stored of this InspectionStatus.  # noqa: E501

        A flag checking if any data were stored.  # noqa: E501

        :return: The data_stored of this InspectionStatus.  # noqa: E501
        :rtype: bool
        """
        return self._data_stored

    @data_stored.setter
    def data_stored(self, data_stored):
        """Sets the data_stored of this InspectionStatus.

        A flag checking if any data were stored.  # noqa: E501

        :param data_stored: The data_stored of this InspectionStatus.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and data_stored is None:  # noqa: E501
            raise ValueError("Invalid value for `data_stored`, must not be `None`")  # noqa: E501

        self._data_stored = data_stored

    @property
    def workflow(self):
        """Gets the workflow of this InspectionStatus.  # noqa: E501

        Status of the submitted inspection Workflow.  # noqa: E501

        :return: The workflow of this InspectionStatus.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this InspectionStatus.

        Status of the submitted inspection Workflow.  # noqa: E501

        :param workflow: The workflow of this InspectionStatus.  # noqa: E501
        :type: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and workflow is None:  # noqa: E501
            raise ValueError("Invalid value for `workflow`, must not be `None`")  # noqa: E501

        self._workflow = workflow

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InspectionStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InspectionStatus):
            return True

        return self.to_dict() != other.to_dict()
