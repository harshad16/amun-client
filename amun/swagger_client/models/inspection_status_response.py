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


class InspectionStatusResponse(object):
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
        'parameters': 'dict(str, object)',
        'status': 'InspectionStatus'
    }

    attribute_map = {
        'parameters': 'parameters',
        'status': 'status'
    }

    def __init__(self, parameters=None, status=None, local_vars_configuration=None):  # noqa: E501
        """InspectionStatusResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._parameters = None
        self._status = None
        self.discriminator = None

        self.parameters = parameters
        self.status = status

    @property
    def parameters(self):
        """Gets the parameters of this InspectionStatusResponse.  # noqa: E501

        Parameters echoed back to user for debugging.  # noqa: E501

        :return: The parameters of this InspectionStatusResponse.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this InspectionStatusResponse.

        Parameters echoed back to user for debugging.  # noqa: E501

        :param parameters: The parameters of this InspectionStatusResponse.  # noqa: E501
        :type: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    @property
    def status(self):
        """Gets the status of this InspectionStatusResponse.  # noqa: E501


        :return: The status of this InspectionStatusResponse.  # noqa: E501
        :rtype: InspectionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InspectionStatusResponse.


        :param status: The status of this InspectionStatusResponse.  # noqa: E501
        :type: InspectionStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, InspectionStatusResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InspectionStatusResponse):
            return True

        return self.to_dict() != other.to_dict()
