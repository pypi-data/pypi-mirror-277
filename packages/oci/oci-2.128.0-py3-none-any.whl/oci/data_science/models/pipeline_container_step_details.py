# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .pipeline_step_details import PipelineStepDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineContainerStepDetails(PipelineStepDetails):
    """
    The type of step where user provides the container details for an execution engine managed by the pipelines service.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineContainerStepDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.PipelineContainerStepDetails.step_type` attribute
        of this class is ``CONTAINER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_type:
            The value to assign to the step_type property of this PipelineContainerStepDetails.
            Allowed values for this property are: "ML_JOB", "CUSTOM_SCRIPT", "CONTAINER"
        :type step_type: str

        :param step_name:
            The value to assign to the step_name property of this PipelineContainerStepDetails.
        :type step_name: str

        :param description:
            The value to assign to the description property of this PipelineContainerStepDetails.
        :type description: str

        :param depends_on:
            The value to assign to the depends_on property of this PipelineContainerStepDetails.
        :type depends_on: list[str]

        :param step_configuration_details:
            The value to assign to the step_configuration_details property of this PipelineContainerStepDetails.
        :type step_configuration_details: oci.data_science.models.PipelineStepConfigurationDetails

        :param step_infrastructure_configuration_details:
            The value to assign to the step_infrastructure_configuration_details property of this PipelineContainerStepDetails.
        :type step_infrastructure_configuration_details: oci.data_science.models.PipelineInfrastructureConfigurationDetails

        :param step_container_configuration_details:
            The value to assign to the step_container_configuration_details property of this PipelineContainerStepDetails.
        :type step_container_configuration_details: oci.data_science.models.PipelineContainerConfigurationDetails

        :param is_artifact_uploaded:
            The value to assign to the is_artifact_uploaded property of this PipelineContainerStepDetails.
        :type is_artifact_uploaded: bool

        """
        self.swagger_types = {
            'step_type': 'str',
            'step_name': 'str',
            'description': 'str',
            'depends_on': 'list[str]',
            'step_configuration_details': 'PipelineStepConfigurationDetails',
            'step_infrastructure_configuration_details': 'PipelineInfrastructureConfigurationDetails',
            'step_container_configuration_details': 'PipelineContainerConfigurationDetails',
            'is_artifact_uploaded': 'bool'
        }

        self.attribute_map = {
            'step_type': 'stepType',
            'step_name': 'stepName',
            'description': 'description',
            'depends_on': 'dependsOn',
            'step_configuration_details': 'stepConfigurationDetails',
            'step_infrastructure_configuration_details': 'stepInfrastructureConfigurationDetails',
            'step_container_configuration_details': 'stepContainerConfigurationDetails',
            'is_artifact_uploaded': 'isArtifactUploaded'
        }

        self._step_type = None
        self._step_name = None
        self._description = None
        self._depends_on = None
        self._step_configuration_details = None
        self._step_infrastructure_configuration_details = None
        self._step_container_configuration_details = None
        self._is_artifact_uploaded = None
        self._step_type = 'CONTAINER'

    @property
    def step_infrastructure_configuration_details(self):
        """
        Gets the step_infrastructure_configuration_details of this PipelineContainerStepDetails.

        :return: The step_infrastructure_configuration_details of this PipelineContainerStepDetails.
        :rtype: oci.data_science.models.PipelineInfrastructureConfigurationDetails
        """
        return self._step_infrastructure_configuration_details

    @step_infrastructure_configuration_details.setter
    def step_infrastructure_configuration_details(self, step_infrastructure_configuration_details):
        """
        Sets the step_infrastructure_configuration_details of this PipelineContainerStepDetails.

        :param step_infrastructure_configuration_details: The step_infrastructure_configuration_details of this PipelineContainerStepDetails.
        :type: oci.data_science.models.PipelineInfrastructureConfigurationDetails
        """
        self._step_infrastructure_configuration_details = step_infrastructure_configuration_details

    @property
    def step_container_configuration_details(self):
        """
        **[Required]** Gets the step_container_configuration_details of this PipelineContainerStepDetails.

        :return: The step_container_configuration_details of this PipelineContainerStepDetails.
        :rtype: oci.data_science.models.PipelineContainerConfigurationDetails
        """
        return self._step_container_configuration_details

    @step_container_configuration_details.setter
    def step_container_configuration_details(self, step_container_configuration_details):
        """
        Sets the step_container_configuration_details of this PipelineContainerStepDetails.

        :param step_container_configuration_details: The step_container_configuration_details of this PipelineContainerStepDetails.
        :type: oci.data_science.models.PipelineContainerConfigurationDetails
        """
        self._step_container_configuration_details = step_container_configuration_details

    @property
    def is_artifact_uploaded(self):
        """
        Gets the is_artifact_uploaded of this PipelineContainerStepDetails.
        A flag to indicate whether the artifact has been uploaded for this step or not.


        :return: The is_artifact_uploaded of this PipelineContainerStepDetails.
        :rtype: bool
        """
        return self._is_artifact_uploaded

    @is_artifact_uploaded.setter
    def is_artifact_uploaded(self, is_artifact_uploaded):
        """
        Sets the is_artifact_uploaded of this PipelineContainerStepDetails.
        A flag to indicate whether the artifact has been uploaded for this step or not.


        :param is_artifact_uploaded: The is_artifact_uploaded of this PipelineContainerStepDetails.
        :type: bool
        """
        self._is_artifact_uploaded = is_artifact_uploaded

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
