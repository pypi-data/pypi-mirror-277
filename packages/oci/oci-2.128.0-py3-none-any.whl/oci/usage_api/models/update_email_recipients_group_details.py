# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateEmailRecipientsGroupDetails(object):
    """
    The saved email recipient group to receive usage statement email.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateEmailRecipientsGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param recipients_list:
            The value to assign to the recipients_list property of this UpdateEmailRecipientsGroupDetails.
        :type recipients_list: list[oci.usage_api.models.EmailRecipient]

        """
        self.swagger_types = {
            'recipients_list': 'list[EmailRecipient]'
        }

        self.attribute_map = {
            'recipients_list': 'recipientsList'
        }

        self._recipients_list = None

    @property
    def recipients_list(self):
        """
        **[Required]** Gets the recipients_list of this UpdateEmailRecipientsGroupDetails.
        The list of recipient will receive the usage statement email.


        :return: The recipients_list of this UpdateEmailRecipientsGroupDetails.
        :rtype: list[oci.usage_api.models.EmailRecipient]
        """
        return self._recipients_list

    @recipients_list.setter
    def recipients_list(self, recipients_list):
        """
        Sets the recipients_list of this UpdateEmailRecipientsGroupDetails.
        The list of recipient will receive the usage statement email.


        :param recipients_list: The recipients_list of this UpdateEmailRecipientsGroupDetails.
        :type: list[oci.usage_api.models.EmailRecipient]
        """
        self._recipients_list = recipients_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
