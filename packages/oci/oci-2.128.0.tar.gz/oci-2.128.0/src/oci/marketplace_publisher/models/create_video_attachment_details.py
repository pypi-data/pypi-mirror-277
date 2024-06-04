# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .create_listing_revision_attachment_details import CreateListingRevisionAttachmentDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVideoAttachmentDetails(CreateListingRevisionAttachmentDetails):
    """
    Create Details of the video attachment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVideoAttachmentDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.marketplace_publisher.models.CreateVideoAttachmentDetails.attachment_type` attribute
        of this class is ``VIDEO`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param listing_revision_id:
            The value to assign to the listing_revision_id property of this CreateVideoAttachmentDetails.
        :type listing_revision_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateVideoAttachmentDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateVideoAttachmentDetails.
        :type description: str

        :param attachment_type:
            The value to assign to the attachment_type property of this CreateVideoAttachmentDetails.
        :type attachment_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVideoAttachmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVideoAttachmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param video_attachment_details:
            The value to assign to the video_attachment_details property of this CreateVideoAttachmentDetails.
        :type video_attachment_details: oci.marketplace_publisher.models.CreateVideoDetails

        """
        self.swagger_types = {
            'listing_revision_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'attachment_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'video_attachment_details': 'CreateVideoDetails'
        }

        self.attribute_map = {
            'listing_revision_id': 'listingRevisionId',
            'display_name': 'displayName',
            'description': 'description',
            'attachment_type': 'attachmentType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'video_attachment_details': 'videoAttachmentDetails'
        }

        self._listing_revision_id = None
        self._display_name = None
        self._description = None
        self._attachment_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._video_attachment_details = None
        self._attachment_type = 'VIDEO'

    @property
    def video_attachment_details(self):
        """
        **[Required]** Gets the video_attachment_details of this CreateVideoAttachmentDetails.

        :return: The video_attachment_details of this CreateVideoAttachmentDetails.
        :rtype: oci.marketplace_publisher.models.CreateVideoDetails
        """
        return self._video_attachment_details

    @video_attachment_details.setter
    def video_attachment_details(self, video_attachment_details):
        """
        Sets the video_attachment_details of this CreateVideoAttachmentDetails.

        :param video_attachment_details: The video_attachment_details of this CreateVideoAttachmentDetails.
        :type: oci.marketplace_publisher.models.CreateVideoDetails
        """
        self._video_attachment_details = video_attachment_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
