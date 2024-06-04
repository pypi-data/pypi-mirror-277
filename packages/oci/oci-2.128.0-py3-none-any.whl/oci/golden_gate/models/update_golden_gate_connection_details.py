# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateGoldenGateConnectionDetails(UpdateConnectionDetails):
    """
    The information to update a GoldenGate Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateGoldenGateConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.UpdateGoldenGateConnectionDetails.connection_type` attribute
        of this class is ``GOLDENGATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateGoldenGateConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateGoldenGateConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateGoldenGateConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateGoldenGateConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateGoldenGateConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateGoldenGateConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateGoldenGateConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateGoldenGateConnectionDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdateGoldenGateConnectionDetails.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this UpdateGoldenGateConnectionDetails.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param deployment_id:
            The value to assign to the deployment_id property of this UpdateGoldenGateConnectionDetails.
        :type deployment_id: str

        :param host:
            The value to assign to the host property of this UpdateGoldenGateConnectionDetails.
        :type host: str

        :param port:
            The value to assign to the port property of this UpdateGoldenGateConnectionDetails.
        :type port: int

        :param username:
            The value to assign to the username property of this UpdateGoldenGateConnectionDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this UpdateGoldenGateConnectionDetails.
        :type password: str

        :param private_ip:
            The value to assign to the private_ip property of this UpdateGoldenGateConnectionDetails.
        :type private_ip: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'deployment_id': 'str',
            'host': 'str',
            'port': 'int',
            'username': 'str',
            'password': 'str',
            'private_ip': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'deployment_id': 'deploymentId',
            'host': 'host',
            'port': 'port',
            'username': 'username',
            'password': 'password',
            'private_ip': 'privateIp'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._deployment_id = None
        self._host = None
        self._port = None
        self._username = None
        self._password = None
        self._private_ip = None
        self._connection_type = 'GOLDENGATE'

    @property
    def deployment_id(self):
        """
        Gets the deployment_id of this UpdateGoldenGateConnectionDetails.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deployment_id of this UpdateGoldenGateConnectionDetails.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """
        Sets the deployment_id of this UpdateGoldenGateConnectionDetails.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deployment_id: The deployment_id of this UpdateGoldenGateConnectionDetails.
        :type: str
        """
        self._deployment_id = deployment_id

    @property
    def host(self):
        """
        Gets the host of this UpdateGoldenGateConnectionDetails.
        The name or address of a host.


        :return: The host of this UpdateGoldenGateConnectionDetails.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this UpdateGoldenGateConnectionDetails.
        The name or address of a host.


        :param host: The host of this UpdateGoldenGateConnectionDetails.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this UpdateGoldenGateConnectionDetails.
        The port of an endpoint usually specified for a connection.


        :return: The port of this UpdateGoldenGateConnectionDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateGoldenGateConnectionDetails.
        The port of an endpoint usually specified for a connection.


        :param port: The port of this UpdateGoldenGateConnectionDetails.
        :type: int
        """
        self._port = port

    @property
    def username(self):
        """
        Gets the username of this UpdateGoldenGateConnectionDetails.
        The username credential existing in the Oracle GoldenGate used to be connected to.


        :return: The username of this UpdateGoldenGateConnectionDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UpdateGoldenGateConnectionDetails.
        The username credential existing in the Oracle GoldenGate used to be connected to.


        :param username: The username of this UpdateGoldenGateConnectionDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        Gets the password of this UpdateGoldenGateConnectionDetails.
        The password used to connect to the Oracle GoldenGate accessed trough this connection.


        :return: The password of this UpdateGoldenGateConnectionDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateGoldenGateConnectionDetails.
        The password used to connect to the Oracle GoldenGate accessed trough this connection.


        :param password: The password of this UpdateGoldenGateConnectionDetails.
        :type: str
        """
        self._password = password

    @property
    def private_ip(self):
        """
        Gets the private_ip of this UpdateGoldenGateConnectionDetails.
        Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host
        field, or make sure the host name is resolvable in the target VCN.

        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :return: The private_ip of this UpdateGoldenGateConnectionDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this UpdateGoldenGateConnectionDetails.
        Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host
        field, or make sure the host name is resolvable in the target VCN.

        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :param private_ip: The private_ip of this UpdateGoldenGateConnectionDetails.
        :type: str
        """
        self._private_ip = private_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
