"""

	Zoho CRM API bridge.

"""
import requests
from core import Connection, ZohoException

class CRM(Connection):

	def __init__(self, **kwargs):
		for key,value in kwargs.items():
			setattr(self, key, value)

		self.insertURL = "https://crm.zoho.com/crm/private/json/{module}/insertRecords?authtoken={authToken}&scope={scope}&newFormat=1&xmlData={xmlData}"

		super(CRM, self).__init__()

	def insertRecords(self, data=[], module=None):
		
		if module is not None:
			self.module = module
		elif module is None and self.module is None:
			raise ZohoException("You have to assing a module")

		xml = self.prepare_xml_request(module=self.module,leads=data)

		url = self.insertURL.format(module=self.module, authToken=self.authToken,
			scope=self.scope, xmlData=xml)
		
		response_json = requests.get(url).json()
		
		return response_json
