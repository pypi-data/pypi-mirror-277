# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizeOperationsInsightsWarehouseResourceUsageAggregation(object):
    """
    Details of resource usage by an Operations Insights Warehouse resource.
    """

    #: A constant which can be used with the lifecycle_state property of a SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizeOperationsInsightsWarehouseResourceUsageAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        :type id: str

        :param cpu_used:
            The value to assign to the cpu_used property of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        :type cpu_used: float

        :param storage_used_in_gbs:
            The value to assign to the storage_used_in_gbs property of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        :type storage_used_in_gbs: float

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'cpu_used': 'float',
            'storage_used_in_gbs': 'float',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'cpu_used': 'cpuUsed',
            'storage_used_in_gbs': 'storageUsedInGBs',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._cpu_used = None
        self._storage_used_in_gbs = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        OPSI Warehouse OCID


        :return: The id of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        OPSI Warehouse OCID


        :param id: The id of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        :type: str
        """
        self._id = id

    @property
    def cpu_used(self):
        """
        Gets the cpu_used of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        Number of OCPUs used by OPSI Warehouse ADW. Can be fractional.


        :return: The cpu_used of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        :rtype: float
        """
        return self._cpu_used

    @cpu_used.setter
    def cpu_used(self, cpu_used):
        """
        Sets the cpu_used of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        Number of OCPUs used by OPSI Warehouse ADW. Can be fractional.


        :param cpu_used: The cpu_used of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        :type: float
        """
        self._cpu_used = cpu_used

    @property
    def storage_used_in_gbs(self):
        """
        Gets the storage_used_in_gbs of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        Storage by OPSI Warehouse ADW in GB.


        :return: The storage_used_in_gbs of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        :rtype: float
        """
        return self._storage_used_in_gbs

    @storage_used_in_gbs.setter
    def storage_used_in_gbs(self, storage_used_in_gbs):
        """
        Sets the storage_used_in_gbs of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        Storage by OPSI Warehouse ADW in GB.


        :param storage_used_in_gbs: The storage_used_in_gbs of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        :type: float
        """
        self._storage_used_in_gbs = storage_used_in_gbs

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        Possible lifecycle states

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        Possible lifecycle states


        :param lifecycle_state: The lifecycle_state of this SummarizeOperationsInsightsWarehouseResourceUsageAggregation.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
