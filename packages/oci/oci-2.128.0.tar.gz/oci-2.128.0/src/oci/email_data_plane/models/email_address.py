# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220926


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmailAddress(object):
    """
    Email address Object that holds display name and email address.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EmailAddress object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param email:
            The value to assign to the email property of this EmailAddress.
        :type email: str

        :param name:
            The value to assign to the name property of this EmailAddress.
        :type name: str

        """
        self.swagger_types = {
            'email': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'email': 'email',
            'name': 'name'
        }

        self._email = None
        self._name = None

    @property
    def email(self):
        """
        **[Required]** Gets the email of this EmailAddress.
        ASCII only email address.


        :return: The email of this EmailAddress.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this EmailAddress.
        ASCII only email address.


        :param email: The email of this EmailAddress.
        :type: str
        """
        self._email = email

    @property
    def name(self):
        """
        Gets the name of this EmailAddress.
        Display name for the email address. UTF-8 is supported for display name `RFC 2047`__.

        __ https://www.rfc-editor.org/rfc/rfc2047


        :return: The name of this EmailAddress.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EmailAddress.
        Display name for the email address. UTF-8 is supported for display name `RFC 2047`__.

        __ https://www.rfc-editor.org/rfc/rfc2047


        :param name: The name of this EmailAddress.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
