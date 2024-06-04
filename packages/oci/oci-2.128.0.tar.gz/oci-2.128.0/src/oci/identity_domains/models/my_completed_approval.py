# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MyCompletedApproval(object):
    """
    Schema for MyPendingApproval and MyCompletedApproval
    """

    #: A constant which can be used with the idcs_prevented_operations property of a MyCompletedApproval.
    #: This constant has a value of "replace"
    IDCS_PREVENTED_OPERATIONS_REPLACE = "replace"

    #: A constant which can be used with the idcs_prevented_operations property of a MyCompletedApproval.
    #: This constant has a value of "update"
    IDCS_PREVENTED_OPERATIONS_UPDATE = "update"

    #: A constant which can be used with the idcs_prevented_operations property of a MyCompletedApproval.
    #: This constant has a value of "delete"
    IDCS_PREVENTED_OPERATIONS_DELETE = "delete"

    def __init__(self, **kwargs):
        """
        Initializes a new MyCompletedApproval object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MyCompletedApproval.
        :type id: str

        :param ocid:
            The value to assign to the ocid property of this MyCompletedApproval.
        :type ocid: str

        :param schemas:
            The value to assign to the schemas property of this MyCompletedApproval.
        :type schemas: list[str]

        :param meta:
            The value to assign to the meta property of this MyCompletedApproval.
        :type meta: oci.identity_domains.models.Meta

        :param idcs_created_by:
            The value to assign to the idcs_created_by property of this MyCompletedApproval.
        :type idcs_created_by: oci.identity_domains.models.IdcsCreatedBy

        :param idcs_last_modified_by:
            The value to assign to the idcs_last_modified_by property of this MyCompletedApproval.
        :type idcs_last_modified_by: oci.identity_domains.models.IdcsLastModifiedBy

        :param idcs_prevented_operations:
            The value to assign to the idcs_prevented_operations property of this MyCompletedApproval.
            Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type idcs_prevented_operations: list[str]

        :param tags:
            The value to assign to the tags property of this MyCompletedApproval.
        :type tags: list[oci.identity_domains.models.Tags]

        :param delete_in_progress:
            The value to assign to the delete_in_progress property of this MyCompletedApproval.
        :type delete_in_progress: bool

        :param idcs_last_upgraded_in_release:
            The value to assign to the idcs_last_upgraded_in_release property of this MyCompletedApproval.
        :type idcs_last_upgraded_in_release: str

        :param domain_ocid:
            The value to assign to the domain_ocid property of this MyCompletedApproval.
        :type domain_ocid: str

        :param compartment_ocid:
            The value to assign to the compartment_ocid property of this MyCompletedApproval.
        :type compartment_ocid: str

        :param tenancy_ocid:
            The value to assign to the tenancy_ocid property of this MyCompletedApproval.
        :type tenancy_ocid: str

        :param request_id:
            The value to assign to the request_id property of this MyCompletedApproval.
        :type request_id: str

        :param request_ocid:
            The value to assign to the request_ocid property of this MyCompletedApproval.
        :type request_ocid: str

        :param resource_display_name:
            The value to assign to the resource_display_name property of this MyCompletedApproval.
        :type resource_display_name: str

        :param resource_type:
            The value to assign to the resource_type property of this MyCompletedApproval.
        :type resource_type: str

        :param expires:
            The value to assign to the expires property of this MyCompletedApproval.
        :type expires: str

        :param request_details:
            The value to assign to the request_details property of this MyCompletedApproval.
        :type request_details: str

        :param status:
            The value to assign to the status property of this MyCompletedApproval.
        :type status: str

        :param response_time:
            The value to assign to the response_time property of this MyCompletedApproval.
        :type response_time: str

        :param justification:
            The value to assign to the justification property of this MyCompletedApproval.
        :type justification: str

        :param request_created_time:
            The value to assign to the request_created_time property of this MyCompletedApproval.
        :type request_created_time: str

        """
        self.swagger_types = {
            'id': 'str',
            'ocid': 'str',
            'schemas': 'list[str]',
            'meta': 'Meta',
            'idcs_created_by': 'IdcsCreatedBy',
            'idcs_last_modified_by': 'IdcsLastModifiedBy',
            'idcs_prevented_operations': 'list[str]',
            'tags': 'list[Tags]',
            'delete_in_progress': 'bool',
            'idcs_last_upgraded_in_release': 'str',
            'domain_ocid': 'str',
            'compartment_ocid': 'str',
            'tenancy_ocid': 'str',
            'request_id': 'str',
            'request_ocid': 'str',
            'resource_display_name': 'str',
            'resource_type': 'str',
            'expires': 'str',
            'request_details': 'str',
            'status': 'str',
            'response_time': 'str',
            'justification': 'str',
            'request_created_time': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'ocid': 'ocid',
            'schemas': 'schemas',
            'meta': 'meta',
            'idcs_created_by': 'idcsCreatedBy',
            'idcs_last_modified_by': 'idcsLastModifiedBy',
            'idcs_prevented_operations': 'idcsPreventedOperations',
            'tags': 'tags',
            'delete_in_progress': 'deleteInProgress',
            'idcs_last_upgraded_in_release': 'idcsLastUpgradedInRelease',
            'domain_ocid': 'domainOcid',
            'compartment_ocid': 'compartmentOcid',
            'tenancy_ocid': 'tenancyOcid',
            'request_id': 'requestId',
            'request_ocid': 'requestOcid',
            'resource_display_name': 'resourceDisplayName',
            'resource_type': 'resourceType',
            'expires': 'expires',
            'request_details': 'requestDetails',
            'status': 'status',
            'response_time': 'responseTime',
            'justification': 'justification',
            'request_created_time': 'requestCreatedTime'
        }

        self._id = None
        self._ocid = None
        self._schemas = None
        self._meta = None
        self._idcs_created_by = None
        self._idcs_last_modified_by = None
        self._idcs_prevented_operations = None
        self._tags = None
        self._delete_in_progress = None
        self._idcs_last_upgraded_in_release = None
        self._domain_ocid = None
        self._compartment_ocid = None
        self._tenancy_ocid = None
        self._request_id = None
        self._request_ocid = None
        self._resource_display_name = None
        self._resource_type = None
        self._expires = None
        self._request_details = None
        self._status = None
        self._response_time = None
        self._justification = None
        self._request_created_time = None

    @property
    def id(self):
        """
        Gets the id of this MyCompletedApproval.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :return: The id of this MyCompletedApproval.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MyCompletedApproval.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :param id: The id of this MyCompletedApproval.
        :type: str
        """
        self._id = id

    @property
    def ocid(self):
        """
        Gets the ocid of this MyCompletedApproval.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :return: The ocid of this MyCompletedApproval.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this MyCompletedApproval.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :param ocid: The ocid of this MyCompletedApproval.
        :type: str
        """
        self._ocid = ocid

    @property
    def schemas(self):
        """
        **[Required]** Gets the schemas of this MyCompletedApproval.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The schemas of this MyCompletedApproval.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this MyCompletedApproval.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param schemas: The schemas of this MyCompletedApproval.
        :type: list[str]
        """
        self._schemas = schemas

    @property
    def meta(self):
        """
        Gets the meta of this MyCompletedApproval.

        :return: The meta of this MyCompletedApproval.
        :rtype: oci.identity_domains.models.Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this MyCompletedApproval.

        :param meta: The meta of this MyCompletedApproval.
        :type: oci.identity_domains.models.Meta
        """
        self._meta = meta

    @property
    def idcs_created_by(self):
        """
        Gets the idcs_created_by of this MyCompletedApproval.

        :return: The idcs_created_by of this MyCompletedApproval.
        :rtype: oci.identity_domains.models.IdcsCreatedBy
        """
        return self._idcs_created_by

    @idcs_created_by.setter
    def idcs_created_by(self, idcs_created_by):
        """
        Sets the idcs_created_by of this MyCompletedApproval.

        :param idcs_created_by: The idcs_created_by of this MyCompletedApproval.
        :type: oci.identity_domains.models.IdcsCreatedBy
        """
        self._idcs_created_by = idcs_created_by

    @property
    def idcs_last_modified_by(self):
        """
        Gets the idcs_last_modified_by of this MyCompletedApproval.

        :return: The idcs_last_modified_by of this MyCompletedApproval.
        :rtype: oci.identity_domains.models.IdcsLastModifiedBy
        """
        return self._idcs_last_modified_by

    @idcs_last_modified_by.setter
    def idcs_last_modified_by(self, idcs_last_modified_by):
        """
        Sets the idcs_last_modified_by of this MyCompletedApproval.

        :param idcs_last_modified_by: The idcs_last_modified_by of this MyCompletedApproval.
        :type: oci.identity_domains.models.IdcsLastModifiedBy
        """
        self._idcs_last_modified_by = idcs_last_modified_by

    @property
    def idcs_prevented_operations(self):
        """
        Gets the idcs_prevented_operations of this MyCompletedApproval.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none

        Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The idcs_prevented_operations of this MyCompletedApproval.
        :rtype: list[str]
        """
        return self._idcs_prevented_operations

    @idcs_prevented_operations.setter
    def idcs_prevented_operations(self, idcs_prevented_operations):
        """
        Sets the idcs_prevented_operations of this MyCompletedApproval.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_prevented_operations: The idcs_prevented_operations of this MyCompletedApproval.
        :type: list[str]
        """
        allowed_values = ["replace", "update", "delete"]
        if idcs_prevented_operations:
            idcs_prevented_operations[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in idcs_prevented_operations]
        self._idcs_prevented_operations = idcs_prevented_operations

    @property
    def tags(self):
        """
        Gets the tags of this MyCompletedApproval.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :return: The tags of this MyCompletedApproval.
        :rtype: list[oci.identity_domains.models.Tags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this MyCompletedApproval.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :param tags: The tags of this MyCompletedApproval.
        :type: list[oci.identity_domains.models.Tags]
        """
        self._tags = tags

    @property
    def delete_in_progress(self):
        """
        Gets the delete_in_progress of this MyCompletedApproval.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The delete_in_progress of this MyCompletedApproval.
        :rtype: bool
        """
        return self._delete_in_progress

    @delete_in_progress.setter
    def delete_in_progress(self, delete_in_progress):
        """
        Sets the delete_in_progress of this MyCompletedApproval.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param delete_in_progress: The delete_in_progress of this MyCompletedApproval.
        :type: bool
        """
        self._delete_in_progress = delete_in_progress

    @property
    def idcs_last_upgraded_in_release(self):
        """
        Gets the idcs_last_upgraded_in_release of this MyCompletedApproval.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The idcs_last_upgraded_in_release of this MyCompletedApproval.
        :rtype: str
        """
        return self._idcs_last_upgraded_in_release

    @idcs_last_upgraded_in_release.setter
    def idcs_last_upgraded_in_release(self, idcs_last_upgraded_in_release):
        """
        Sets the idcs_last_upgraded_in_release of this MyCompletedApproval.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_last_upgraded_in_release: The idcs_last_upgraded_in_release of this MyCompletedApproval.
        :type: str
        """
        self._idcs_last_upgraded_in_release = idcs_last_upgraded_in_release

    @property
    def domain_ocid(self):
        """
        Gets the domain_ocid of this MyCompletedApproval.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The domain_ocid of this MyCompletedApproval.
        :rtype: str
        """
        return self._domain_ocid

    @domain_ocid.setter
    def domain_ocid(self, domain_ocid):
        """
        Sets the domain_ocid of this MyCompletedApproval.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param domain_ocid: The domain_ocid of this MyCompletedApproval.
        :type: str
        """
        self._domain_ocid = domain_ocid

    @property
    def compartment_ocid(self):
        """
        Gets the compartment_ocid of this MyCompletedApproval.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The compartment_ocid of this MyCompletedApproval.
        :rtype: str
        """
        return self._compartment_ocid

    @compartment_ocid.setter
    def compartment_ocid(self, compartment_ocid):
        """
        Sets the compartment_ocid of this MyCompletedApproval.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param compartment_ocid: The compartment_ocid of this MyCompletedApproval.
        :type: str
        """
        self._compartment_ocid = compartment_ocid

    @property
    def tenancy_ocid(self):
        """
        Gets the tenancy_ocid of this MyCompletedApproval.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The tenancy_ocid of this MyCompletedApproval.
        :rtype: str
        """
        return self._tenancy_ocid

    @tenancy_ocid.setter
    def tenancy_ocid(self, tenancy_ocid):
        """
        Sets the tenancy_ocid of this MyCompletedApproval.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param tenancy_ocid: The tenancy_ocid of this MyCompletedApproval.
        :type: str
        """
        self._tenancy_ocid = tenancy_ocid

    @property
    def request_id(self):
        """
        Gets the request_id of this MyCompletedApproval.
        The Unique Identifier of the request.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The request_id of this MyCompletedApproval.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this MyCompletedApproval.
        The Unique Identifier of the request.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param request_id: The request_id of this MyCompletedApproval.
        :type: str
        """
        self._request_id = request_id

    @property
    def request_ocid(self):
        """
        Gets the request_ocid of this MyCompletedApproval.
        The OCI Unique Identifier of the request.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The request_ocid of this MyCompletedApproval.
        :rtype: str
        """
        return self._request_ocid

    @request_ocid.setter
    def request_ocid(self, request_ocid):
        """
        Sets the request_ocid of this MyCompletedApproval.
        The OCI Unique Identifier of the request.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param request_ocid: The request_ocid of this MyCompletedApproval.
        :type: str
        """
        self._request_ocid = request_ocid

    @property
    def resource_display_name(self):
        """
        Gets the resource_display_name of this MyCompletedApproval.
        Requested Resource display name

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The resource_display_name of this MyCompletedApproval.
        :rtype: str
        """
        return self._resource_display_name

    @resource_display_name.setter
    def resource_display_name(self, resource_display_name):
        """
        Sets the resource_display_name of this MyCompletedApproval.
        Requested Resource display name

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param resource_display_name: The resource_display_name of this MyCompletedApproval.
        :type: str
        """
        self._resource_display_name = resource_display_name

    @property
    def resource_type(self):
        """
        Gets the resource_type of this MyCompletedApproval.
        Requested Resource type

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The resource_type of this MyCompletedApproval.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this MyCompletedApproval.
        Requested Resource type

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param resource_type: The resource_type of this MyCompletedApproval.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def expires(self):
        """
        Gets the expires of this MyCompletedApproval.
        Time by when ApprovalWorkflowInstance expires

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :return: The expires of this MyCompletedApproval.
        :rtype: str
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """
        Sets the expires of this MyCompletedApproval.
        Time by when ApprovalWorkflowInstance expires

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :param expires: The expires of this MyCompletedApproval.
        :type: str
        """
        self._expires = expires

    @property
    def request_details(self):
        """
        Gets the request_details of this MyCompletedApproval.
        Request Details

        **SCIM++ Properties:**
         - idcsSearchable: false
         - idcsScimCompliant: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The request_details of this MyCompletedApproval.
        :rtype: str
        """
        return self._request_details

    @request_details.setter
    def request_details(self, request_details):
        """
        Sets the request_details of this MyCompletedApproval.
        Request Details

        **SCIM++ Properties:**
         - idcsSearchable: false
         - idcsScimCompliant: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param request_details: The request_details of this MyCompletedApproval.
        :type: str
        """
        self._request_details = request_details

    @property
    def status(self):
        """
        Gets the status of this MyCompletedApproval.
        Status of the approver's response on the approval

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :return: The status of this MyCompletedApproval.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this MyCompletedApproval.
        Status of the approver's response on the approval

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :param status: The status of this MyCompletedApproval.
        :type: str
        """
        self._status = status

    @property
    def response_time(self):
        """
        Gets the response_time of this MyCompletedApproval.
        The time that the user responded to the Approval

        **SCIM++ Properties:**
         - multiValued: false
         - idcsSearchable: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :return: The response_time of this MyCompletedApproval.
        :rtype: str
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """
        Sets the response_time of this MyCompletedApproval.
        The time that the user responded to the Approval

        **SCIM++ Properties:**
         - multiValued: false
         - idcsSearchable: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :param response_time: The response_time of this MyCompletedApproval.
        :type: str
        """
        self._response_time = response_time

    @property
    def justification(self):
        """
        Gets the justification of this MyCompletedApproval.
        Justification for approval

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: writeOnly
         - required: false
         - returned: never
         - type: string
         - uniqueness: none


        :return: The justification of this MyCompletedApproval.
        :rtype: str
        """
        return self._justification

    @justification.setter
    def justification(self, justification):
        """
        Sets the justification of this MyCompletedApproval.
        Justification for approval

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: writeOnly
         - required: false
         - returned: never
         - type: string
         - uniqueness: none


        :param justification: The justification of this MyCompletedApproval.
        :type: str
        """
        self._justification = justification

    @property
    def request_created_time(self):
        """
        Gets the request_created_time of this MyCompletedApproval.
        The time that the Request was created

        **SCIM++ Properties:**
         - multiValued: false
         - idcsSearchable: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :return: The request_created_time of this MyCompletedApproval.
        :rtype: str
        """
        return self._request_created_time

    @request_created_time.setter
    def request_created_time(self, request_created_time):
        """
        Sets the request_created_time of this MyCompletedApproval.
        The time that the Request was created

        **SCIM++ Properties:**
         - multiValued: false
         - idcsSearchable: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :param request_created_time: The request_created_time of this MyCompletedApproval.
        :type: str
        """
        self._request_created_time = request_created_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
