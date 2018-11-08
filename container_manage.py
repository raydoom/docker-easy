# -*- coding: utf-8 -*-
__author__ = 'ma'

from config import SERVERS

def get_server_id_mapping():
    return dict([(server.id, server) for server in SERVERS])
    print (dict([(server.id, server) for server in SERVERS]))

def parse_server_config(server, server_dict):
    parts = server.split('.', 1)
    if len(parts) == 1:
        return server_dict.get(server), ''
    else:
        return server_dict.get(parts[0]), parts[1]

def container_option(server, container_Id, opt):
    if opt == 'start':
        server.start_container(container_Id)
        return True
    if opt == 'stop':
        server.stop_container(container_Id)
        return True
    if opt == 'restart':
        server.restart_container(container_Id)
        return True