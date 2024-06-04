# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Artifact(object):
    """
    Base model object for the artifacts.
    """

    #: A constant which can be used with the artifact_type property of a Artifact.
    #: This constant has a value of "CONTAINER_IMAGE"
    ARTIFACT_TYPE_CONTAINER_IMAGE = "CONTAINER_IMAGE"

    #: A constant which can be used with the artifact_type property of a Artifact.
    #: This constant has a value of "HELM_CHART"
    ARTIFACT_TYPE_HELM_CHART = "HELM_CHART"

    #: A constant which can be used with the status property of a Artifact.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a Artifact.
    #: This constant has a value of "AVAILABLE"
    STATUS_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the status property of a Artifact.
    #: This constant has a value of "UNAVAILABLE"
    STATUS_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a Artifact.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Artifact.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Artifact.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Artifact.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Artifact.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Artifact.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Artifact object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.marketplace_publisher.models.ContainerImageArtifact`
        * :class:`~oci.marketplace_publisher.models.KubernetesImageArtifact`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Artifact.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Artifact.
        :type display_name: str

        :param artifact_type:
            The value to assign to the artifact_type property of this Artifact.
            Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type artifact_type: str

        :param status:
            The value to assign to the status property of this Artifact.
            Allowed values for this property are: "IN_PROGRESS", "AVAILABLE", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param status_notes:
            The value to assign to the status_notes property of this Artifact.
        :type status_notes: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Artifact.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Artifact.
        :type time_created: datetime

        :param compartment_id:
            The value to assign to the compartment_id property of this Artifact.
        :type compartment_id: str

        :param publisher_id:
            The value to assign to the publisher_id property of this Artifact.
        :type publisher_id: str

        :param time_updated:
            The value to assign to the time_updated property of this Artifact.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Artifact.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Artifact.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Artifact.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'artifact_type': 'str',
            'status': 'str',
            'status_notes': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'compartment_id': 'str',
            'publisher_id': 'str',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'artifact_type': 'artifactType',
            'status': 'status',
            'status_notes': 'statusNotes',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'compartment_id': 'compartmentId',
            'publisher_id': 'publisherId',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._artifact_type = None
        self._status = None
        self._status_notes = None
        self._lifecycle_state = None
        self._time_created = None
        self._compartment_id = None
        self._publisher_id = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['artifactType']

        if type == 'CONTAINER_IMAGE':
            return 'ContainerImageArtifact'

        if type == 'HELM_CHART':
            return 'KubernetesImageArtifact'
        else:
            return 'Artifact'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Artifact.
        Unique OCID identifier for the artifact.


        :return: The id of this Artifact.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Artifact.
        Unique OCID identifier for the artifact.


        :param id: The id of this Artifact.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Artifact.
        A display name for the artifact.


        :return: The display_name of this Artifact.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Artifact.
        A display name for the artifact.


        :param display_name: The display_name of this Artifact.
        :type: str
        """
        self._display_name = display_name

    @property
    def artifact_type(self):
        """
        **[Required]** Gets the artifact_type of this Artifact.
        Artifact type for the artifact.

        Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The artifact_type of this Artifact.
        :rtype: str
        """
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, artifact_type):
        """
        Sets the artifact_type of this Artifact.
        Artifact type for the artifact.


        :param artifact_type: The artifact_type of this Artifact.
        :type: str
        """
        allowed_values = ["CONTAINER_IMAGE", "HELM_CHART"]
        if not value_allowed_none_or_none_sentinel(artifact_type, allowed_values):
            artifact_type = 'UNKNOWN_ENUM_VALUE'
        self._artifact_type = artifact_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this Artifact.
        The current status for the Artifact.

        Allowed values for this property are: "IN_PROGRESS", "AVAILABLE", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this Artifact.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Artifact.
        The current status for the Artifact.


        :param status: The status of this Artifact.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "AVAILABLE", "UNAVAILABLE"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def status_notes(self):
        """
        Gets the status_notes of this Artifact.
        Status notes for the Artifact.


        :return: The status_notes of this Artifact.
        :rtype: str
        """
        return self._status_notes

    @status_notes.setter
    def status_notes(self, status_notes):
        """
        Sets the status_notes of this Artifact.
        Status notes for the Artifact.


        :param status_notes: The status_notes of this Artifact.
        :type: str
        """
        self._status_notes = status_notes

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Artifact.
        The current state for the Artifact.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Artifact.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Artifact.
        The current state for the Artifact.


        :param lifecycle_state: The lifecycle_state of this Artifact.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Artifact.
        The date and time the artifact was created, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Artifact.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Artifact.
        The date and time the artifact was created, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Artifact.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Artifact.
        The unique identifier for the compartment.


        :return: The compartment_id of this Artifact.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Artifact.
        The unique identifier for the compartment.


        :param compartment_id: The compartment_id of this Artifact.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def publisher_id(self):
        """
        **[Required]** Gets the publisher_id of this Artifact.
        The unique identifier for the publisher.


        :return: The publisher_id of this Artifact.
        :rtype: str
        """
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, publisher_id):
        """
        Sets the publisher_id of this Artifact.
        The unique identifier for the publisher.


        :param publisher_id: The publisher_id of this Artifact.
        :type: str
        """
        self._publisher_id = publisher_id

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Artifact.
        The date and time the artifact was updated, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Artifact.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Artifact.
        The date and time the artifact was updated, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Artifact.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Artifact.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Artifact.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Artifact.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Artifact.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Artifact.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Artifact.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Artifact.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Artifact.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Artifact.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Artifact.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Artifact.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Artifact.
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
