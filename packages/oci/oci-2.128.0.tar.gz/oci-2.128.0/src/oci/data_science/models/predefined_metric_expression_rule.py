# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .metric_expression_rule import MetricExpressionRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PredefinedMetricExpressionRule(MetricExpressionRule):
    """
    An expression built using CPU or Memory metrics for triggering an autoscaling action on the model deployment.
    """

    #: A constant which can be used with the metric_type property of a PredefinedMetricExpressionRule.
    #: This constant has a value of "CPU_UTILIZATION"
    METRIC_TYPE_CPU_UTILIZATION = "CPU_UTILIZATION"

    #: A constant which can be used with the metric_type property of a PredefinedMetricExpressionRule.
    #: This constant has a value of "MEMORY_UTILIZATION"
    METRIC_TYPE_MEMORY_UTILIZATION = "MEMORY_UTILIZATION"

    def __init__(self, **kwargs):
        """
        Initializes a new PredefinedMetricExpressionRule object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.PredefinedMetricExpressionRule.metric_expression_rule_type` attribute
        of this class is ``PREDEFINED_EXPRESSION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_expression_rule_type:
            The value to assign to the metric_expression_rule_type property of this PredefinedMetricExpressionRule.
            Allowed values for this property are: "PREDEFINED_EXPRESSION", "CUSTOM_EXPRESSION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_expression_rule_type: str

        :param metric_type:
            The value to assign to the metric_type property of this PredefinedMetricExpressionRule.
            Allowed values for this property are: "CPU_UTILIZATION", "MEMORY_UTILIZATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_type: str

        :param scale_in_configuration:
            The value to assign to the scale_in_configuration property of this PredefinedMetricExpressionRule.
        :type scale_in_configuration: oci.data_science.models.PredefinedExpressionThresholdScalingConfiguration

        :param scale_out_configuration:
            The value to assign to the scale_out_configuration property of this PredefinedMetricExpressionRule.
        :type scale_out_configuration: oci.data_science.models.PredefinedExpressionThresholdScalingConfiguration

        """
        self.swagger_types = {
            'metric_expression_rule_type': 'str',
            'metric_type': 'str',
            'scale_in_configuration': 'PredefinedExpressionThresholdScalingConfiguration',
            'scale_out_configuration': 'PredefinedExpressionThresholdScalingConfiguration'
        }

        self.attribute_map = {
            'metric_expression_rule_type': 'metricExpressionRuleType',
            'metric_type': 'metricType',
            'scale_in_configuration': 'scaleInConfiguration',
            'scale_out_configuration': 'scaleOutConfiguration'
        }

        self._metric_expression_rule_type = None
        self._metric_type = None
        self._scale_in_configuration = None
        self._scale_out_configuration = None
        self._metric_expression_rule_type = 'PREDEFINED_EXPRESSION'

    @property
    def metric_type(self):
        """
        **[Required]** Gets the metric_type of this PredefinedMetricExpressionRule.
        Metric type

        Allowed values for this property are: "CPU_UTILIZATION", "MEMORY_UTILIZATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The metric_type of this PredefinedMetricExpressionRule.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """
        Sets the metric_type of this PredefinedMetricExpressionRule.
        Metric type


        :param metric_type: The metric_type of this PredefinedMetricExpressionRule.
        :type: str
        """
        allowed_values = ["CPU_UTILIZATION", "MEMORY_UTILIZATION"]
        if not value_allowed_none_or_none_sentinel(metric_type, allowed_values):
            metric_type = 'UNKNOWN_ENUM_VALUE'
        self._metric_type = metric_type

    @property
    def scale_in_configuration(self):
        """
        **[Required]** Gets the scale_in_configuration of this PredefinedMetricExpressionRule.

        :return: The scale_in_configuration of this PredefinedMetricExpressionRule.
        :rtype: oci.data_science.models.PredefinedExpressionThresholdScalingConfiguration
        """
        return self._scale_in_configuration

    @scale_in_configuration.setter
    def scale_in_configuration(self, scale_in_configuration):
        """
        Sets the scale_in_configuration of this PredefinedMetricExpressionRule.

        :param scale_in_configuration: The scale_in_configuration of this PredefinedMetricExpressionRule.
        :type: oci.data_science.models.PredefinedExpressionThresholdScalingConfiguration
        """
        self._scale_in_configuration = scale_in_configuration

    @property
    def scale_out_configuration(self):
        """
        **[Required]** Gets the scale_out_configuration of this PredefinedMetricExpressionRule.

        :return: The scale_out_configuration of this PredefinedMetricExpressionRule.
        :rtype: oci.data_science.models.PredefinedExpressionThresholdScalingConfiguration
        """
        return self._scale_out_configuration

    @scale_out_configuration.setter
    def scale_out_configuration(self, scale_out_configuration):
        """
        Sets the scale_out_configuration of this PredefinedMetricExpressionRule.

        :param scale_out_configuration: The scale_out_configuration of this PredefinedMetricExpressionRule.
        :type: oci.data_science.models.PredefinedExpressionThresholdScalingConfiguration
        """
        self._scale_out_configuration = scale_out_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
