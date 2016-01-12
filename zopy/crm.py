"""

	Zoho CRM API bridge.

"""
import requests
from core import Connection, ZohoException

class ZohoInsert(object):
	"""
	Properties:
		count = int # Number of elements was sended
		response = ResponseInsert # object with return data
	"""	
	class ResponseInsert(object):
		"""
		Properties:
			result = dict # Zoho Api Result 
			uri = str # url where post be sended
		"""	 
		def __init__(self, response):
			for key,value in response['response'].items():
				setattr(self, key, value)
			
	def __init__(self, xmlData=None, response=None):
		if xmlData is None or response is None:
			raise ZohoException("xmlData couldn't be None")
		
		self.xmlData = xmlData
		self.count=self.count()
		self.response = self.ResponseInsert(response=response)

	def count(self):
		return len([a for a in self.xmlData if type(a) is dict])

class CRM(Connection):

	def __init__(self, **kwargs):
		for key,value in kwargs.items():
			setattr(self, key, value)

		self.insertURL = "https://crm.zoho.com/crm/private/json/{module}/insertRecords?authtoken={authToken}&scope={scope}&newFormat=1&xmlData={xmlData}"
		super(CRM, self).__init__()

	def insertRecords(self, authToken=None, scope=None, xmlData=[], module=None, **options):
		
		# valid required fields		
		self._valid_mandatory_fields(authToken, scope, module)

		xml = self.prepare_xml(module=self.module,leads=xmlData)

		url = self.insertURL.format(module=self.module, authToken=self.authToken,
			scope=self.scope, xmlData=xml)
		
		response_json = requests.get(url).json()
		
		obj_response = ZohoInsert(xmlData=xmlData, response=response_json)
		return obj_response