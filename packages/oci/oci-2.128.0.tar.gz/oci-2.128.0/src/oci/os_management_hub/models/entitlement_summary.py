# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntitlementSummary(object):
    """
    Provides summary information for an entitlement.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntitlementSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this EntitlementSummary.
        :type compartment_id: str

        :param csi:
            The value to assign to the csi property of this EntitlementSummary.
        :type csi: str

        :param vendor_name:
            The value to assign to the vendor_name property of this EntitlementSummary.
        :type vendor_name: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'csi': 'str',
            'vendor_name': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'csi': 'csi',
            'vendor_name': 'vendorName'
        }

        self._compartment_id = None
        self._csi = None
        self._vendor_name = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this EntitlementSummary.
        The `OCID`__ of the tenancy containing the entitlement.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this EntitlementSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EntitlementSummary.
        The `OCID`__ of the tenancy containing the entitlement.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this EntitlementSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def csi(self):
        """
        **[Required]** Gets the csi of this EntitlementSummary.
        The Customer Support Identifier (CSI) which unlocks the software sources. The CSI is is a unique key given to a customer and it uniquely identifies the entitlement.


        :return: The csi of this EntitlementSummary.
        :rtype: str
        """
        return self._csi

    @csi.setter
    def csi(self, csi):
        """
        Sets the csi of this EntitlementSummary.
        The Customer Support Identifier (CSI) which unlocks the software sources. The CSI is is a unique key given to a customer and it uniquely identifies the entitlement.


        :param csi: The csi of this EntitlementSummary.
        :type: str
        """
        self._csi = csi

    @property
    def vendor_name(self):
        """
        **[Required]** Gets the vendor_name of this EntitlementSummary.
        The vendor for the entitlement.


        :return: The vendor_name of this EntitlementSummary.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this EntitlementSummary.
        The vendor for the entitlement.


        :param vendor_name: The vendor_name of this EntitlementSummary.
        :type: str
        """
        self._vendor_name = vendor_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
