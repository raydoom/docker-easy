# -*- coding: utf-8 -*-
__author__ = 'ma'

import time
import docker
from uuid import uuid4
import logging

def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

class Server(object):
	def __init__(self, host, port, name=None):
		self.host = host
		self.port = port
		self.id = str(uuid4())
		if name:
			self.name = name
		else:
			self.name = '%s:%d' % (self.host, self.port)
		self.docker_client = docker.Client(base_url='tcp://%s:%d' % (self.host, self.port))


	def get_container_info(self, container_uuid):
		container_info = {}
		try:
			container_info = self.docker_client.containers(container_uuid)
			container_info['host'] = self.host
			container_info['port'] = self.port
			container_info['id']   = self.id
		except Exception as e:
			logging.error(e)
		return container_info


	def get_all_container_info(self):
		container_infos = {}
		try:
			container_infos = self.docker_client.containers(all=1)
			for container_info in container_infos:
				container_info['host'] = self.host
				container_info['port'] = self.port
				container_info['id']   = self.id
		except Exception as e:
			logging.error(e)
		return container_infos
	
	def start_container(self, container_uuid):
		self.docker_client.start(container_uuid)
		return True

	def stop_container(self, container_uuid):
		self.docker_client.stop(container_uuid)
		return True

	def restart_container(self, container_uuid):
		self.docker_client.restart(container_uuid)
		return True

	def get_container_state(self, container_uuid):
		container_infos = self.docker_client.containers(all=1)
		for container_info in container_infos:
			if container_info['Id'] == container_uuid:
				container_state = container_info['State']

	def tail_log(self, container_uuid, format_func):
		func = self.docker_client.logs
		log_old, log_new = '', ''
		secs = 0
		while secs < 300 :		
			log = func(container_uuid, tail=15)
			log = log.decode()
			time.sleep(0.5)
			secs = secs+1
			log_old = log_new
			log_new = log
			for log_line in log.split('\n'):
				time_stamp = get_time_stamp()
				log_line = '[' + time_stamp + ']--' + log_line
				duplicate_flag = 0
				for log_old_line in log_old.split('\n'):
					log_old_line = '[' + time_stamp + ']--' + log_old_line
					if log_line == log_old_line:
						duplicate_flag = 1
				if duplicate_flag == 0:
					yield format_func(log_line)



