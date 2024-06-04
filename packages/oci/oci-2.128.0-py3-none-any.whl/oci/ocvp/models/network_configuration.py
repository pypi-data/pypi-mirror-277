# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230701


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkConfiguration(object):
    """
    The network configurations used by Cluster, including
    `OCIDs`__ of the management subnet and VLANs.

    __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param provisioning_subnet_id:
            The value to assign to the provisioning_subnet_id property of this NetworkConfiguration.
        :type provisioning_subnet_id: str

        :param vsphere_vlan_id:
            The value to assign to the vsphere_vlan_id property of this NetworkConfiguration.
        :type vsphere_vlan_id: str

        :param vmotion_vlan_id:
            The value to assign to the vmotion_vlan_id property of this NetworkConfiguration.
        :type vmotion_vlan_id: str

        :param vsan_vlan_id:
            The value to assign to the vsan_vlan_id property of this NetworkConfiguration.
        :type vsan_vlan_id: str

        :param nsx_v_tep_vlan_id:
            The value to assign to the nsx_v_tep_vlan_id property of this NetworkConfiguration.
        :type nsx_v_tep_vlan_id: str

        :param nsx_edge_v_tep_vlan_id:
            The value to assign to the nsx_edge_v_tep_vlan_id property of this NetworkConfiguration.
        :type nsx_edge_v_tep_vlan_id: str

        :param nsx_edge_uplink1_vlan_id:
            The value to assign to the nsx_edge_uplink1_vlan_id property of this NetworkConfiguration.
        :type nsx_edge_uplink1_vlan_id: str

        :param nsx_edge_uplink2_vlan_id:
            The value to assign to the nsx_edge_uplink2_vlan_id property of this NetworkConfiguration.
        :type nsx_edge_uplink2_vlan_id: str

        :param replication_vlan_id:
            The value to assign to the replication_vlan_id property of this NetworkConfiguration.
        :type replication_vlan_id: str

        :param provisioning_vlan_id:
            The value to assign to the provisioning_vlan_id property of this NetworkConfiguration.
        :type provisioning_vlan_id: str

        :param hcx_vlan_id:
            The value to assign to the hcx_vlan_id property of this NetworkConfiguration.
        :type hcx_vlan_id: str

        """
        self.swagger_types = {
            'provisioning_subnet_id': 'str',
            'vsphere_vlan_id': 'str',
            'vmotion_vlan_id': 'str',
            'vsan_vlan_id': 'str',
            'nsx_v_tep_vlan_id': 'str',
            'nsx_edge_v_tep_vlan_id': 'str',
            'nsx_edge_uplink1_vlan_id': 'str',
            'nsx_edge_uplink2_vlan_id': 'str',
            'replication_vlan_id': 'str',
            'provisioning_vlan_id': 'str',
            'hcx_vlan_id': 'str'
        }

        self.attribute_map = {
            'provisioning_subnet_id': 'provisioningSubnetId',
            'vsphere_vlan_id': 'vsphereVlanId',
            'vmotion_vlan_id': 'vmotionVlanId',
            'vsan_vlan_id': 'vsanVlanId',
            'nsx_v_tep_vlan_id': 'nsxVTepVlanId',
            'nsx_edge_v_tep_vlan_id': 'nsxEdgeVTepVlanId',
            'nsx_edge_uplink1_vlan_id': 'nsxEdgeUplink1VlanId',
            'nsx_edge_uplink2_vlan_id': 'nsxEdgeUplink2VlanId',
            'replication_vlan_id': 'replicationVlanId',
            'provisioning_vlan_id': 'provisioningVlanId',
            'hcx_vlan_id': 'hcxVlanId'
        }

        self._provisioning_subnet_id = None
        self._vsphere_vlan_id = None
        self._vmotion_vlan_id = None
        self._vsan_vlan_id = None
        self._nsx_v_tep_vlan_id = None
        self._nsx_edge_v_tep_vlan_id = None
        self._nsx_edge_uplink1_vlan_id = None
        self._nsx_edge_uplink2_vlan_id = None
        self._replication_vlan_id = None
        self._provisioning_vlan_id = None
        self._hcx_vlan_id = None

    @property
    def provisioning_subnet_id(self):
        """
        **[Required]** Gets the provisioning_subnet_id of this NetworkConfiguration.
        The `OCID`__ of the management subnet used
        to provision the Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The provisioning_subnet_id of this NetworkConfiguration.
        :rtype: str
        """
        return self._provisioning_subnet_id

    @provisioning_subnet_id.setter
    def provisioning_subnet_id(self, provisioning_subnet_id):
        """
        Sets the provisioning_subnet_id of this NetworkConfiguration.
        The `OCID`__ of the management subnet used
        to provision the Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param provisioning_subnet_id: The provisioning_subnet_id of this NetworkConfiguration.
        :type: str
        """
        self._provisioning_subnet_id = provisioning_subnet_id

    @property
    def vsphere_vlan_id(self):
        """
        Gets the vsphere_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the SDDC
        for the vSphere component of the VMware environment. This VLAN is a mandatory attribute
        for Management Cluster.

        This attribute is not guaranteed to reflect the vSphere VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the vSphere VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the vSphere component of the VMware environment, you
        should use :func:`update_sddc` to update the Cluster's
        `vsphereVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vsphere_vlan_id of this NetworkConfiguration.
        :rtype: str
        """
        return self._vsphere_vlan_id

    @vsphere_vlan_id.setter
    def vsphere_vlan_id(self, vsphere_vlan_id):
        """
        Sets the vsphere_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the SDDC
        for the vSphere component of the VMware environment. This VLAN is a mandatory attribute
        for Management Cluster.

        This attribute is not guaranteed to reflect the vSphere VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the vSphere VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the vSphere component of the VMware environment, you
        should use :func:`update_sddc` to update the Cluster's
        `vsphereVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vsphere_vlan_id: The vsphere_vlan_id of this NetworkConfiguration.
        :type: str
        """
        self._vsphere_vlan_id = vsphere_vlan_id

    @property
    def vmotion_vlan_id(self):
        """
        **[Required]** Gets the vmotion_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the Cluster
        for the vMotion component of the VMware environment.

        This attribute is not guaranteed to reflect the vMotion VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the vMotion VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the vMotion component of the VMware environment, you
        should use :func:`update_cluster` to update the Cluster's
        `vmotionVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vmotion_vlan_id of this NetworkConfiguration.
        :rtype: str
        """
        return self._vmotion_vlan_id

    @vmotion_vlan_id.setter
    def vmotion_vlan_id(self, vmotion_vlan_id):
        """
        Sets the vmotion_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the Cluster
        for the vMotion component of the VMware environment.

        This attribute is not guaranteed to reflect the vMotion VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the vMotion VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the vMotion component of the VMware environment, you
        should use :func:`update_cluster` to update the Cluster's
        `vmotionVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vmotion_vlan_id: The vmotion_vlan_id of this NetworkConfiguration.
        :type: str
        """
        self._vmotion_vlan_id = vmotion_vlan_id

    @property
    def vsan_vlan_id(self):
        """
        **[Required]** Gets the vsan_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the Cluster
        for the vSAN component of the VMware environment.

        This attribute is not guaranteed to reflect the vSAN VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the vSAN VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the vSAN component of the VMware environment, you
        should use :func:`update_cluster` to update the Cluster's
        `vsanVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vsan_vlan_id of this NetworkConfiguration.
        :rtype: str
        """
        return self._vsan_vlan_id

    @vsan_vlan_id.setter
    def vsan_vlan_id(self, vsan_vlan_id):
        """
        Sets the vsan_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the Cluster
        for the vSAN component of the VMware environment.

        This attribute is not guaranteed to reflect the vSAN VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the vSAN VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the vSAN component of the VMware environment, you
        should use :func:`update_cluster` to update the Cluster's
        `vsanVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vsan_vlan_id: The vsan_vlan_id of this NetworkConfiguration.
        :type: str
        """
        self._vsan_vlan_id = vsan_vlan_id

    @property
    def nsx_v_tep_vlan_id(self):
        """
        **[Required]** Gets the nsx_v_tep_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the Cluster
        for the NSX VTEP component of the VMware environment.

        This attribute is not guaranteed to reflect the NSX VTEP VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the NSX VTEP VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the NSX VTEP component of the VMware environment, you
        should use :func:`update_cluster` to update the Cluster's
        `nsxVTepVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_v_tep_vlan_id of this NetworkConfiguration.
        :rtype: str
        """
        return self._nsx_v_tep_vlan_id

    @nsx_v_tep_vlan_id.setter
    def nsx_v_tep_vlan_id(self, nsx_v_tep_vlan_id):
        """
        Sets the nsx_v_tep_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the Cluster
        for the NSX VTEP component of the VMware environment.

        This attribute is not guaranteed to reflect the NSX VTEP VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the NSX VTEP VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the NSX VTEP component of the VMware environment, you
        should use :func:`update_cluster` to update the Cluster's
        `nsxVTepVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_v_tep_vlan_id: The nsx_v_tep_vlan_id of this NetworkConfiguration.
        :type: str
        """
        self._nsx_v_tep_vlan_id = nsx_v_tep_vlan_id

    @property
    def nsx_edge_v_tep_vlan_id(self):
        """
        **[Required]** Gets the nsx_edge_v_tep_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the Cluster
        for the NSX Edge VTEP component of the VMware environment.

        This attribute is not guaranteed to reflect the NSX Edge VTEP VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the NSX Edge VTEP VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the NSX Edge VTEP component of the VMware environment, you
        should use :func:`update_cluster` to update the Cluster's
        `nsxEdgeVTepVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_v_tep_vlan_id of this NetworkConfiguration.
        :rtype: str
        """
        return self._nsx_edge_v_tep_vlan_id

    @nsx_edge_v_tep_vlan_id.setter
    def nsx_edge_v_tep_vlan_id(self, nsx_edge_v_tep_vlan_id):
        """
        Sets the nsx_edge_v_tep_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the Cluster
        for the NSX Edge VTEP component of the VMware environment.

        This attribute is not guaranteed to reflect the NSX Edge VTEP VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the NSX Edge VTEP VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the NSX Edge VTEP component of the VMware environment, you
        should use :func:`update_cluster` to update the Cluster's
        `nsxEdgeVTepVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_v_tep_vlan_id: The nsx_edge_v_tep_vlan_id of this NetworkConfiguration.
        :type: str
        """
        self._nsx_edge_v_tep_vlan_id = nsx_edge_v_tep_vlan_id

    @property
    def nsx_edge_uplink1_vlan_id(self):
        """
        Gets the nsx_edge_uplink1_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the SDDC
        for the NSX Edge Uplink 1 component of the VMware environment. This VLAN is a mandatory
        attribute for Management Cluster.

        This attribute is not guaranteed to reflect the NSX Edge Uplink 1 VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the NSX Edge Uplink 1 VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the NSX Edge Uplink 1 component of the VMware environment, you
        should use :func:`update_cluster` to update the Cluster's
        `nsxEdgeUplink1VlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_uplink1_vlan_id of this NetworkConfiguration.
        :rtype: str
        """
        return self._nsx_edge_uplink1_vlan_id

    @nsx_edge_uplink1_vlan_id.setter
    def nsx_edge_uplink1_vlan_id(self, nsx_edge_uplink1_vlan_id):
        """
        Sets the nsx_edge_uplink1_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the SDDC
        for the NSX Edge Uplink 1 component of the VMware environment. This VLAN is a mandatory
        attribute for Management Cluster.

        This attribute is not guaranteed to reflect the NSX Edge Uplink 1 VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the NSX Edge Uplink 1 VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the NSX Edge Uplink 1 component of the VMware environment, you
        should use :func:`update_cluster` to update the Cluster's
        `nsxEdgeUplink1VlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_uplink1_vlan_id: The nsx_edge_uplink1_vlan_id of this NetworkConfiguration.
        :type: str
        """
        self._nsx_edge_uplink1_vlan_id = nsx_edge_uplink1_vlan_id

    @property
    def nsx_edge_uplink2_vlan_id(self):
        """
        Gets the nsx_edge_uplink2_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the SDDC
        for the NSX Edge Uplink 2 component of the VMware environment. This VLAN is a mandatory
        attribute for Management Cluster.

        This attribute is not guaranteed to reflect the NSX Edge Uplink 2 VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the NSX Edge Uplink 2 VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the NSX Edge Uplink 2 component of the VMware environment, you
        should use :func:`update_cluster` to update the Cluster's
        `nsxEdgeUplink2VlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_uplink2_vlan_id of this NetworkConfiguration.
        :rtype: str
        """
        return self._nsx_edge_uplink2_vlan_id

    @nsx_edge_uplink2_vlan_id.setter
    def nsx_edge_uplink2_vlan_id(self, nsx_edge_uplink2_vlan_id):
        """
        Sets the nsx_edge_uplink2_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the SDDC
        for the NSX Edge Uplink 2 component of the VMware environment. This VLAN is a mandatory
        attribute for Management Cluster.

        This attribute is not guaranteed to reflect the NSX Edge Uplink 2 VLAN
        currently used by the ESXi hosts in the Cluster. The purpose
        of this attribute is to show the NSX Edge Uplink 2 VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        Cluster in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN
        for the NSX Edge Uplink 2 component of the VMware environment, you
        should use :func:`update_cluster` to update the Cluster's
        `nsxEdgeUplink2VlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_uplink2_vlan_id: The nsx_edge_uplink2_vlan_id of this NetworkConfiguration.
        :type: str
        """
        self._nsx_edge_uplink2_vlan_id = nsx_edge_uplink2_vlan_id

    @property
    def replication_vlan_id(self):
        """
        Gets the replication_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the Cluster
        for the vSphere Replication component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The replication_vlan_id of this NetworkConfiguration.
        :rtype: str
        """
        return self._replication_vlan_id

    @replication_vlan_id.setter
    def replication_vlan_id(self, replication_vlan_id):
        """
        Sets the replication_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the Cluster
        for the vSphere Replication component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param replication_vlan_id: The replication_vlan_id of this NetworkConfiguration.
        :type: str
        """
        self._replication_vlan_id = replication_vlan_id

    @property
    def provisioning_vlan_id(self):
        """
        Gets the provisioning_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the Cluster
        for the Provisioning component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The provisioning_vlan_id of this NetworkConfiguration.
        :rtype: str
        """
        return self._provisioning_vlan_id

    @provisioning_vlan_id.setter
    def provisioning_vlan_id(self, provisioning_vlan_id):
        """
        Sets the provisioning_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the Cluster
        for the Provisioning component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param provisioning_vlan_id: The provisioning_vlan_id of this NetworkConfiguration.
        :type: str
        """
        self._provisioning_vlan_id = provisioning_vlan_id

    @property
    def hcx_vlan_id(self):
        """
        Gets the hcx_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the SDDC
        for the HCX component of the VMware environment. This VLAN is a mandatory attribute
        for Management Cluster when HCX is enabled.

        This attribute is not guaranteed to reflect the HCX VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the HCX VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the HCX component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `hcxVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The hcx_vlan_id of this NetworkConfiguration.
        :rtype: str
        """
        return self._hcx_vlan_id

    @hcx_vlan_id.setter
    def hcx_vlan_id(self, hcx_vlan_id):
        """
        Sets the hcx_vlan_id of this NetworkConfiguration.
        The `OCID`__ of the VLAN used by the SDDC
        for the HCX component of the VMware environment. This VLAN is a mandatory attribute
        for Management Cluster when HCX is enabled.

        This attribute is not guaranteed to reflect the HCX VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the HCX VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the HCX component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `hcxVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param hcx_vlan_id: The hcx_vlan_id of this NetworkConfiguration.
        :type: str
        """
        self._hcx_vlan_id = hcx_vlan_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
