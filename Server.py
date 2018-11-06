# -*- coding: utf-8 -*-
__author__ = 'brianyang'

import time
import docker
from uuid import uuid4
import logging


class Server(object):
	def __init__(self, host, port, name=None):
		self.host = host
		self.port = port
		self.id = str(uuid4())
		self.RUNNING = 20
		self.STARTING = 10
		self.STOPPED = 0
		if name:
			self.name = name
		else:
			self.name = '%s:%d' % (self.host, self.port)
		self.docker_client = docker.Client(base_url='tcp://%s:%d' % (self.host, self.port))


	def get_container_info(self,container_name):
		container_info = {}
		try:
			container_info = self.docker_client.containers(container_name)
			container_info['host'] = self.host
			container_info['port'] = self.port
			container_info['id']   = self.id
		except Exception as e:
			logging.error(e)
		return container_info


	def get_all_container_info(self):
		container_infos = {}
		try:
			container_infos = self.docker_client.containers()
			for container_info in container_infos:
				container_info['host'] = self.host
				container_info['port'] = self.port
				container_info['id']   = self.id
		except Exception as e:
			logging.error(e)
		return container_infos
	    
