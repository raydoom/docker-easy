# -*- coding: utf-8 -*-
__author__ = 'ma'

import json, time

from flask import Flask, render_template, Response

from container_manage import get_server_id_mapping, container_option

from Server import Server

app = Flask(__name__)

server_id_mapping = get_server_id_mapping()

def common_response(ret):
    return Response(json.dumps({'ret': ret}), content_type='application/json')


@app.route('/all_servers/')
def all_servers():
    server_all_list = []
    servers = server_id_mapping.values()
    for server in servers:
        containers_list = server.get_all_container_info()
        server_all_list.append(containers_list)
    return render_template('all_servers.html', servers=server_id_mapping.values(), server_all_list = server_all_list)


@app.route('/<server_ip>/<server_port>/<container_id>/<opt>/')
def container_opt(server_ip, server_port, container_id, opt):
    server = Server(host=server_ip,port=int(server_port))
    result = container_option(server=server, container_id=container_id, opt=opt)
    return common_response(result)

def format_log(log):

    return '<div>%s</div>' % (log,)


@app.route('/<server_ip>/<server_port>/<container_id>/tail/')
def tail_std_log(server_ip, server_port, container_id):
    server = Server(host=server_ip,port=int(server_port))
    return Response(server.tail_log(container_id, format_log))


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8896,debug=True)
