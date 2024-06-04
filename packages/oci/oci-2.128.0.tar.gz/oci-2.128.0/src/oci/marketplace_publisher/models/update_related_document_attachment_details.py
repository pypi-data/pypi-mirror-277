# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .update_listing_revision_attachment_details import UpdateListingRevisionAttachmentDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateRelatedDocumentAttachmentDetails(UpdateListingRevisionAttachmentDetails):
    """
    Update Details of the related document attachment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateRelatedDocumentAttachmentDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.marketplace_publisher.models.UpdateRelatedDocumentAttachmentDetails.attachment_type` attribute
        of this class is ``RELATED_DOCUMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateRelatedDocumentAttachmentDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateRelatedDocumentAttachmentDetails.
        :type description: str

        :param attachment_type:
            The value to assign to the attachment_type property of this UpdateRelatedDocumentAttachmentDetails.
        :type attachment_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateRelatedDocumentAttachmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateRelatedDocumentAttachmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param document_category:
            The value to assign to the document_category property of this UpdateRelatedDocumentAttachmentDetails.
        :type document_category: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'attachment_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'document_category': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'attachment_type': 'attachmentType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'document_category': 'documentCategory'
        }

        self._display_name = None
        self._description = None
        self._attachment_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._document_category = None
        self._attachment_type = 'RELATED_DOCUMENT'

    @property
    def document_category(self):
        """
        Gets the document_category of this UpdateRelatedDocumentAttachmentDetails.
        The document category of the listing revision attachment.


        :return: The document_category of this UpdateRelatedDocumentAttachmentDetails.
        :rtype: str
        """
        return self._document_category

    @document_category.setter
    def document_category(self, document_category):
        """
        Sets the document_category of this UpdateRelatedDocumentAttachmentDetails.
        The document category of the listing revision attachment.


        :param document_category: The document_category of this UpdateRelatedDocumentAttachmentDetails.
        :type: str
        """
        self._document_category = document_category

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
