# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230801


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterPlacementGroupSummary(object):
    """
    A summary object that provides the metadata details of the cluster placement group.
    """

    #: A constant which can be used with the cluster_placement_group_type property of a ClusterPlacementGroupSummary.
    #: This constant has a value of "STANDARD"
    CLUSTER_PLACEMENT_GROUP_TYPE_STANDARD = "STANDARD"

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterPlacementGroupSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ClusterPlacementGroupSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this ClusterPlacementGroupSummary.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ClusterPlacementGroupSummary.
        :type compartment_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this ClusterPlacementGroupSummary.
        :type availability_domain: str

        :param cluster_placement_group_type:
            The value to assign to the cluster_placement_group_type property of this ClusterPlacementGroupSummary.
            Allowed values for this property are: "STANDARD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type cluster_placement_group_type: str

        :param time_created:
            The value to assign to the time_created property of this ClusterPlacementGroupSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ClusterPlacementGroupSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ClusterPlacementGroupSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ClusterPlacementGroupSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ClusterPlacementGroupSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ClusterPlacementGroupSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ClusterPlacementGroupSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'availability_domain': 'str',
            'cluster_placement_group_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'availability_domain': 'availabilityDomain',
            'cluster_placement_group_type': 'clusterPlacementGroupType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._availability_domain = None
        self._cluster_placement_group_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ClusterPlacementGroupSummary.
        The `OCID`__ of the cluster placement group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ClusterPlacementGroupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ClusterPlacementGroupSummary.
        The `OCID`__ of the cluster placement group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ClusterPlacementGroupSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ClusterPlacementGroupSummary.
        The friendly name of the cluster placement group.


        :return: The name of this ClusterPlacementGroupSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ClusterPlacementGroupSummary.
        The friendly name of the cluster placement group.


        :param name: The name of this ClusterPlacementGroupSummary.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ClusterPlacementGroupSummary.
        The `OCID`__ of the compartment that contains the cluster placement group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ClusterPlacementGroupSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ClusterPlacementGroupSummary.
        The `OCID`__ of the compartment that contains the cluster placement group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ClusterPlacementGroupSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this ClusterPlacementGroupSummary.
        The availability domain of the cluster placement group.


        :return: The availability_domain of this ClusterPlacementGroupSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ClusterPlacementGroupSummary.
        The availability domain of the cluster placement group.


        :param availability_domain: The availability_domain of this ClusterPlacementGroupSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def cluster_placement_group_type(self):
        """
        **[Required]** Gets the cluster_placement_group_type of this ClusterPlacementGroupSummary.
        The type of cluster placement group.

        Allowed values for this property are: "STANDARD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The cluster_placement_group_type of this ClusterPlacementGroupSummary.
        :rtype: str
        """
        return self._cluster_placement_group_type

    @cluster_placement_group_type.setter
    def cluster_placement_group_type(self, cluster_placement_group_type):
        """
        Sets the cluster_placement_group_type of this ClusterPlacementGroupSummary.
        The type of cluster placement group.


        :param cluster_placement_group_type: The cluster_placement_group_type of this ClusterPlacementGroupSummary.
        :type: str
        """
        allowed_values = ["STANDARD"]
        if not value_allowed_none_or_none_sentinel(cluster_placement_group_type, allowed_values):
            cluster_placement_group_type = 'UNKNOWN_ENUM_VALUE'
        self._cluster_placement_group_type = cluster_placement_group_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ClusterPlacementGroupSummary.
        The time the cluster placement group was created, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ClusterPlacementGroupSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ClusterPlacementGroupSummary.
        The time the cluster placement group was created, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ClusterPlacementGroupSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ClusterPlacementGroupSummary.
        The time the cluster placement group was updated, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ClusterPlacementGroupSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ClusterPlacementGroupSummary.
        The time the cluster placement group was updated, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ClusterPlacementGroupSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ClusterPlacementGroupSummary.
        The current state of the cluster placement group.


        :return: The lifecycle_state of this ClusterPlacementGroupSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ClusterPlacementGroupSummary.
        The current state of the cluster placement group.


        :param lifecycle_state: The lifecycle_state of this ClusterPlacementGroupSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ClusterPlacementGroupSummary.
        A message describing the current state in more detail. For example, lifecycle details for a resource in a Failed state might include information to act on.


        :return: The lifecycle_details of this ClusterPlacementGroupSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ClusterPlacementGroupSummary.
        A message describing the current state in more detail. For example, lifecycle details for a resource in a Failed state might include information to act on.


        :param lifecycle_details: The lifecycle_details of this ClusterPlacementGroupSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this ClusterPlacementGroupSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ClusterPlacementGroupSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ClusterPlacementGroupSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ClusterPlacementGroupSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this ClusterPlacementGroupSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ClusterPlacementGroupSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ClusterPlacementGroupSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ClusterPlacementGroupSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ClusterPlacementGroupSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ClusterPlacementGroupSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ClusterPlacementGroupSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ClusterPlacementGroupSummary.
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
