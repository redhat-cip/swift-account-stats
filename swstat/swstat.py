#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2013 eNovance SAS <licensing@enovance.com>
#
# Author: Fabien Boucher <fabien.boucher@enovance.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import swiftclient

MAX_RETRIES = 10

try:
    from swiftclient.exceptions import ClientException
except ImportError:
    # swiftclient-1.4 support
    from swiftclient import ClientException


def browse_account(cnx):
    head, containers = cnx.get_account(full_listing=True)
    account_size = int(head['x-account-bytes-used'])
    container_names = [cont['name'] for cont in containers]
    container_sizes = [int(cont['bytes']) for cont in containers]
    return account_size, container_names, container_sizes


def browse_container(cnx, container):
    try:
        head, objects = cnx.get_container(container, full_listing=True)
    except(ClientException):
        # When container is somehow not available
        return 0, [], []

    container_size = int(head['x-container-bytes-used'])
    object_names = [obj['name'] for obj in objects]
    object_sizes = [int(obj['bytes']) for obj in objects]
    return container_size, object_names, object_sizes


def retrieve_account_stats(tenant,
                           bare_storage_url,
                           os_options,
                           admin_token,
                           email=""):
    tenant_storage_url = bare_storage_url + tenant.id
    cnx = swiftclient.client.Connection(
        authurl=None, user=None, key=None,
        preauthurl=tenant_storage_url,
        os_options=os_options,
        preauthtoken=admin_token,
        retries=MAX_RETRIES)

    account_size, container_names, container_sizes = browse_account(cnx)
    mi = None
    ma = None
    av = None
    if container_names:
        mi = min(container_sizes)
        ma = max(container_sizes)
        av = sum(container_sizes) / len(container_names)
    if isinstance(tenant.name, unicode):
        name = tenant.name.encode('utf-8')
    else:
        name = tenant.name
    account_stats = {'account_name': name,
                     'account_id': tenant.id,
                     'account_size': account_size,
                     'container_amount': len(container_names),
                     'container_max_size': ma,
                     'container_min_size': mi,
                     'container_avg_size': av,
                     'email': email}

    containers_stats = []
    for container in container_names:
        container_size, object_names, \
            object_sizes = browse_container(cnx, container)
        if isinstance(container, unicode):
            name = container.encode('utf-8')
        else:
            name = container
        mi = None
        ma = None
        av = None
        if object_names:
            mi = min(object_sizes)
            ma = max(object_sizes)
            av = sum(object_sizes) / len(object_names)
        container_details = {'container_name': name,
                             'container_size': container_size,
                             'object_sizes': object_sizes,
                             'object_amount': len(object_names),
                             'object_max_size': ma,
                             'object_min_size': mi,
                             'object_avg_size': av}
        containers_stats.append(container_details)
    return account_stats, containers_stats
