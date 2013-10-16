#!/usr/bin/env python
import argh
import gevent
from gevent import AsyncResult
import novaclient.auth_plugin
from novaclient.client import Client

a = AsyncResult()


def build_server():
    pass


def build_chef_server():
    pass


def build_allinone():
    pass


def provision_environment():
    pass


def deploy(user, api_key):
    client = connection(user, api_key)
    flavor = next(flavor.id for flavor in client.flavors.list()
                  if "1GB" in flavor.name)
    image = next(image.id for image in client.images.list()
                 if "Ubuntu 12.04" in image.name)

    gevent.joinall([build_chef_server,
                    build_allinone])
    client.create()


def connection(user, api_key):
    novaclient.auth_plugin.discover_auth_systems()
    auth_plugin = novaclient.auth_plugin.load_plugin("rackspace")
    compute = Client('1.1', user, api_key, user,
                     auth_url='https://identity.api.rackspacecloud.com/v2.0/',
                     region_name='dfw', service_type='compute', os_cache=False,
                     no_cache=True, auth_plugin=auth_plugin,
                     auth_system="rackspace", insecure=True)
    return compute

argh.dispatch_command(deploy)
