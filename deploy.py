#!/usr/bin/env python
import argh
import novaclient.auth_plugin
from novaclient.client import Client


def deploy(user, api_key):
    client = connection(user, api_key)
    print client


def connection(user, api_key):
    novaclient.auth_plugin.load_plugin("rackspace")
    os = Client('3', user, api_key, user,
                auth_url='https://identity.api.rackspacecloud.com/v2.0/',
                region_name='dfw', service_type='compute', os_cache=False,
                no_cache=True, auth_system='rackspace')
    return os

argh.dispatch_command(deploy)
