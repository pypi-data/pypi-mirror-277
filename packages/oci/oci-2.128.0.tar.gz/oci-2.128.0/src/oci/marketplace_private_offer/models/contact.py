# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Contact(object):
    """
    The contact information of an individual
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Contact object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param first_name:
            The value to assign to the first_name property of this Contact.
        :type first_name: str

        :param last_name:
            The value to assign to the last_name property of this Contact.
        :type last_name: str

        :param email:
            The value to assign to the email property of this Contact.
        :type email: str

        """
        self.swagger_types = {
            'first_name': 'str',
            'last_name': 'str',
            'email': 'str'
        }

        self.attribute_map = {
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email': 'email'
        }

        self._first_name = None
        self._last_name = None
        self._email = None

    @property
    def first_name(self):
        """
        Gets the first_name of this Contact.
        The first name of the contact


        :return: The first_name of this Contact.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Contact.
        The first name of the contact


        :param first_name: The first_name of this Contact.
        :type: str
        """
        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Contact.
        The last name of the contact


        :return: The last_name of this Contact.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Contact.
        The last name of the contact


        :param last_name: The last_name of this Contact.
        :type: str
        """
        self._last_name = last_name

    @property
    def email(self):
        """
        Gets the email of this Contact.
        The email of the contact


        :return: The email of this Contact.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Contact.
        The email of the contact


        :param email: The email of this Contact.
        :type: str
        """
        self._email = email

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
