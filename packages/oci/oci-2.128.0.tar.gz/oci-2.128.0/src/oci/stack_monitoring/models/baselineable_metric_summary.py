# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BaselineableMetricSummary(object):
    """
    Summary for the baseline-able metric
    """

    #: A constant which can be used with the lifecycle_state property of a BaselineableMetricSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a BaselineableMetricSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new BaselineableMetricSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BaselineableMetricSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BaselineableMetricSummary.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this BaselineableMetricSummary.
        :type tenancy_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BaselineableMetricSummary.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this BaselineableMetricSummary.
        :type name: str

        :param column:
            The value to assign to the column property of this BaselineableMetricSummary.
        :type column: str

        :param namespace:
            The value to assign to the namespace property of this BaselineableMetricSummary.
        :type namespace: str

        :param resource_group:
            The value to assign to the resource_group property of this BaselineableMetricSummary.
        :type resource_group: str

        :param is_out_of_box:
            The value to assign to the is_out_of_box property of this BaselineableMetricSummary.
        :type is_out_of_box: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BaselineableMetricSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BaselineableMetricSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this BaselineableMetricSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'lifecycle_state': 'str',
            'tenancy_id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'column': 'str',
            'namespace': 'str',
            'resource_group': 'str',
            'is_out_of_box': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'tenancy_id': 'tenancyId',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'column': 'column',
            'namespace': 'namespace',
            'resource_group': 'resourceGroup',
            'is_out_of_box': 'isOutOfBox',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._lifecycle_state = None
        self._tenancy_id = None
        self._compartment_id = None
        self._name = None
        self._column = None
        self._namespace = None
        self._resource_group = None
        self._is_out_of_box = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BaselineableMetricSummary.
        OCID of the metric


        :return: The id of this BaselineableMetricSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BaselineableMetricSummary.
        OCID of the metric


        :param id: The id of this BaselineableMetricSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this BaselineableMetricSummary.
        The current lifecycle state of the metric extension

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BaselineableMetricSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BaselineableMetricSummary.
        The current lifecycle state of the metric extension


        :param lifecycle_state: The lifecycle_state of this BaselineableMetricSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this BaselineableMetricSummary.
        OCID of the tenancy


        :return: The tenancy_id of this BaselineableMetricSummary.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this BaselineableMetricSummary.
        OCID of the tenancy


        :param tenancy_id: The tenancy_id of this BaselineableMetricSummary.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this BaselineableMetricSummary.
        OCID of the compartment


        :return: The compartment_id of this BaselineableMetricSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BaselineableMetricSummary.
        OCID of the compartment


        :param compartment_id: The compartment_id of this BaselineableMetricSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this BaselineableMetricSummary.
        name of the metric


        :return: The name of this BaselineableMetricSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BaselineableMetricSummary.
        name of the metric


        :param name: The name of this BaselineableMetricSummary.
        :type: str
        """
        self._name = name

    @property
    def column(self):
        """
        **[Required]** Gets the column of this BaselineableMetricSummary.
        metric column name


        :return: The column of this BaselineableMetricSummary.
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column):
        """
        Sets the column of this BaselineableMetricSummary.
        metric column name


        :param column: The column of this BaselineableMetricSummary.
        :type: str
        """
        self._column = column

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this BaselineableMetricSummary.
        namespace of the metric


        :return: The namespace of this BaselineableMetricSummary.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this BaselineableMetricSummary.
        namespace of the metric


        :param namespace: The namespace of this BaselineableMetricSummary.
        :type: str
        """
        self._namespace = namespace

    @property
    def resource_group(self):
        """
        **[Required]** Gets the resource_group of this BaselineableMetricSummary.
        Resource group of the metric


        :return: The resource_group of this BaselineableMetricSummary.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """
        Sets the resource_group of this BaselineableMetricSummary.
        Resource group of the metric


        :param resource_group: The resource_group of this BaselineableMetricSummary.
        :type: str
        """
        self._resource_group = resource_group

    @property
    def is_out_of_box(self):
        """
        **[Required]** Gets the is_out_of_box of this BaselineableMetricSummary.
        Is the metric created out of box, default false


        :return: The is_out_of_box of this BaselineableMetricSummary.
        :rtype: bool
        """
        return self._is_out_of_box

    @is_out_of_box.setter
    def is_out_of_box(self, is_out_of_box):
        """
        Sets the is_out_of_box of this BaselineableMetricSummary.
        Is the metric created out of box, default false


        :param is_out_of_box: The is_out_of_box of this BaselineableMetricSummary.
        :type: bool
        """
        self._is_out_of_box = is_out_of_box

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BaselineableMetricSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this BaselineableMetricSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BaselineableMetricSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this BaselineableMetricSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BaselineableMetricSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this BaselineableMetricSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BaselineableMetricSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this BaselineableMetricSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this BaselineableMetricSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this BaselineableMetricSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this BaselineableMetricSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this BaselineableMetricSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
