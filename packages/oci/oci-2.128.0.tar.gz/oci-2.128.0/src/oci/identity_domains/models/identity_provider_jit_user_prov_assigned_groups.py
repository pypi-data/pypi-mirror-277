# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IdentityProviderJitUserProvAssignedGroups(object):
    """
    Refers to every group of which a JIT-provisioned User should be a member.  Just-in-Time user-provisioning applies this static list when jitUserProvGroupStaticListEnabled:true.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IdentityProviderJitUserProvAssignedGroups object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this IdentityProviderJitUserProvAssignedGroups.
        :type value: str

        :param ref:
            The value to assign to the ref property of this IdentityProviderJitUserProvAssignedGroups.
        :type ref: str

        :param display:
            The value to assign to the display property of this IdentityProviderJitUserProvAssignedGroups.
        :type display: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'display': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'display': 'display'
        }

        self._value = None
        self._ref = None
        self._display = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this IdentityProviderJitUserProvAssignedGroups.
        Group identifier

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this IdentityProviderJitUserProvAssignedGroups.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this IdentityProviderJitUserProvAssignedGroups.
        Group identifier

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this IdentityProviderJitUserProvAssignedGroups.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this IdentityProviderJitUserProvAssignedGroups.
        Group URI

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this IdentityProviderJitUserProvAssignedGroups.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this IdentityProviderJitUserProvAssignedGroups.
        Group URI

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this IdentityProviderJitUserProvAssignedGroups.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this IdentityProviderJitUserProvAssignedGroups.
        A human readable name, primarily used for display purposes. READ-ONLY.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this IdentityProviderJitUserProvAssignedGroups.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this IdentityProviderJitUserProvAssignedGroups.
        A human readable name, primarily used for display purposes. READ-ONLY.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this IdentityProviderJitUserProvAssignedGroups.
        :type: str
        """
        self._display = display

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
