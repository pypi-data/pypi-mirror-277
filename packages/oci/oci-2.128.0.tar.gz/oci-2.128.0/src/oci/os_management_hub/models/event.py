# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Event(object):
    """
    An event is an occurrence of something of interest on a managed instance,
    such as a kernel crash, software package update, or software source
    update.
    """

    #: A constant which can be used with the type property of a Event.
    #: This constant has a value of "KERNEL_OOPS"
    TYPE_KERNEL_OOPS = "KERNEL_OOPS"

    #: A constant which can be used with the type property of a Event.
    #: This constant has a value of "KERNEL_CRASH"
    TYPE_KERNEL_CRASH = "KERNEL_CRASH"

    #: A constant which can be used with the type property of a Event.
    #: This constant has a value of "EXPLOIT_ATTEMPT"
    TYPE_EXPLOIT_ATTEMPT = "EXPLOIT_ATTEMPT"

    #: A constant which can be used with the type property of a Event.
    #: This constant has a value of "SOFTWARE_UPDATE"
    TYPE_SOFTWARE_UPDATE = "SOFTWARE_UPDATE"

    #: A constant which can be used with the type property of a Event.
    #: This constant has a value of "KSPLICE_UPDATE"
    TYPE_KSPLICE_UPDATE = "KSPLICE_UPDATE"

    #: A constant which can be used with the type property of a Event.
    #: This constant has a value of "SOFTWARE_SOURCE"
    TYPE_SOFTWARE_SOURCE = "SOFTWARE_SOURCE"

    #: A constant which can be used with the type property of a Event.
    #: This constant has a value of "AGENT"
    TYPE_AGENT = "AGENT"

    #: A constant which can be used with the type property of a Event.
    #: This constant has a value of "MANAGEMENT_STATION"
    TYPE_MANAGEMENT_STATION = "MANAGEMENT_STATION"

    #: A constant which can be used with the lifecycle_state property of a Event.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Event.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Event.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Event.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Event.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Event.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Event object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.os_management_hub.models.SoftwareUpdateEvent`
        * :class:`~oci.os_management_hub.models.KernelOopsEvent`
        * :class:`~oci.os_management_hub.models.ManagementStationEvent`
        * :class:`~oci.os_management_hub.models.SoftwareSourceEvent`
        * :class:`~oci.os_management_hub.models.KernelCrashEvent`
        * :class:`~oci.os_management_hub.models.ExploitAttemptEvent`
        * :class:`~oci.os_management_hub.models.AgentEvent`
        * :class:`~oci.os_management_hub.models.KspliceUpdateEvent`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Event.
        :type id: str

        :param type:
            The value to assign to the type property of this Event.
            Allowed values for this property are: "KERNEL_OOPS", "KERNEL_CRASH", "EXPLOIT_ATTEMPT", "SOFTWARE_UPDATE", "KSPLICE_UPDATE", "SOFTWARE_SOURCE", "AGENT", "MANAGEMENT_STATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param event_summary:
            The value to assign to the event_summary property of this Event.
        :type event_summary: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Event.
        :type compartment_id: str

        :param event_details:
            The value to assign to the event_details property of this Event.
        :type event_details: str

        :param resource_id:
            The value to assign to the resource_id property of this Event.
        :type resource_id: str

        :param system_details:
            The value to assign to the system_details property of this Event.
        :type system_details: oci.os_management_hub.models.SystemDetails

        :param time_occurred:
            The value to assign to the time_occurred property of this Event.
        :type time_occurred: datetime

        :param time_created:
            The value to assign to the time_created property of this Event.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Event.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Event.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Event.
        :type lifecycle_details: str

        :param is_managed_by_autonomous_linux:
            The value to assign to the is_managed_by_autonomous_linux property of this Event.
        :type is_managed_by_autonomous_linux: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Event.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Event.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Event.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'event_summary': 'str',
            'compartment_id': 'str',
            'event_details': 'str',
            'resource_id': 'str',
            'system_details': 'SystemDetails',
            'time_occurred': 'datetime',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'is_managed_by_autonomous_linux': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'event_summary': 'eventSummary',
            'compartment_id': 'compartmentId',
            'event_details': 'eventDetails',
            'resource_id': 'resourceId',
            'system_details': 'systemDetails',
            'time_occurred': 'timeOccurred',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'is_managed_by_autonomous_linux': 'isManagedByAutonomousLinux',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._type = None
        self._event_summary = None
        self._compartment_id = None
        self._event_details = None
        self._resource_id = None
        self._system_details = None
        self._time_occurred = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._is_managed_by_autonomous_linux = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'SOFTWARE_UPDATE':
            return 'SoftwareUpdateEvent'

        if type == 'KERNEL_OOPS':
            return 'KernelOopsEvent'

        if type == 'MANAGEMENT_STATION':
            return 'ManagementStationEvent'

        if type == 'SOFTWARE_SOURCE':
            return 'SoftwareSourceEvent'

        if type == 'KERNEL_CRASH':
            return 'KernelCrashEvent'

        if type == 'EXPLOIT_ATTEMPT':
            return 'ExploitAttemptEvent'

        if type == 'AGENT':
            return 'AgentEvent'

        if type == 'KSPLICE_UPDATE':
            return 'KspliceUpdateEvent'
        else:
            return 'Event'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Event.
        The `OCID`__ of the event.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Event.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Event.
        The `OCID`__ of the event.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Event.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Event.
        Event type:
          * `KERNEL_OOPS` - Used to identify a kernel panic condition event
          * `KERNEL_CRASH` - Used to identify an internal fatal kernel error that cannot be safely recovered from
          * `EXPLOIT_ATTEMPT` - Used to identify a known exploit detection as identified by Ksplice
          * `SOFTWARE_UPDATE` - Software updates - Packages
          * `KSPLICE_UPDATE` - Ksplice updates
          * `SOFTWARE_SOURCE` - Software source
          * `AGENT` - Agent
          * `MANAGEMENT_STATION` - Management Station

        Allowed values for this property are: "KERNEL_OOPS", "KERNEL_CRASH", "EXPLOIT_ATTEMPT", "SOFTWARE_UPDATE", "KSPLICE_UPDATE", "SOFTWARE_SOURCE", "AGENT", "MANAGEMENT_STATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Event.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Event.
        Event type:
          * `KERNEL_OOPS` - Used to identify a kernel panic condition event
          * `KERNEL_CRASH` - Used to identify an internal fatal kernel error that cannot be safely recovered from
          * `EXPLOIT_ATTEMPT` - Used to identify a known exploit detection as identified by Ksplice
          * `SOFTWARE_UPDATE` - Software updates - Packages
          * `KSPLICE_UPDATE` - Ksplice updates
          * `SOFTWARE_SOURCE` - Software source
          * `AGENT` - Agent
          * `MANAGEMENT_STATION` - Management Station


        :param type: The type of this Event.
        :type: str
        """
        allowed_values = ["KERNEL_OOPS", "KERNEL_CRASH", "EXPLOIT_ATTEMPT", "SOFTWARE_UPDATE", "KSPLICE_UPDATE", "SOFTWARE_SOURCE", "AGENT", "MANAGEMENT_STATION"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def event_summary(self):
        """
        **[Required]** Gets the event_summary of this Event.
        Summary of the event.


        :return: The event_summary of this Event.
        :rtype: str
        """
        return self._event_summary

    @event_summary.setter
    def event_summary(self, event_summary):
        """
        Sets the event_summary of this Event.
        Summary of the event.


        :param event_summary: The event_summary of this Event.
        :type: str
        """
        self._event_summary = event_summary

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Event.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Event.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Event.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Event.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def event_details(self):
        """
        Gets the event_details of this Event.
        Details of an event.


        :return: The event_details of this Event.
        :rtype: str
        """
        return self._event_details

    @event_details.setter
    def event_details(self, event_details):
        """
        Sets the event_details of this Event.
        Details of an event.


        :param event_details: The event_details of this Event.
        :type: str
        """
        self._event_details = event_details

    @property
    def resource_id(self):
        """
        Gets the resource_id of this Event.
        The `OCID`__ of the managed instance or resource where the event occurred.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The resource_id of this Event.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this Event.
        The `OCID`__ of the managed instance or resource where the event occurred.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param resource_id: The resource_id of this Event.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def system_details(self):
        """
        Gets the system_details of this Event.

        :return: The system_details of this Event.
        :rtype: oci.os_management_hub.models.SystemDetails
        """
        return self._system_details

    @system_details.setter
    def system_details(self, system_details):
        """
        Sets the system_details of this Event.

        :param system_details: The system_details of this Event.
        :type: oci.os_management_hub.models.SystemDetails
        """
        self._system_details = system_details

    @property
    def time_occurred(self):
        """
        Gets the time_occurred of this Event.
        The date and time that the event occurred.


        :return: The time_occurred of this Event.
        :rtype: datetime
        """
        return self._time_occurred

    @time_occurred.setter
    def time_occurred(self, time_occurred):
        """
        Sets the time_occurred of this Event.
        The date and time that the event occurred.


        :param time_occurred: The time_occurred of this Event.
        :type: datetime
        """
        self._time_occurred = time_occurred

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Event.
        The date and time the Event was created, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Event.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Event.
        The date and time the Event was created, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Event.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Event.
        The date and time that the event was updated (in `RFC 3339`__ format).
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Event.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Event.
        The date and time that the event was updated (in `RFC 3339`__ format).
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Event.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Event.
        The current state of the event.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Event.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Event.
        The current state of the event.


        :param lifecycle_state: The lifecycle_state of this Event.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Event.
        Describes the current state of the event in more detail. For example, the
        message can provide actionable information for a resource in the 'FAILED' state.


        :return: The lifecycle_details of this Event.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Event.
        Describes the current state of the event in more detail. For example, the
        message can provide actionable information for a resource in the 'FAILED' state.


        :param lifecycle_details: The lifecycle_details of this Event.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def is_managed_by_autonomous_linux(self):
        """
        Gets the is_managed_by_autonomous_linux of this Event.
        Indicates whether the event occurred on a resource that is managed by the Autonomous Linux service.


        :return: The is_managed_by_autonomous_linux of this Event.
        :rtype: bool
        """
        return self._is_managed_by_autonomous_linux

    @is_managed_by_autonomous_linux.setter
    def is_managed_by_autonomous_linux(self, is_managed_by_autonomous_linux):
        """
        Sets the is_managed_by_autonomous_linux of this Event.
        Indicates whether the event occurred on a resource that is managed by the Autonomous Linux service.


        :param is_managed_by_autonomous_linux: The is_managed_by_autonomous_linux of this Event.
        :type: bool
        """
        self._is_managed_by_autonomous_linux = is_managed_by_autonomous_linux

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this Event.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Event.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Event.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Event.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this Event.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Event.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Event.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Event.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Event.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Event.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Event.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Event.
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
