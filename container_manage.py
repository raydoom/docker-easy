# -*- coding: utf-8 -*-
__author__ = 'ma'

from config import SERVERS

def get_server_id_mapping():
    return dict([(server.id, server) for server in SERVERS])


def container_option(server, container_id, opt):
    if opt == 'start':
        server.start_container(container_id)
        return True
    if opt == 'stop':
        server.stop_container(container_id)
        return True
    if opt == 'restart':
        server.restart_container(container_id)
        return True