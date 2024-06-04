# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmailRecipientsGroupSummary(object):
    """
    Email recipients group summary for the list recipients groups.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EmailRecipientsGroupSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this EmailRecipientsGroupSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EmailRecipientsGroupSummary.
        :type compartment_id: str

        :param recipients_list:
            The value to assign to the recipients_list property of this EmailRecipientsGroupSummary.
        :type recipients_list: list[oci.usage_api.models.EmailRecipient]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EmailRecipientsGroupSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EmailRecipientsGroupSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EmailRecipientsGroupSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this EmailRecipientsGroupSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'recipients_list': 'list[EmailRecipient]',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'recipients_list': 'recipientsList',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._recipients_list = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this EmailRecipientsGroupSummary.
        The usage statement email recipients group OCID.


        :return: The id of this EmailRecipientsGroupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EmailRecipientsGroupSummary.
        The usage statement email recipients group OCID.


        :param id: The id of this EmailRecipientsGroupSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this EmailRecipientsGroupSummary.
        The customer tenancy.


        :return: The compartment_id of this EmailRecipientsGroupSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EmailRecipientsGroupSummary.
        The customer tenancy.


        :param compartment_id: The compartment_id of this EmailRecipientsGroupSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def recipients_list(self):
        """
        **[Required]** Gets the recipients_list of this EmailRecipientsGroupSummary.
        The list of recipient will receive the usage statement email.


        :return: The recipients_list of this EmailRecipientsGroupSummary.
        :rtype: list[oci.usage_api.models.EmailRecipient]
        """
        return self._recipients_list

    @recipients_list.setter
    def recipients_list(self, recipients_list):
        """
        Sets the recipients_list of this EmailRecipientsGroupSummary.
        The list of recipient will receive the usage statement email.


        :param recipients_list: The recipients_list of this EmailRecipientsGroupSummary.
        :type: list[oci.usage_api.models.EmailRecipient]
        """
        self._recipients_list = recipients_list

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this EmailRecipientsGroupSummary.
        The email recipient group lifecycle state.


        :return: The lifecycle_state of this EmailRecipientsGroupSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EmailRecipientsGroupSummary.
        The email recipient group lifecycle state.


        :param lifecycle_state: The lifecycle_state of this EmailRecipientsGroupSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this EmailRecipientsGroupSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this EmailRecipientsGroupSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EmailRecipientsGroupSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this EmailRecipientsGroupSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this EmailRecipientsGroupSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this EmailRecipientsGroupSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EmailRecipientsGroupSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this EmailRecipientsGroupSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this EmailRecipientsGroupSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this EmailRecipientsGroupSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this EmailRecipientsGroupSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this EmailRecipientsGroupSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
