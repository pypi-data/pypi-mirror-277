# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: release


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateKeyDetails(object):
    """
    The details of the key that you want to create.
    """

    #: A constant which can be used with the protection_mode property of a CreateKeyDetails.
    #: This constant has a value of "HSM"
    PROTECTION_MODE_HSM = "HSM"

    #: A constant which can be used with the protection_mode property of a CreateKeyDetails.
    #: This constant has a value of "SOFTWARE"
    PROTECTION_MODE_SOFTWARE = "SOFTWARE"

    #: A constant which can be used with the protection_mode property of a CreateKeyDetails.
    #: This constant has a value of "EXTERNAL"
    PROTECTION_MODE_EXTERNAL = "EXTERNAL"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateKeyDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateKeyDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateKeyDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateKeyDetails.
        :type freeform_tags: dict(str, str)

        :param key_shape:
            The value to assign to the key_shape property of this CreateKeyDetails.
        :type key_shape: oci.key_management.models.KeyShape

        :param is_auto_rotation_enabled:
            The value to assign to the is_auto_rotation_enabled property of this CreateKeyDetails.
        :type is_auto_rotation_enabled: bool

        :param auto_key_rotation_details:
            The value to assign to the auto_key_rotation_details property of this CreateKeyDetails.
        :type auto_key_rotation_details: oci.key_management.models.AutoKeyRotationDetails

        :param protection_mode:
            The value to assign to the protection_mode property of this CreateKeyDetails.
            Allowed values for this property are: "HSM", "SOFTWARE", "EXTERNAL"
        :type protection_mode: str

        :param external_key_reference:
            The value to assign to the external_key_reference property of this CreateKeyDetails.
        :type external_key_reference: oci.key_management.models.ExternalKeyReference

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'key_shape': 'KeyShape',
            'is_auto_rotation_enabled': 'bool',
            'auto_key_rotation_details': 'AutoKeyRotationDetails',
            'protection_mode': 'str',
            'external_key_reference': 'ExternalKeyReference'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'key_shape': 'keyShape',
            'is_auto_rotation_enabled': 'isAutoRotationEnabled',
            'auto_key_rotation_details': 'autoKeyRotationDetails',
            'protection_mode': 'protectionMode',
            'external_key_reference': 'externalKeyReference'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._key_shape = None
        self._is_auto_rotation_enabled = None
        self._auto_key_rotation_details = None
        self._protection_mode = None
        self._external_key_reference = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateKeyDetails.
        The OCID of the compartment where you want to create the master encryption key.


        :return: The compartment_id of this CreateKeyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateKeyDetails.
        The OCID of the compartment where you want to create the master encryption key.


        :param compartment_id: The compartment_id of this CreateKeyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateKeyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateKeyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateKeyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateKeyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateKeyDetails.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateKeyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateKeyDetails.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateKeyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateKeyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateKeyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateKeyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateKeyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def key_shape(self):
        """
        **[Required]** Gets the key_shape of this CreateKeyDetails.

        :return: The key_shape of this CreateKeyDetails.
        :rtype: oci.key_management.models.KeyShape
        """
        return self._key_shape

    @key_shape.setter
    def key_shape(self, key_shape):
        """
        Sets the key_shape of this CreateKeyDetails.

        :param key_shape: The key_shape of this CreateKeyDetails.
        :type: oci.key_management.models.KeyShape
        """
        self._key_shape = key_shape

    @property
    def is_auto_rotation_enabled(self):
        """
        Gets the is_auto_rotation_enabled of this CreateKeyDetails.
        A parameter specifying whether the auto key rotation is enabled or not.


        :return: The is_auto_rotation_enabled of this CreateKeyDetails.
        :rtype: bool
        """
        return self._is_auto_rotation_enabled

    @is_auto_rotation_enabled.setter
    def is_auto_rotation_enabled(self, is_auto_rotation_enabled):
        """
        Sets the is_auto_rotation_enabled of this CreateKeyDetails.
        A parameter specifying whether the auto key rotation is enabled or not.


        :param is_auto_rotation_enabled: The is_auto_rotation_enabled of this CreateKeyDetails.
        :type: bool
        """
        self._is_auto_rotation_enabled = is_auto_rotation_enabled

    @property
    def auto_key_rotation_details(self):
        """
        Gets the auto_key_rotation_details of this CreateKeyDetails.

        :return: The auto_key_rotation_details of this CreateKeyDetails.
        :rtype: oci.key_management.models.AutoKeyRotationDetails
        """
        return self._auto_key_rotation_details

    @auto_key_rotation_details.setter
    def auto_key_rotation_details(self, auto_key_rotation_details):
        """
        Sets the auto_key_rotation_details of this CreateKeyDetails.

        :param auto_key_rotation_details: The auto_key_rotation_details of this CreateKeyDetails.
        :type: oci.key_management.models.AutoKeyRotationDetails
        """
        self._auto_key_rotation_details = auto_key_rotation_details

    @property
    def protection_mode(self):
        """
        Gets the protection_mode of this CreateKeyDetails.
        The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed.
        A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside
        the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists
        on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,
        a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.
        A protection mode of `EXTERNAL` mean that the key persists on the customer's external key manager which is hosted externally outside of oracle.
        Oracle only hold a reference to that key.
        All cryptographic operations that use a key with a protection mode of `EXTERNAL` are performed by external key manager.

        Allowed values for this property are: "HSM", "SOFTWARE", "EXTERNAL"


        :return: The protection_mode of this CreateKeyDetails.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """
        Sets the protection_mode of this CreateKeyDetails.
        The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed.
        A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside
        the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists
        on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,
        a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.
        A protection mode of `EXTERNAL` mean that the key persists on the customer's external key manager which is hosted externally outside of oracle.
        Oracle only hold a reference to that key.
        All cryptographic operations that use a key with a protection mode of `EXTERNAL` are performed by external key manager.


        :param protection_mode: The protection_mode of this CreateKeyDetails.
        :type: str
        """
        allowed_values = ["HSM", "SOFTWARE", "EXTERNAL"]
        if not value_allowed_none_or_none_sentinel(protection_mode, allowed_values):
            raise ValueError(
                f"Invalid value for `protection_mode`, must be None or one of {allowed_values}"
            )
        self._protection_mode = protection_mode

    @property
    def external_key_reference(self):
        """
        Gets the external_key_reference of this CreateKeyDetails.

        :return: The external_key_reference of this CreateKeyDetails.
        :rtype: oci.key_management.models.ExternalKeyReference
        """
        return self._external_key_reference

    @external_key_reference.setter
    def external_key_reference(self, external_key_reference):
        """
        Sets the external_key_reference of this CreateKeyDetails.

        :param external_key_reference: The external_key_reference of this CreateKeyDetails.
        :type: oci.key_management.models.ExternalKeyReference
        """
        self._external_key_reference = external_key_reference

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
