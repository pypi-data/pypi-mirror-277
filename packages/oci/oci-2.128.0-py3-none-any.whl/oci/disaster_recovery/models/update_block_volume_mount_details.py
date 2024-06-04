# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBlockVolumeMountDetails(object):
    """
    The details for updating the file system mount on a block volume.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBlockVolumeMountDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mount_point:
            The value to assign to the mount_point property of this UpdateBlockVolumeMountDetails.
        :type mount_point: str

        """
        self.swagger_types = {
            'mount_point': 'str'
        }

        self.attribute_map = {
            'mount_point': 'mountPoint'
        }

        self._mount_point = None

    @property
    def mount_point(self):
        """
        Gets the mount_point of this UpdateBlockVolumeMountDetails.
        The physical mount point used for mounting the file system on a block volume.

        Example: `/mnt/yourmountpoint`


        :return: The mount_point of this UpdateBlockVolumeMountDetails.
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """
        Sets the mount_point of this UpdateBlockVolumeMountDetails.
        The physical mount point used for mounting the file system on a block volume.

        Example: `/mnt/yourmountpoint`


        :param mount_point: The mount_point of this UpdateBlockVolumeMountDetails.
        :type: str
        """
        self._mount_point = mount_point

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
