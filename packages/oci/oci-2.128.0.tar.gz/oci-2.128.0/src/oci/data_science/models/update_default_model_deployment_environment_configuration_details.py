# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .update_model_deployment_environment_configuration_details import UpdateModelDeploymentEnvironmentConfigurationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDefaultModelDeploymentEnvironmentConfigurationDetails(UpdateModelDeploymentEnvironmentConfigurationDetails):
    """
    The update environment configuration details object for managed container
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDefaultModelDeploymentEnvironmentConfigurationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.UpdateDefaultModelDeploymentEnvironmentConfigurationDetails.environment_configuration_type` attribute
        of this class is ``DEFAULT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param environment_configuration_type:
            The value to assign to the environment_configuration_type property of this UpdateDefaultModelDeploymentEnvironmentConfigurationDetails.
            Allowed values for this property are: "DEFAULT", "OCIR_CONTAINER"
        :type environment_configuration_type: str

        :param environment_variables:
            The value to assign to the environment_variables property of this UpdateDefaultModelDeploymentEnvironmentConfigurationDetails.
        :type environment_variables: dict(str, str)

        """
        self.swagger_types = {
            'environment_configuration_type': 'str',
            'environment_variables': 'dict(str, str)'
        }

        self.attribute_map = {
            'environment_configuration_type': 'environmentConfigurationType',
            'environment_variables': 'environmentVariables'
        }

        self._environment_configuration_type = None
        self._environment_variables = None
        self._environment_configuration_type = 'DEFAULT'

    @property
    def environment_variables(self):
        """
        Gets the environment_variables of this UpdateDefaultModelDeploymentEnvironmentConfigurationDetails.
        Environment variables to set for the web server container.
        The size of envVars must be less than 2048 bytes.
        Key should be under 32 characters.
        Key should contain only letters, digits and underscore (_)
        Key should start with a letter.
        Key should have at least 2 characters.
        Key should not end with underscore eg. `TEST_`
        Key if added cannot be empty. Value can be empty.
        No specific size limits on individual Values. But overall environment variables is limited to 2048 bytes.
        Key can't be reserved Model Deployment environment variables.


        :return: The environment_variables of this UpdateDefaultModelDeploymentEnvironmentConfigurationDetails.
        :rtype: dict(str, str)
        """
        return self._environment_variables

    @environment_variables.setter
    def environment_variables(self, environment_variables):
        """
        Sets the environment_variables of this UpdateDefaultModelDeploymentEnvironmentConfigurationDetails.
        Environment variables to set for the web server container.
        The size of envVars must be less than 2048 bytes.
        Key should be under 32 characters.
        Key should contain only letters, digits and underscore (_)
        Key should start with a letter.
        Key should have at least 2 characters.
        Key should not end with underscore eg. `TEST_`
        Key if added cannot be empty. Value can be empty.
        No specific size limits on individual Values. But overall environment variables is limited to 2048 bytes.
        Key can't be reserved Model Deployment environment variables.


        :param environment_variables: The environment_variables of this UpdateDefaultModelDeploymentEnvironmentConfigurationDetails.
        :type: dict(str, str)
        """
        self._environment_variables = environment_variables

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
