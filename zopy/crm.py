#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from core import Connection

class CRM(Connection):

	def __init__(self, **kwargs):
		for key,value in kwargs.items():
			setattr(self, key, value)
		super(CRM, self).__init__()

	""" To retrieve data by the owner of the Authentication Token specified in the API request """
	def getMyRecords(self, module=None, **options):
		action = "getMyRecords"
		params = self._options_to_params(authToken=self.authToken,
			scope=self.scope, options=options)

		return self._getPost( module=module, 
			action=action, options=options)

	""" To insert records into the required Zoho CRM module """
	def insertRecords(self, xmlData=[], module=None, **options):
		action = "insertRecords"
		xml = self.prepare_xml(module=module, leads=xmlData)
		print xml
		return self._getPost( module=module ,xml=xml, 
			action=action, options=options)
