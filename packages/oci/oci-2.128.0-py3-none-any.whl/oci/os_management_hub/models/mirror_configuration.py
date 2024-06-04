# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MirrorConfiguration(object):
    """
    Mirror information used for the management station configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MirrorConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param directory:
            The value to assign to the directory property of this MirrorConfiguration.
        :type directory: str

        :param port:
            The value to assign to the port property of this MirrorConfiguration.
        :type port: str

        :param sslport:
            The value to assign to the sslport property of this MirrorConfiguration.
        :type sslport: str

        :param sslcert:
            The value to assign to the sslcert property of this MirrorConfiguration.
        :type sslcert: str

        """
        self.swagger_types = {
            'directory': 'str',
            'port': 'str',
            'sslport': 'str',
            'sslcert': 'str'
        }

        self.attribute_map = {
            'directory': 'directory',
            'port': 'port',
            'sslport': 'sslport',
            'sslcert': 'sslcert'
        }

        self._directory = None
        self._port = None
        self._sslport = None
        self._sslcert = None

    @property
    def directory(self):
        """
        **[Required]** Gets the directory of this MirrorConfiguration.
        Path to the data volume on the management station where software source mirrors are stored.


        :return: The directory of this MirrorConfiguration.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """
        Sets the directory of this MirrorConfiguration.
        Path to the data volume on the management station where software source mirrors are stored.


        :param directory: The directory of this MirrorConfiguration.
        :type: str
        """
        self._directory = directory

    @property
    def port(self):
        """
        **[Required]** Gets the port of this MirrorConfiguration.
        Default mirror listening port for http.


        :return: The port of this MirrorConfiguration.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this MirrorConfiguration.
        Default mirror listening port for http.


        :param port: The port of this MirrorConfiguration.
        :type: str
        """
        self._port = port

    @property
    def sslport(self):
        """
        **[Required]** Gets the sslport of this MirrorConfiguration.
        Default mirror listening port for https.


        :return: The sslport of this MirrorConfiguration.
        :rtype: str
        """
        return self._sslport

    @sslport.setter
    def sslport(self, sslport):
        """
        Sets the sslport of this MirrorConfiguration.
        Default mirror listening port for https.


        :param sslport: The sslport of this MirrorConfiguration.
        :type: str
        """
        self._sslport = sslport

    @property
    def sslcert(self):
        """
        Gets the sslcert of this MirrorConfiguration.
        Path to the SSL cerfificate.


        :return: The sslcert of this MirrorConfiguration.
        :rtype: str
        """
        return self._sslcert

    @sslcert.setter
    def sslcert(self, sslcert):
        """
        Sets the sslcert of this MirrorConfiguration.
        Path to the SSL cerfificate.


        :param sslcert: The sslcert of this MirrorConfiguration.
        :type: str
        """
        self._sslcert = sslcert

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
