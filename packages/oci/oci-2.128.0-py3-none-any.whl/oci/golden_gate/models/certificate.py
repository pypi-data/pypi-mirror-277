# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Certificate(object):
    """
    Certificate data.
    """

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Certificate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Certificate.
        :type key: str

        :param deployment_id:
            The value to assign to the deployment_id property of this Certificate.
        :type deployment_id: str

        :param certificate_content:
            The value to assign to the certificate_content property of this Certificate.
        :type certificate_content: str

        :param issuer:
            The value to assign to the issuer property of this Certificate.
        :type issuer: str

        :param is_self_signed:
            The value to assign to the is_self_signed property of this Certificate.
        :type is_self_signed: bool

        :param md5_hash:
            The value to assign to the md5_hash property of this Certificate.
        :type md5_hash: str

        :param public_key:
            The value to assign to the public_key property of this Certificate.
        :type public_key: str

        :param public_key_algorithm:
            The value to assign to the public_key_algorithm property of this Certificate.
        :type public_key_algorithm: str

        :param public_key_size:
            The value to assign to the public_key_size property of this Certificate.
        :type public_key_size: int

        :param serial:
            The value to assign to the serial property of this Certificate.
        :type serial: str

        :param subject:
            The value to assign to the subject property of this Certificate.
        :type subject: str

        :param time_valid_from:
            The value to assign to the time_valid_from property of this Certificate.
        :type time_valid_from: datetime

        :param time_valid_to:
            The value to assign to the time_valid_to property of this Certificate.
        :type time_valid_to: datetime

        :param version:
            The value to assign to the version property of this Certificate.
        :type version: str

        :param sha1_hash:
            The value to assign to the sha1_hash property of this Certificate.
        :type sha1_hash: str

        :param authority_key_id:
            The value to assign to the authority_key_id property of this Certificate.
        :type authority_key_id: str

        :param is_ca:
            The value to assign to the is_ca property of this Certificate.
        :type is_ca: bool

        :param subject_key_id:
            The value to assign to the subject_key_id property of this Certificate.
        :type subject_key_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Certificate.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Certificate.
        :type time_created: datetime

        """
        self.swagger_types = {
            'key': 'str',
            'deployment_id': 'str',
            'certificate_content': 'str',
            'issuer': 'str',
            'is_self_signed': 'bool',
            'md5_hash': 'str',
            'public_key': 'str',
            'public_key_algorithm': 'str',
            'public_key_size': 'int',
            'serial': 'str',
            'subject': 'str',
            'time_valid_from': 'datetime',
            'time_valid_to': 'datetime',
            'version': 'str',
            'sha1_hash': 'str',
            'authority_key_id': 'str',
            'is_ca': 'bool',
            'subject_key_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'key': 'key',
            'deployment_id': 'deploymentId',
            'certificate_content': 'certificateContent',
            'issuer': 'issuer',
            'is_self_signed': 'isSelfSigned',
            'md5_hash': 'md5Hash',
            'public_key': 'publicKey',
            'public_key_algorithm': 'publicKeyAlgorithm',
            'public_key_size': 'publicKeySize',
            'serial': 'serial',
            'subject': 'subject',
            'time_valid_from': 'timeValidFrom',
            'time_valid_to': 'timeValidTo',
            'version': 'version',
            'sha1_hash': 'sha1Hash',
            'authority_key_id': 'authorityKeyId',
            'is_ca': 'isCa',
            'subject_key_id': 'subjectKeyId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._key = None
        self._deployment_id = None
        self._certificate_content = None
        self._issuer = None
        self._is_self_signed = None
        self._md5_hash = None
        self._public_key = None
        self._public_key_algorithm = None
        self._public_key_size = None
        self._serial = None
        self._subject = None
        self._time_valid_from = None
        self._time_valid_to = None
        self._version = None
        self._sha1_hash = None
        self._authority_key_id = None
        self._is_ca = None
        self._subject_key_id = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Certificate.
        The identifier key (unique name in the scope of the deployment) of the certificate being referenced.
        It must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.


        :return: The key of this Certificate.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Certificate.
        The identifier key (unique name in the scope of the deployment) of the certificate being referenced.
        It must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.


        :param key: The key of this Certificate.
        :type: str
        """
        self._key = key

    @property
    def deployment_id(self):
        """
        **[Required]** Gets the deployment_id of this Certificate.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deployment_id of this Certificate.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """
        Sets the deployment_id of this Certificate.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deployment_id: The deployment_id of this Certificate.
        :type: str
        """
        self._deployment_id = deployment_id

    @property
    def certificate_content(self):
        """
        **[Required]** Gets the certificate_content of this Certificate.
        The base64 encoded content of the PEM file containing the SSL certificate.


        :return: The certificate_content of this Certificate.
        :rtype: str
        """
        return self._certificate_content

    @certificate_content.setter
    def certificate_content(self, certificate_content):
        """
        Sets the certificate_content of this Certificate.
        The base64 encoded content of the PEM file containing the SSL certificate.


        :param certificate_content: The certificate_content of this Certificate.
        :type: str
        """
        self._certificate_content = certificate_content

    @property
    def issuer(self):
        """
        **[Required]** Gets the issuer of this Certificate.
        The Certificate issuer.


        :return: The issuer of this Certificate.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this Certificate.
        The Certificate issuer.


        :param issuer: The issuer of this Certificate.
        :type: str
        """
        self._issuer = issuer

    @property
    def is_self_signed(self):
        """
        **[Required]** Gets the is_self_signed of this Certificate.
        Indicates if the certificate is self signed.


        :return: The is_self_signed of this Certificate.
        :rtype: bool
        """
        return self._is_self_signed

    @is_self_signed.setter
    def is_self_signed(self, is_self_signed):
        """
        Sets the is_self_signed of this Certificate.
        Indicates if the certificate is self signed.


        :param is_self_signed: The is_self_signed of this Certificate.
        :type: bool
        """
        self._is_self_signed = is_self_signed

    @property
    def md5_hash(self):
        """
        **[Required]** Gets the md5_hash of this Certificate.
        The Certificate md5Hash.


        :return: The md5_hash of this Certificate.
        :rtype: str
        """
        return self._md5_hash

    @md5_hash.setter
    def md5_hash(self, md5_hash):
        """
        Sets the md5_hash of this Certificate.
        The Certificate md5Hash.


        :param md5_hash: The md5_hash of this Certificate.
        :type: str
        """
        self._md5_hash = md5_hash

    @property
    def public_key(self):
        """
        **[Required]** Gets the public_key of this Certificate.
        The Certificate public key.


        :return: The public_key of this Certificate.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this Certificate.
        The Certificate public key.


        :param public_key: The public_key of this Certificate.
        :type: str
        """
        self._public_key = public_key

    @property
    def public_key_algorithm(self):
        """
        **[Required]** Gets the public_key_algorithm of this Certificate.
        The Certificate public key algorithm.


        :return: The public_key_algorithm of this Certificate.
        :rtype: str
        """
        return self._public_key_algorithm

    @public_key_algorithm.setter
    def public_key_algorithm(self, public_key_algorithm):
        """
        Sets the public_key_algorithm of this Certificate.
        The Certificate public key algorithm.


        :param public_key_algorithm: The public_key_algorithm of this Certificate.
        :type: str
        """
        self._public_key_algorithm = public_key_algorithm

    @property
    def public_key_size(self):
        """
        **[Required]** Gets the public_key_size of this Certificate.
        The Certificate public key size.


        :return: The public_key_size of this Certificate.
        :rtype: int
        """
        return self._public_key_size

    @public_key_size.setter
    def public_key_size(self, public_key_size):
        """
        Sets the public_key_size of this Certificate.
        The Certificate public key size.


        :param public_key_size: The public_key_size of this Certificate.
        :type: int
        """
        self._public_key_size = public_key_size

    @property
    def serial(self):
        """
        **[Required]** Gets the serial of this Certificate.
        The Certificate serial.


        :return: The serial of this Certificate.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this Certificate.
        The Certificate serial.


        :param serial: The serial of this Certificate.
        :type: str
        """
        self._serial = serial

    @property
    def subject(self):
        """
        **[Required]** Gets the subject of this Certificate.
        The Certificate subject.


        :return: The subject of this Certificate.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this Certificate.
        The Certificate subject.


        :param subject: The subject of this Certificate.
        :type: str
        """
        self._subject = subject

    @property
    def time_valid_from(self):
        """
        **[Required]** Gets the time_valid_from of this Certificate.
        The time the certificate is valid from. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_valid_from of this Certificate.
        :rtype: datetime
        """
        return self._time_valid_from

    @time_valid_from.setter
    def time_valid_from(self, time_valid_from):
        """
        Sets the time_valid_from of this Certificate.
        The time the certificate is valid from. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_valid_from: The time_valid_from of this Certificate.
        :type: datetime
        """
        self._time_valid_from = time_valid_from

    @property
    def time_valid_to(self):
        """
        **[Required]** Gets the time_valid_to of this Certificate.
        The time the certificate is valid to. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_valid_to of this Certificate.
        :rtype: datetime
        """
        return self._time_valid_to

    @time_valid_to.setter
    def time_valid_to(self, time_valid_to):
        """
        Sets the time_valid_to of this Certificate.
        The time the certificate is valid to. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_valid_to: The time_valid_to of this Certificate.
        :type: datetime
        """
        self._time_valid_to = time_valid_to

    @property
    def version(self):
        """
        **[Required]** Gets the version of this Certificate.
        The Certificate version.


        :return: The version of this Certificate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Certificate.
        The Certificate version.


        :param version: The version of this Certificate.
        :type: str
        """
        self._version = version

    @property
    def sha1_hash(self):
        """
        **[Required]** Gets the sha1_hash of this Certificate.
        The Certificate sha1 hash.


        :return: The sha1_hash of this Certificate.
        :rtype: str
        """
        return self._sha1_hash

    @sha1_hash.setter
    def sha1_hash(self, sha1_hash):
        """
        Sets the sha1_hash of this Certificate.
        The Certificate sha1 hash.


        :param sha1_hash: The sha1_hash of this Certificate.
        :type: str
        """
        self._sha1_hash = sha1_hash

    @property
    def authority_key_id(self):
        """
        **[Required]** Gets the authority_key_id of this Certificate.
        The Certificate authority key id.


        :return: The authority_key_id of this Certificate.
        :rtype: str
        """
        return self._authority_key_id

    @authority_key_id.setter
    def authority_key_id(self, authority_key_id):
        """
        Sets the authority_key_id of this Certificate.
        The Certificate authority key id.


        :param authority_key_id: The authority_key_id of this Certificate.
        :type: str
        """
        self._authority_key_id = authority_key_id

    @property
    def is_ca(self):
        """
        **[Required]** Gets the is_ca of this Certificate.
        Indicates if the certificate is ca.


        :return: The is_ca of this Certificate.
        :rtype: bool
        """
        return self._is_ca

    @is_ca.setter
    def is_ca(self, is_ca):
        """
        Sets the is_ca of this Certificate.
        Indicates if the certificate is ca.


        :param is_ca: The is_ca of this Certificate.
        :type: bool
        """
        self._is_ca = is_ca

    @property
    def subject_key_id(self):
        """
        **[Required]** Gets the subject_key_id of this Certificate.
        The Certificate subject key id.


        :return: The subject_key_id of this Certificate.
        :rtype: str
        """
        return self._subject_key_id

    @subject_key_id.setter
    def subject_key_id(self, subject_key_id):
        """
        Sets the subject_key_id of this Certificate.
        The Certificate subject key id.


        :param subject_key_id: The subject_key_id of this Certificate.
        :type: str
        """
        self._subject_key_id = subject_key_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Certificate.
        Possible certificate lifecycle states.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Certificate.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Certificate.
        Possible certificate lifecycle states.


        :param lifecycle_state: The lifecycle_state of this Certificate.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Certificate.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Certificate.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Certificate.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Certificate.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
