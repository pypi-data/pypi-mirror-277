# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190506


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOdaPrivateEndpointScanProxyDetails(object):
    """
    Properties that are required to create an ODA Private Endpoint Scan Proxy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOdaPrivateEndpointScanProxyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param scan_listener_type:
            The value to assign to the scan_listener_type property of this CreateOdaPrivateEndpointScanProxyDetails.
        :type scan_listener_type: str

        :param protocol:
            The value to assign to the protocol property of this CreateOdaPrivateEndpointScanProxyDetails.
        :type protocol: str

        :param scan_listener_infos:
            The value to assign to the scan_listener_infos property of this CreateOdaPrivateEndpointScanProxyDetails.
        :type scan_listener_infos: list[oci.oda.models.ScanListenerInfo]

        """
        self.swagger_types = {
            'scan_listener_type': 'str',
            'protocol': 'str',
            'scan_listener_infos': 'list[ScanListenerInfo]'
        }

        self.attribute_map = {
            'scan_listener_type': 'scanListenerType',
            'protocol': 'protocol',
            'scan_listener_infos': 'scanListenerInfos'
        }

        self._scan_listener_type = None
        self._protocol = None
        self._scan_listener_infos = None

    @property
    def scan_listener_type(self):
        """
        **[Required]** Gets the scan_listener_type of this CreateOdaPrivateEndpointScanProxyDetails.
        Type indicating whether Scan listener is specified by its FQDN or list of IPs


        :return: The scan_listener_type of this CreateOdaPrivateEndpointScanProxyDetails.
        :rtype: str
        """
        return self._scan_listener_type

    @scan_listener_type.setter
    def scan_listener_type(self, scan_listener_type):
        """
        Sets the scan_listener_type of this CreateOdaPrivateEndpointScanProxyDetails.
        Type indicating whether Scan listener is specified by its FQDN or list of IPs


        :param scan_listener_type: The scan_listener_type of this CreateOdaPrivateEndpointScanProxyDetails.
        :type: str
        """
        self._scan_listener_type = scan_listener_type

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this CreateOdaPrivateEndpointScanProxyDetails.
        The protocol used for communication between client, scanProxy and RAC's scan listeners


        :return: The protocol of this CreateOdaPrivateEndpointScanProxyDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this CreateOdaPrivateEndpointScanProxyDetails.
        The protocol used for communication between client, scanProxy and RAC's scan listeners


        :param protocol: The protocol of this CreateOdaPrivateEndpointScanProxyDetails.
        :type: str
        """
        self._protocol = protocol

    @property
    def scan_listener_infos(self):
        """
        **[Required]** Gets the scan_listener_infos of this CreateOdaPrivateEndpointScanProxyDetails.
        The FQDN/IPs and port information of customer's Real Application Cluster (RAC)'s SCAN listeners.


        :return: The scan_listener_infos of this CreateOdaPrivateEndpointScanProxyDetails.
        :rtype: list[oci.oda.models.ScanListenerInfo]
        """
        return self._scan_listener_infos

    @scan_listener_infos.setter
    def scan_listener_infos(self, scan_listener_infos):
        """
        Sets the scan_listener_infos of this CreateOdaPrivateEndpointScanProxyDetails.
        The FQDN/IPs and port information of customer's Real Application Cluster (RAC)'s SCAN listeners.


        :param scan_listener_infos: The scan_listener_infos of this CreateOdaPrivateEndpointScanProxyDetails.
        :type: list[oci.oda.models.ScanListenerInfo]
        """
        self._scan_listener_infos = scan_listener_infos

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
