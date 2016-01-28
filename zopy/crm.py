#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from core import (Connection,ZohoException)

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
		return self._getPost( module=module ,xml=xml, 
			action=action, options=options)

	def searchRecords(self, module=None, criteria={}, **options):
		action="searchRecords"
		if not criteria or type(criteria) is not dict:
			raise ZohoException("You must set a valid criteria dictionary")

		criteria_str = "("
		for k,v in criteria.items():
			criteria_str += "{}:{}".format(k,v)
		criteria_str += ")"

		options.update({"criteria":criteria_str})

		return self._getPost( module=module, 
			action=action, options=options)

	def updateRecords(self, module=None, id=None, xmlData=None, **options):
		action="updateRecords"
		options.update({"id":id})

		xml = self.prepare_xml(module=module, leads=xmlData)
		return self._getPost( module=module ,xml=xml, 
			action=action, options=options)



authToken = "70148d40da6dae9d6e7d98bff0d3a6fb"
crm = CRM(authToken=authToken,scope="ZohoCRM/crmapi")

def save_lead_crm(data, baseid, cc_product_id):
	contact_information = {"CustomModule3 Name": data.get('email'),
		"Nombres":data.get('name'),
		"Teléfono celular" : data.get('phone'),
		"Baseid": baseid,
		"Ingresos": data.get('income'),
		"Gastos": data.get('spend_financial'),
		"La mejor tarjeta de crédito": cc_product_id
		}

	insert = crm.insertRecords(module="CustomModule3",xmlData=[contact_information],version=2,duplicateCheck=1)
	lead_id = ""
	if insert.has_key("result"):
		for row in insert['result']['recorddetail']['FL']:
			if row.get('val') == "Id":
				lead_id = row.get('content')
				break
	else:
		lead_id, contact_information = False

	return insert,lead_id, contact_information

insert,lead_id, data = save_lead_crm({'late_payment': u'1', 'name': u'aar\xf3n', 'phone': u'1234567890', 'user_type': 6, 'why_you_want_it': u'12', 'employment_time': u'12', 'why_you_want_it_sub': u'13', 'income': 20000, 'other_credits': u'0', 'spend_financial': u'2000', 'email': u'dhararon@hotmail.com'},
	"2e8f5619-c5d9-11e5-8b35-68a86d4d53f4",
	"La Tarjeta de Crédito Básica")
