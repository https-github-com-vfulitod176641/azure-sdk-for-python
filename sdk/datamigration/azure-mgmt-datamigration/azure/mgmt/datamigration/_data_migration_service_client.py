# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import DataMigrationServiceClientConfiguration
from .operations import ResourceSkusOperations
from .operations import ServicesOperations
from .operations import TasksOperations
from .operations import ServiceTasksOperations
from .operations import ProjectsOperations
from .operations import UsagesOperations
from .operations import Operations
from .operations import FilesOperations
from . import models


class DataMigrationServiceClient(SDKClient):
    """Data Migration Client

    :ivar config: Configuration for client.
    :vartype config: DataMigrationServiceClientConfiguration

    :ivar resource_skus: ResourceSkus operations
    :vartype resource_skus: azure.mgmt.datamigration.operations.ResourceSkusOperations
    :ivar services: Services operations
    :vartype services: azure.mgmt.datamigration.operations.ServicesOperations
    :ivar tasks: Tasks operations
    :vartype tasks: azure.mgmt.datamigration.operations.TasksOperations
    :ivar service_tasks: ServiceTasks operations
    :vartype service_tasks: azure.mgmt.datamigration.operations.ServiceTasksOperations
    :ivar projects: Projects operations
    :vartype projects: azure.mgmt.datamigration.operations.ProjectsOperations
    :ivar usages: Usages operations
    :vartype usages: azure.mgmt.datamigration.operations.UsagesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.datamigration.operations.Operations
    :ivar files: Files operations
    :vartype files: azure.mgmt.datamigration.operations.FilesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Identifier of the subscription
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = DataMigrationServiceClientConfiguration(credentials, subscription_id, base_url)
        super(DataMigrationServiceClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-07-15-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.resource_skus = ResourceSkusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.services = ServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tasks = TasksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.service_tasks = ServiceTasksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.projects = ProjectsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.files = FilesOperations(
            self._client, self.config, self._serialize, self._deserialize)