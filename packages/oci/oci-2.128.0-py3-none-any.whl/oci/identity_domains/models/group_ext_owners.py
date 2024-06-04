# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GroupExtOwners(object):
    """
    Group owners

    **SCIM++ Properties:**
    - caseExact: false
    - idcsCompositeKey: [value, type]
    - idcsSearchable: true
    - multiValued: true
    - mutability: readWrite
    - required: false
    - returned: request
    - type: complex
    - uniqueness: none
    """

    #: A constant which can be used with the type property of a GroupExtOwners.
    #: This constant has a value of "User"
    TYPE_USER = "User"

    #: A constant which can be used with the type property of a GroupExtOwners.
    #: This constant has a value of "App"
    TYPE_APP = "App"

    def __init__(self, **kwargs):
        """
        Initializes a new GroupExtOwners object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this GroupExtOwners.
        :type value: str

        :param ref:
            The value to assign to the ref property of this GroupExtOwners.
        :type ref: str

        :param display:
            The value to assign to the display property of this GroupExtOwners.
        :type display: str

        :param type:
            The value to assign to the type property of this GroupExtOwners.
            Allowed values for this property are: "User", "App", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'display': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'display': 'display',
            'type': 'type'
        }

        self._value = None
        self._ref = None
        self._display = None
        self._type = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this GroupExtOwners.
        ID of the owner of this Group

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this GroupExtOwners.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this GroupExtOwners.
        ID of the owner of this Group

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this GroupExtOwners.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this GroupExtOwners.
        The URI that corresponds to the owning Resource of this Group

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this GroupExtOwners.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this GroupExtOwners.
        The URI that corresponds to the owning Resource of this Group

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this GroupExtOwners.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this GroupExtOwners.
        Owner display name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this GroupExtOwners.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this GroupExtOwners.
        Owner display name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this GroupExtOwners.
        :type: str
        """
        self._display = display

    @property
    def type(self):
        """
        **[Required]** Gets the type of this GroupExtOwners.
        Indicates the type of resource--for example, User or Group

        **SCIM++ Properties:**
         - caseExact: true
         - idcsDefaultValue: User
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "User", "App", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this GroupExtOwners.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GroupExtOwners.
        Indicates the type of resource--for example, User or Group

        **SCIM++ Properties:**
         - caseExact: true
         - idcsDefaultValue: User
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this GroupExtOwners.
        :type: str
        """
        allowed_values = ["User", "App"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
