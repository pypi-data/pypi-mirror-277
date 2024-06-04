# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SelfRegistrationProfileFooterText(object):
    """
    Footer text
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SelfRegistrationProfileFooterText object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param locale:
            The value to assign to the locale property of this SelfRegistrationProfileFooterText.
        :type locale: str

        :param value:
            The value to assign to the value property of this SelfRegistrationProfileFooterText.
        :type value: str

        :param default:
            The value to assign to the default property of this SelfRegistrationProfileFooterText.
        :type default: bool

        """
        self.swagger_types = {
            'locale': 'str',
            'value': 'str',
            'default': 'bool'
        }

        self.attribute_map = {
            'locale': 'locale',
            'value': 'value',
            'default': 'default'
        }

        self._locale = None
        self._value = None
        self._default = None

    @property
    def locale(self):
        """
        **[Required]** Gets the locale of this SelfRegistrationProfileFooterText.
        Type of user's locale e.g. en-CA

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCanonicalValueSourceFilter: attrName eq \"locales\" and attrValues.value eq \"$(type)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The locale of this SelfRegistrationProfileFooterText.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this SelfRegistrationProfileFooterText.
        Type of user's locale e.g. en-CA

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCanonicalValueSourceFilter: attrName eq \"locales\" and attrValues.value eq \"$(type)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param locale: The locale of this SelfRegistrationProfileFooterText.
        :type: str
        """
        self._locale = locale

    @property
    def value(self):
        """
        **[Required]** Gets the value of this SelfRegistrationProfileFooterText.
        Localized value of footer text in corresponding locale

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this SelfRegistrationProfileFooterText.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SelfRegistrationProfileFooterText.
        Localized value of footer text in corresponding locale

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this SelfRegistrationProfileFooterText.
        :type: str
        """
        self._value = value

    @property
    def default(self):
        """
        Gets the default of this SelfRegistrationProfileFooterText.
        If true, specifies that the localized attribute instance value is the default and will be returned if no localized value found for requesting user's preferred locale. One and only one instance should have this attribute set to true.

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The default of this SelfRegistrationProfileFooterText.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this SelfRegistrationProfileFooterText.
        If true, specifies that the localized attribute instance value is the default and will be returned if no localized value found for requesting user's preferred locale. One and only one instance should have this attribute set to true.

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param default: The default of this SelfRegistrationProfileFooterText.
        :type: bool
        """
        self._default = default

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
