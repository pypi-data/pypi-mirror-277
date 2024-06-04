# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppVersionSummary(object):
    """
    The version details specific to an app.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param release_date:
            The value to assign to the release_date property of this AppVersionSummary.
        :type release_date: str

        :param end_of_support:
            The value to assign to the end_of_support property of this AppVersionSummary.
        :type end_of_support: str

        :param supported_app_name:
            The value to assign to the supported_app_name property of this AppVersionSummary.
        :type supported_app_name: str

        :param is_certified:
            The value to assign to the is_certified property of this AppVersionSummary.
        :type is_certified: bool

        """
        self.swagger_types = {
            'release_date': 'str',
            'end_of_support': 'str',
            'supported_app_name': 'str',
            'is_certified': 'bool'
        }

        self.attribute_map = {
            'release_date': 'releaseDate',
            'end_of_support': 'endOfSupport',
            'supported_app_name': 'supportedAppName',
            'is_certified': 'isCertified'
        }

        self._release_date = None
        self._end_of_support = None
        self._supported_app_name = None
        self._is_certified = None

    @property
    def release_date(self):
        """
        **[Required]** Gets the release_date of this AppVersionSummary.
        The Autonomous Container Database version release date.


        :return: The release_date of this AppVersionSummary.
        :rtype: str
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """
        Sets the release_date of this AppVersionSummary.
        The Autonomous Container Database version release date.


        :param release_date: The release_date of this AppVersionSummary.
        :type: str
        """
        self._release_date = release_date

    @property
    def end_of_support(self):
        """
        **[Required]** Gets the end_of_support of this AppVersionSummary.
        The Autonomous Container Database version end of support date.


        :return: The end_of_support of this AppVersionSummary.
        :rtype: str
        """
        return self._end_of_support

    @end_of_support.setter
    def end_of_support(self, end_of_support):
        """
        Sets the end_of_support of this AppVersionSummary.
        The Autonomous Container Database version end of support date.


        :param end_of_support: The end_of_support of this AppVersionSummary.
        :type: str
        """
        self._end_of_support = end_of_support

    @property
    def supported_app_name(self):
        """
        **[Required]** Gets the supported_app_name of this AppVersionSummary.
        The name of the supported application.


        :return: The supported_app_name of this AppVersionSummary.
        :rtype: str
        """
        return self._supported_app_name

    @supported_app_name.setter
    def supported_app_name(self, supported_app_name):
        """
        Sets the supported_app_name of this AppVersionSummary.
        The name of the supported application.


        :param supported_app_name: The supported_app_name of this AppVersionSummary.
        :type: str
        """
        self._supported_app_name = supported_app_name

    @property
    def is_certified(self):
        """
        **[Required]** Gets the is_certified of this AppVersionSummary.
        Indicates if the image is certified.


        :return: The is_certified of this AppVersionSummary.
        :rtype: bool
        """
        return self._is_certified

    @is_certified.setter
    def is_certified(self, is_certified):
        """
        Sets the is_certified of this AppVersionSummary.
        Indicates if the image is certified.


        :param is_certified: The is_certified of this AppVersionSummary.
        :type: bool
        """
        self._is_certified = is_certified

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
