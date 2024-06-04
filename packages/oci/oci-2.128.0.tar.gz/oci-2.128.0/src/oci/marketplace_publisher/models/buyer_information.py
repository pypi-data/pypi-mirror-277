# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BuyerInformation(object):
    """
    The information related to the buyer of an Offer
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BuyerInformation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param company_name:
            The value to assign to the company_name property of this BuyerInformation.
        :type company_name: str

        :param note_to_buyer:
            The value to assign to the note_to_buyer property of this BuyerInformation.
        :type note_to_buyer: str

        :param primary_contact:
            The value to assign to the primary_contact property of this BuyerInformation.
        :type primary_contact: oci.marketplace_publisher.models.Contact

        :param additional_contacts:
            The value to assign to the additional_contacts property of this BuyerInformation.
        :type additional_contacts: list[oci.marketplace_publisher.models.Contact]

        """
        self.swagger_types = {
            'company_name': 'str',
            'note_to_buyer': 'str',
            'primary_contact': 'Contact',
            'additional_contacts': 'list[Contact]'
        }

        self.attribute_map = {
            'company_name': 'companyName',
            'note_to_buyer': 'noteToBuyer',
            'primary_contact': 'primaryContact',
            'additional_contacts': 'additionalContacts'
        }

        self._company_name = None
        self._note_to_buyer = None
        self._primary_contact = None
        self._additional_contacts = None

    @property
    def company_name(self):
        """
        Gets the company_name of this BuyerInformation.
        the name of the company for the buyer


        :return: The company_name of this BuyerInformation.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this BuyerInformation.
        the name of the company for the buyer


        :param company_name: The company_name of this BuyerInformation.
        :type: str
        """
        self._company_name = company_name

    @property
    def note_to_buyer(self):
        """
        Gets the note_to_buyer of this BuyerInformation.
        a note the seller can specify for the buyer through a notification email


        :return: The note_to_buyer of this BuyerInformation.
        :rtype: str
        """
        return self._note_to_buyer

    @note_to_buyer.setter
    def note_to_buyer(self, note_to_buyer):
        """
        Sets the note_to_buyer of this BuyerInformation.
        a note the seller can specify for the buyer through a notification email


        :param note_to_buyer: The note_to_buyer of this BuyerInformation.
        :type: str
        """
        self._note_to_buyer = note_to_buyer

    @property
    def primary_contact(self):
        """
        Gets the primary_contact of this BuyerInformation.

        :return: The primary_contact of this BuyerInformation.
        :rtype: oci.marketplace_publisher.models.Contact
        """
        return self._primary_contact

    @primary_contact.setter
    def primary_contact(self, primary_contact):
        """
        Sets the primary_contact of this BuyerInformation.

        :param primary_contact: The primary_contact of this BuyerInformation.
        :type: oci.marketplace_publisher.models.Contact
        """
        self._primary_contact = primary_contact

    @property
    def additional_contacts(self):
        """
        Gets the additional_contacts of this BuyerInformation.
        the additional contacts associated with the buyer


        :return: The additional_contacts of this BuyerInformation.
        :rtype: list[oci.marketplace_publisher.models.Contact]
        """
        return self._additional_contacts

    @additional_contacts.setter
    def additional_contacts(self, additional_contacts):
        """
        Sets the additional_contacts of this BuyerInformation.
        the additional contacts associated with the buyer


        :param additional_contacts: The additional_contacts of this BuyerInformation.
        :type: list[oci.marketplace_publisher.models.Contact]
        """
        self._additional_contacts = additional_contacts

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
