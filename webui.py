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
        server_container_dict = {}
        server_container_dict['server_ip'] = server.host
        server_container_dict['server_port'] = server.port
        containers = server.get_all_container_info()
        if containers != None:
            server_container_dict['containers'] = containers
            server_all_list.append(server_container_dict)
    return render_template('all_servers.html', servers=server_id_mapping.values(), server_all_list = server_all_list)


@app.route('/<server_ip>/<server_port>/<container_Id>/<opt>/')
def container_opt(server_ip, server_port, container_Id, opt):
    server = Server(host=server_ip,port=int(server_port))
    result = container_option(server=server, container_Id=container_Id, opt=opt)
    print (result)
    return common_response(result)

def format_log(log):

    return '<div>%s</div>' % (log,)


@app.route('/<server_ip>/<server_port>/<container_Id>/tail/')
def tail_std_log(server_ip, server_port, container_Id):
    server = Server(host=server_ip,port=int(server_port))
    return Response(server.tail_log(container_Id, format_log))


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8896,debug=True)
