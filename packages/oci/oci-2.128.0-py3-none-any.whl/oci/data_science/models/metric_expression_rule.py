# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetricExpressionRule(object):
    """
    The metric expression rule base.
    """

    #: A constant which can be used with the metric_expression_rule_type property of a MetricExpressionRule.
    #: This constant has a value of "PREDEFINED_EXPRESSION"
    METRIC_EXPRESSION_RULE_TYPE_PREDEFINED_EXPRESSION = "PREDEFINED_EXPRESSION"

    #: A constant which can be used with the metric_expression_rule_type property of a MetricExpressionRule.
    #: This constant has a value of "CUSTOM_EXPRESSION"
    METRIC_EXPRESSION_RULE_TYPE_CUSTOM_EXPRESSION = "CUSTOM_EXPRESSION"

    def __init__(self, **kwargs):
        """
        Initializes a new MetricExpressionRule object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_science.models.PredefinedMetricExpressionRule`
        * :class:`~oci.data_science.models.CustomMetricExpressionRule`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_expression_rule_type:
            The value to assign to the metric_expression_rule_type property of this MetricExpressionRule.
            Allowed values for this property are: "PREDEFINED_EXPRESSION", "CUSTOM_EXPRESSION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_expression_rule_type: str

        """
        self.swagger_types = {
            'metric_expression_rule_type': 'str'
        }

        self.attribute_map = {
            'metric_expression_rule_type': 'metricExpressionRuleType'
        }

        self._metric_expression_rule_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['metricExpressionRuleType']

        if type == 'PREDEFINED_EXPRESSION':
            return 'PredefinedMetricExpressionRule'

        if type == 'CUSTOM_EXPRESSION':
            return 'CustomMetricExpressionRule'
        else:
            return 'MetricExpressionRule'

    @property
    def metric_expression_rule_type(self):
        """
        **[Required]** Gets the metric_expression_rule_type of this MetricExpressionRule.
        The metric expression for creating the alarm used to trigger autoscaling actions on the model deployment.

        The following values are supported:

        * `PREDEFINED_EXPRESSION`: An expression built using CPU or Memory metrics emitted by the Model Deployment Monitoring.

        * `CUSTOM_EXPRESSION`: A custom Monitoring Query Language (MQL) expression.

        Allowed values for this property are: "PREDEFINED_EXPRESSION", "CUSTOM_EXPRESSION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The metric_expression_rule_type of this MetricExpressionRule.
        :rtype: str
        """
        return self._metric_expression_rule_type

    @metric_expression_rule_type.setter
    def metric_expression_rule_type(self, metric_expression_rule_type):
        """
        Sets the metric_expression_rule_type of this MetricExpressionRule.
        The metric expression for creating the alarm used to trigger autoscaling actions on the model deployment.

        The following values are supported:

        * `PREDEFINED_EXPRESSION`: An expression built using CPU or Memory metrics emitted by the Model Deployment Monitoring.

        * `CUSTOM_EXPRESSION`: A custom Monitoring Query Language (MQL) expression.


        :param metric_expression_rule_type: The metric_expression_rule_type of this MetricExpressionRule.
        :type: str
        """
        allowed_values = ["PREDEFINED_EXPRESSION", "CUSTOM_EXPRESSION"]
        if not value_allowed_none_or_none_sentinel(metric_expression_rule_type, allowed_values):
            metric_expression_rule_type = 'UNKNOWN_ENUM_VALUE'
        self._metric_expression_rule_type = metric_expression_rule_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
