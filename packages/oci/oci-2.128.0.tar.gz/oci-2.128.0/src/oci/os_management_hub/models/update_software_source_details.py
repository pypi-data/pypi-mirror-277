# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSoftwareSourceDetails(object):
    """
    Provides the information used to update a software source.
    """

    #: A constant which can be used with the software_source_type property of a UpdateSoftwareSourceDetails.
    #: This constant has a value of "VENDOR"
    SOFTWARE_SOURCE_TYPE_VENDOR = "VENDOR"

    #: A constant which can be used with the software_source_type property of a UpdateSoftwareSourceDetails.
    #: This constant has a value of "CUSTOM"
    SOFTWARE_SOURCE_TYPE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the software_source_type property of a UpdateSoftwareSourceDetails.
    #: This constant has a value of "VERSIONED"
    SOFTWARE_SOURCE_TYPE_VERSIONED = "VERSIONED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSoftwareSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.os_management_hub.models.UpdateCustomSoftwareSourceDetails`
        * :class:`~oci.os_management_hub.models.UpdateVersionedCustomSoftwareSourceDetails`
        * :class:`~oci.os_management_hub.models.UpdateVendorSoftwareSourceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this UpdateSoftwareSourceDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this UpdateSoftwareSourceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateSoftwareSourceDetails.
        :type description: str

        :param software_source_type:
            The value to assign to the software_source_type property of this UpdateSoftwareSourceDetails.
            Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED"
        :type software_source_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSoftwareSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSoftwareSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'software_source_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'software_source_type': 'softwareSourceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._software_source_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['softwareSourceType']

        if type == 'CUSTOM':
            return 'UpdateCustomSoftwareSourceDetails'

        if type == 'VERSIONED':
            return 'UpdateVersionedCustomSoftwareSourceDetails'

        if type == 'VENDOR':
            return 'UpdateVendorSoftwareSourceDetails'
        else:
            return 'UpdateSoftwareSourceDetails'

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this UpdateSoftwareSourceDetails.
        The `OCID`__ of the compartment that contains the software source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this UpdateSoftwareSourceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UpdateSoftwareSourceDetails.
        The `OCID`__ of the compartment that contains the software source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this UpdateSoftwareSourceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateSoftwareSourceDetails.
        User-friendly name for the software source.


        :return: The display_name of this UpdateSoftwareSourceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateSoftwareSourceDetails.
        User-friendly name for the software source.


        :param display_name: The display_name of this UpdateSoftwareSourceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateSoftwareSourceDetails.
        User-specified description of the software source.


        :return: The description of this UpdateSoftwareSourceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateSoftwareSourceDetails.
        User-specified description of the software source.


        :param description: The description of this UpdateSoftwareSourceDetails.
        :type: str
        """
        self._description = description

    @property
    def software_source_type(self):
        """
        Gets the software_source_type of this UpdateSoftwareSourceDetails.
        Type of the software source.

        Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED"


        :return: The software_source_type of this UpdateSoftwareSourceDetails.
        :rtype: str
        """
        return self._software_source_type

    @software_source_type.setter
    def software_source_type(self, software_source_type):
        """
        Sets the software_source_type of this UpdateSoftwareSourceDetails.
        Type of the software source.


        :param software_source_type: The software_source_type of this UpdateSoftwareSourceDetails.
        :type: str
        """
        allowed_values = ["VENDOR", "CUSTOM", "VERSIONED"]
        if not value_allowed_none_or_none_sentinel(software_source_type, allowed_values):
            raise ValueError(
                f"Invalid value for `software_source_type`, must be None or one of {allowed_values}"
            )
        self._software_source_type = software_source_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateSoftwareSourceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateSoftwareSourceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSoftwareSourceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateSoftwareSourceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSoftwareSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateSoftwareSourceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSoftwareSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateSoftwareSourceDetails.
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
