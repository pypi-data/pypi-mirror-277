# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateManagedInstanceGroupDetails(object):
    """
    Provides the information used to create a new managed instance group.
    """

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "ORACLE_LINUX_6"
    OS_FAMILY_ORACLE_LINUX_6 = "ORACLE_LINUX_6"

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "WINDOWS_SERVER_2016"
    OS_FAMILY_WINDOWS_SERVER_2016 = "WINDOWS_SERVER_2016"

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "WINDOWS_SERVER_2019"
    OS_FAMILY_WINDOWS_SERVER_2019 = "WINDOWS_SERVER_2019"

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "WINDOWS_SERVER_2022"
    OS_FAMILY_WINDOWS_SERVER_2022 = "WINDOWS_SERVER_2022"

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "ALL"
    OS_FAMILY_ALL = "ALL"

    #: A constant which can be used with the arch_type property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "I686"
    ARCH_TYPE_I686 = "I686"

    #: A constant which can be used with the arch_type property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "NOARCH"
    ARCH_TYPE_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_type property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "SRC"
    ARCH_TYPE_SRC = "SRC"

    #: A constant which can be used with the vendor_name property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "ORACLE"
    VENDOR_NAME_ORACLE = "ORACLE"

    #: A constant which can be used with the vendor_name property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "MICROSOFT"
    VENDOR_NAME_MICROSOFT = "MICROSOFT"

    #: A constant which can be used with the location property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "ON_PREMISE"
    LOCATION_ON_PREMISE = "ON_PREMISE"

    #: A constant which can be used with the location property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "OCI_COMPUTE"
    LOCATION_OCI_COMPUTE = "OCI_COMPUTE"

    #: A constant which can be used with the location property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "AZURE"
    LOCATION_AZURE = "AZURE"

    #: A constant which can be used with the location property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "EC2"
    LOCATION_EC2 = "EC2"

    #: A constant which can be used with the location property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "GCP"
    LOCATION_GCP = "GCP"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateManagedInstanceGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateManagedInstanceGroupDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateManagedInstanceGroupDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateManagedInstanceGroupDetails.
        :type compartment_id: str

        :param os_family:
            The value to assign to the os_family property of this CreateManagedInstanceGroupDetails.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this CreateManagedInstanceGroupDetails.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"
        :type arch_type: str

        :param vendor_name:
            The value to assign to the vendor_name property of this CreateManagedInstanceGroupDetails.
            Allowed values for this property are: "ORACLE", "MICROSOFT"
        :type vendor_name: str

        :param location:
            The value to assign to the location property of this CreateManagedInstanceGroupDetails.
            Allowed values for this property are: "ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"
        :type location: str

        :param software_source_ids:
            The value to assign to the software_source_ids property of this CreateManagedInstanceGroupDetails.
        :type software_source_ids: list[str]

        :param managed_instance_ids:
            The value to assign to the managed_instance_ids property of this CreateManagedInstanceGroupDetails.
        :type managed_instance_ids: list[str]

        :param notification_topic_id:
            The value to assign to the notification_topic_id property of this CreateManagedInstanceGroupDetails.
        :type notification_topic_id: str

        :param autonomous_settings:
            The value to assign to the autonomous_settings property of this CreateManagedInstanceGroupDetails.
        :type autonomous_settings: oci.os_management_hub.models.UpdatableAutonomousSettings

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateManagedInstanceGroupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateManagedInstanceGroupDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'os_family': 'str',
            'arch_type': 'str',
            'vendor_name': 'str',
            'location': 'str',
            'software_source_ids': 'list[str]',
            'managed_instance_ids': 'list[str]',
            'notification_topic_id': 'str',
            'autonomous_settings': 'UpdatableAutonomousSettings',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'vendor_name': 'vendorName',
            'location': 'location',
            'software_source_ids': 'softwareSourceIds',
            'managed_instance_ids': 'managedInstanceIds',
            'notification_topic_id': 'notificationTopicId',
            'autonomous_settings': 'autonomousSettings',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._os_family = None
        self._arch_type = None
        self._vendor_name = None
        self._location = None
        self._software_source_ids = None
        self._managed_instance_ids = None
        self._notification_topic_id = None
        self._autonomous_settings = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateManagedInstanceGroupDetails.
        A user-friendly name for the managed instance group. Does not have to be unique and you can change the name later. Avoid entering confidential information.


        :return: The display_name of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateManagedInstanceGroupDetails.
        A user-friendly name for the managed instance group. Does not have to be unique and you can change the name later. Avoid entering confidential information.


        :param display_name: The display_name of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateManagedInstanceGroupDetails.
        User-specified description of the managed instance group. Avoid entering confidential information.


        :return: The description of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateManagedInstanceGroupDetails.
        User-specified description of the managed instance group. Avoid entering confidential information.


        :param description: The description of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateManagedInstanceGroupDetails.
        The `OCID`__ of the compartment that contains the managed instance group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateManagedInstanceGroupDetails.
        The `OCID`__ of the compartment that contains the managed instance group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def os_family(self):
        """
        **[Required]** Gets the os_family of this CreateManagedInstanceGroupDetails.
        The operating system type of the managed instances that will be attached to this group.

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"


        :return: The os_family of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this CreateManagedInstanceGroupDetails.
        The operating system type of the managed instances that will be attached to this group.


        :param os_family: The os_family of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            raise ValueError(
                f"Invalid value for `os_family`, must be None or one of {allowed_values}"
            )
        self._os_family = os_family

    @property
    def arch_type(self):
        """
        **[Required]** Gets the arch_type of this CreateManagedInstanceGroupDetails.
        The CPU architecture type of the managed instances that will be attached to this group.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"


        :return: The arch_type of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this CreateManagedInstanceGroupDetails.
        The CPU architecture type of the managed instances that will be attached to this group.


        :param arch_type: The arch_type of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            raise ValueError(
                f"Invalid value for `arch_type`, must be None or one of {allowed_values}"
            )
        self._arch_type = arch_type

    @property
    def vendor_name(self):
        """
        **[Required]** Gets the vendor_name of this CreateManagedInstanceGroupDetails.
        The vendor of the operating system that will be used by the managed instances in the group.

        Allowed values for this property are: "ORACLE", "MICROSOFT"


        :return: The vendor_name of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this CreateManagedInstanceGroupDetails.
        The vendor of the operating system that will be used by the managed instances in the group.


        :param vendor_name: The vendor_name of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        allowed_values = ["ORACLE", "MICROSOFT"]
        if not value_allowed_none_or_none_sentinel(vendor_name, allowed_values):
            raise ValueError(
                f"Invalid value for `vendor_name`, must be None or one of {allowed_values}"
            )
        self._vendor_name = vendor_name

    @property
    def location(self):
        """
        Gets the location of this CreateManagedInstanceGroupDetails.
        The location of managed instances attached to the group. If no location is provided, the default is on premises.

        Allowed values for this property are: "ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"


        :return: The location of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this CreateManagedInstanceGroupDetails.
        The location of managed instances attached to the group. If no location is provided, the default is on premises.


        :param location: The location of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        allowed_values = ["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]
        if not value_allowed_none_or_none_sentinel(location, allowed_values):
            raise ValueError(
                f"Invalid value for `location`, must be None or one of {allowed_values}"
            )
        self._location = location

    @property
    def software_source_ids(self):
        """
        Gets the software_source_ids of this CreateManagedInstanceGroupDetails.
        The list of software source `OCIDs`__ available to the managed instances in the group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The software_source_ids of this CreateManagedInstanceGroupDetails.
        :rtype: list[str]
        """
        return self._software_source_ids

    @software_source_ids.setter
    def software_source_ids(self, software_source_ids):
        """
        Sets the software_source_ids of this CreateManagedInstanceGroupDetails.
        The list of software source `OCIDs`__ available to the managed instances in the group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param software_source_ids: The software_source_ids of this CreateManagedInstanceGroupDetails.
        :type: list[str]
        """
        self._software_source_ids = software_source_ids

    @property
    def managed_instance_ids(self):
        """
        Gets the managed_instance_ids of this CreateManagedInstanceGroupDetails.
        The list of managed instance `OCIDs`__ to be added to the group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The managed_instance_ids of this CreateManagedInstanceGroupDetails.
        :rtype: list[str]
        """
        return self._managed_instance_ids

    @managed_instance_ids.setter
    def managed_instance_ids(self, managed_instance_ids):
        """
        Sets the managed_instance_ids of this CreateManagedInstanceGroupDetails.
        The list of managed instance `OCIDs`__ to be added to the group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param managed_instance_ids: The managed_instance_ids of this CreateManagedInstanceGroupDetails.
        :type: list[str]
        """
        self._managed_instance_ids = managed_instance_ids

    @property
    def notification_topic_id(self):
        """
        Gets the notification_topic_id of this CreateManagedInstanceGroupDetails.
        The `OCID`__ for the Oracle Notifications service (ONS) topic. ONS is the channel used to send notifications to the customer.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The notification_topic_id of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._notification_topic_id

    @notification_topic_id.setter
    def notification_topic_id(self, notification_topic_id):
        """
        Sets the notification_topic_id of this CreateManagedInstanceGroupDetails.
        The `OCID`__ for the Oracle Notifications service (ONS) topic. ONS is the channel used to send notifications to the customer.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param notification_topic_id: The notification_topic_id of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        self._notification_topic_id = notification_topic_id

    @property
    def autonomous_settings(self):
        """
        Gets the autonomous_settings of this CreateManagedInstanceGroupDetails.

        :return: The autonomous_settings of this CreateManagedInstanceGroupDetails.
        :rtype: oci.os_management_hub.models.UpdatableAutonomousSettings
        """
        return self._autonomous_settings

    @autonomous_settings.setter
    def autonomous_settings(self, autonomous_settings):
        """
        Sets the autonomous_settings of this CreateManagedInstanceGroupDetails.

        :param autonomous_settings: The autonomous_settings of this CreateManagedInstanceGroupDetails.
        :type: oci.os_management_hub.models.UpdatableAutonomousSettings
        """
        self._autonomous_settings = autonomous_settings

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateManagedInstanceGroupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateManagedInstanceGroupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateManagedInstanceGroupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateManagedInstanceGroupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateManagedInstanceGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateManagedInstanceGroupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateManagedInstanceGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateManagedInstanceGroupDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
