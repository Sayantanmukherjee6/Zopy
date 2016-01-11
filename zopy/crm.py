"""

	Zoho CRM API bridge.

"""
import requests
from core import Connection, ZohoException

class CRM(Connection):

	def __init__(self, **kwargs):
		for key,value in kwargs.items():
			setattr(self, key, value)
		super(CRM, self).__init__()

	def create_account(self, data=[]):
		self.module = "Accounts"

		xml = self.prepare_xml_request(module=self.module,leads=data)
		url = self.crm_insert_url.format(module=self.module,authToken=self.authToken,scope=self.scope,xmlData=xml)

		response_json = requests.get(url).json()
		
		return response_json

	def insertRecords(self, data=[], module=None):
		
		if module is not None:
			self.module = module

		xml = self.prepare_xml_request(module=self.module,leads=data)

		url = self.crm_insert_url.format(module=self.module, authToken=self.authToken,
			scope=self.scope, xmlData=xml)
		
		response_json = requests.get(url).json()
		
		return response_json
