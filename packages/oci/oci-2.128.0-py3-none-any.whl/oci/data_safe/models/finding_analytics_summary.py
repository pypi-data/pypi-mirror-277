# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FindingAnalyticsSummary(object):
    """
    The summary of information about the analytics data of findings or top findings.
    It includes details such as metric name, findinKey,
    title (topFindingCategory for top finding), severity (topFindingStatus for top finding) and targetId.
    """

    #: A constant which can be used with the metric_name property of a FindingAnalyticsSummary.
    #: This constant has a value of "TOP_FINDING_STATS"
    METRIC_NAME_TOP_FINDING_STATS = "TOP_FINDING_STATS"

    #: A constant which can be used with the metric_name property of a FindingAnalyticsSummary.
    #: This constant has a value of "FINDING_STATS"
    METRIC_NAME_FINDING_STATS = "FINDING_STATS"

    def __init__(self, **kwargs):
        """
        Initializes a new FindingAnalyticsSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this FindingAnalyticsSummary.
            Allowed values for this property are: "TOP_FINDING_STATS", "FINDING_STATS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_name: str

        :param dimensions:
            The value to assign to the dimensions property of this FindingAnalyticsSummary.
        :type dimensions: oci.data_safe.models.FindingAnalyticsDimensions

        :param count:
            The value to assign to the count property of this FindingAnalyticsSummary.
        :type count: int

        """
        self.swagger_types = {
            'metric_name': 'str',
            'dimensions': 'FindingAnalyticsDimensions',
            'count': 'int'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'dimensions': 'dimensions',
            'count': 'count'
        }

        self._metric_name = None
        self._dimensions = None
        self._count = None

    @property
    def metric_name(self):
        """
        **[Required]** Gets the metric_name of this FindingAnalyticsSummary.
        The name of the aggregation metric.

        Allowed values for this property are: "TOP_FINDING_STATS", "FINDING_STATS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The metric_name of this FindingAnalyticsSummary.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this FindingAnalyticsSummary.
        The name of the aggregation metric.


        :param metric_name: The metric_name of this FindingAnalyticsSummary.
        :type: str
        """
        allowed_values = ["TOP_FINDING_STATS", "FINDING_STATS"]
        if not value_allowed_none_or_none_sentinel(metric_name, allowed_values):
            metric_name = 'UNKNOWN_ENUM_VALUE'
        self._metric_name = metric_name

    @property
    def dimensions(self):
        """
        Gets the dimensions of this FindingAnalyticsSummary.

        :return: The dimensions of this FindingAnalyticsSummary.
        :rtype: oci.data_safe.models.FindingAnalyticsDimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this FindingAnalyticsSummary.

        :param dimensions: The dimensions of this FindingAnalyticsSummary.
        :type: oci.data_safe.models.FindingAnalyticsDimensions
        """
        self._dimensions = dimensions

    @property
    def count(self):
        """
        **[Required]** Gets the count of this FindingAnalyticsSummary.
        The total count for the aggregation metric.


        :return: The count of this FindingAnalyticsSummary.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this FindingAnalyticsSummary.
        The total count for the aggregation metric.


        :param count: The count of this FindingAnalyticsSummary.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
