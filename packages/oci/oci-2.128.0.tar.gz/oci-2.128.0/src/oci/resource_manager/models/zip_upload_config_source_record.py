# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180917

from .config_source_record import ConfigSourceRecord
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ZipUploadConfigSourceRecord(ConfigSourceRecord):
    """
    Information about the user-provided Terraform configuration zip file.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ZipUploadConfigSourceRecord object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.ZipUploadConfigSourceRecord.config_source_record_type` attribute
        of this class is ``ZIP_UPLOAD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_record_type:
            The value to assign to the config_source_record_type property of this ZipUploadConfigSourceRecord.
            Allowed values for this property are: "BITBUCKET_CLOUD_CONFIG_SOURCE", "BITBUCKET_SERVER_CONFIG_SOURCE", "COMPARTMENT_CONFIG_SOURCE", "DEVOPS_CONFIG_SOURCE", "GIT_CONFIG_SOURCE", "OBJECT_STORAGE_CONFIG_SOURCE", "ZIP_UPLOAD"
        :type config_source_record_type: str

        """
        self.swagger_types = {
            'config_source_record_type': 'str'
        }

        self.attribute_map = {
            'config_source_record_type': 'configSourceRecordType'
        }

        self._config_source_record_type = None
        self._config_source_record_type = 'ZIP_UPLOAD'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
