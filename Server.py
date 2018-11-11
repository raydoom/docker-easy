# -*- coding: utf-8 -*-
__author__ = 'ma'

import time
import docker
import logging

from common_func import get_time_stamp


class Server(object):
	def __init__(self, host, port, name=None):
		self.host = host
		self.port = port
		self.id = host
		if name:
			self.name = name
		else:
			self.name = '%s:%d' % (self.host, self.port)
		self.docker_client = docker.DockerClient(base_url='tcp://%s:%d' % (self.host, self.port),version='1.21')

	def get_all_container_info(self):
		container_infos = {}
		try:
			containers = self.docker_client.containers.list(all=1)
			container_infos['host'] = self.host
			container_infos['port'] = self.port
			container_infos['id']   = self.id
			container_infos['containers'] = self.docker_client.containers.list(all=1)
		except Exception as e:
			logging.error(e)
		return container_infos
	
	def start_container(self, container_id):
		(self.docker_client.containers.get(container_id)).start()
		return True

	def stop_container(self, container_id):
		(self.docker_client.containers.get(container_id)).stop()
		return True

	def restart_container(self, container_id):
		(self.docker_client.containers.get(container_id)).restart()
		return True

	def tail_log(self, container_id, format_func):
		func_tail_log = self.docker_client.containers.get(container_id).logs
		log_old, log_new = '', ''
		secs = 0
		while secs < 60 :		
			log = func_tail_log(tail=15)
			log = log.decode()
			time.sleep(0.5)
			secs = secs+1
			log_old = log_new
			log_new = log
			print (log)
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



