# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180115


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DynectMigrationDetails(object):
    """
    Details specific to performing a DynECT zone migration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DynectMigrationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param customer_name:
            The value to assign to the customer_name property of this DynectMigrationDetails.
        :type customer_name: str

        :param username:
            The value to assign to the username property of this DynectMigrationDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this DynectMigrationDetails.
        :type password: str

        :param http_redirect_replacements:
            The value to assign to the http_redirect_replacements property of this DynectMigrationDetails.
        :type http_redirect_replacements: dict(str, list[MigrationReplacement])

        """
        self.swagger_types = {
            'customer_name': 'str',
            'username': 'str',
            'password': 'str',
            'http_redirect_replacements': 'dict(str, list[MigrationReplacement])'
        }

        self.attribute_map = {
            'customer_name': 'customerName',
            'username': 'username',
            'password': 'password',
            'http_redirect_replacements': 'httpRedirectReplacements'
        }

        self._customer_name = None
        self._username = None
        self._password = None
        self._http_redirect_replacements = None

    @property
    def customer_name(self):
        """
        **[Required]** Gets the customer_name of this DynectMigrationDetails.
        DynECT customer name the zone belongs to.


        :return: The customer_name of this DynectMigrationDetails.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """
        Sets the customer_name of this DynectMigrationDetails.
        DynECT customer name the zone belongs to.


        :param customer_name: The customer_name of this DynectMigrationDetails.
        :type: str
        """
        self._customer_name = customer_name

    @property
    def username(self):
        """
        **[Required]** Gets the username of this DynectMigrationDetails.
        DynECT API username to perform the migration with.


        :return: The username of this DynectMigrationDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this DynectMigrationDetails.
        DynECT API username to perform the migration with.


        :param username: The username of this DynectMigrationDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        **[Required]** Gets the password of this DynectMigrationDetails.
        DynECT API password for the provided username.


        :return: The password of this DynectMigrationDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this DynectMigrationDetails.
        DynECT API password for the provided username.


        :param password: The password of this DynectMigrationDetails.
        :type: str
        """
        self._password = password

    @property
    def http_redirect_replacements(self):
        """
        Gets the http_redirect_replacements of this DynectMigrationDetails.
        A map of fully-qualified domain names (FQDNs) to an array of `MigrationReplacement` objects.


        :return: The http_redirect_replacements of this DynectMigrationDetails.
        :rtype: dict(str, list[MigrationReplacement])
        """
        return self._http_redirect_replacements

    @http_redirect_replacements.setter
    def http_redirect_replacements(self, http_redirect_replacements):
        """
        Sets the http_redirect_replacements of this DynectMigrationDetails.
        A map of fully-qualified domain names (FQDNs) to an array of `MigrationReplacement` objects.


        :param http_redirect_replacements: The http_redirect_replacements of this DynectMigrationDetails.
        :type: dict(str, list[MigrationReplacement])
        """
        self._http_redirect_replacements = http_redirect_replacements

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
