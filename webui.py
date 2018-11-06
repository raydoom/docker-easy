# -*- coding: utf-8 -*-
__author__ = 'brianyang'

import json

from flask import Flask, render_template, Response

from container_manage import get_server_id_mapping

app = Flask(__name__)

server_id_mapping = get_server_id_mapping()

def common_response(ret):
    return Response(json.dumps({'ret': ret}), content_type='application/json')


@app.route('/all_servers/')
def all_servers():
    server_all = server_id_mapping.values()
    for server_all_al in server_all:
        server_all_al.get_all_container_info()
        all_container_list = server_all_al.get_all_container_info()
        print (all_container_list)

    return render_template('all_servers.html', servers=server_id_mapping.values(), all_container_list = all_container_list)



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8896,debug=True)
