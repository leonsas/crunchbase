import requests
import pdb
class NetworkError(RuntimeError):
   def __init__(self, strerror):
      self.strerror = strerror

class crunchbase:
	def __init__(self):
		
		with open("crunchbase.key") as f:
			self.api_key=f.read()
		
	def loadJSON(self, query):
		baseURL="http://api.crunchbase.com/v/1/"
		qURL=baseURL+query+".js?api_key="+self.api_key

		r=requests.get(qURL)
		if r.status_code == 200:
			return r.json
		else: 
			s= "HTTP code " + str(r.status_code)
			raise NetworkError(s)

	def getAllCompanies(self):
		'''Pulls a list of all the companies in the crunchbase API
		
		'''
		queryString="companies"
		return self.loadJSON(queryString)
	
	
	def getAllFinancialOrganizations(self):
		'''Pulls a list of all the financial organizations in the crunchbase API
		'''
		queryString="financial-organizations"
		return self.loadJSON(queryString)
		
	
	#
	def getFinancialOrganizationInfo(self, orgName):
		'''Pulls the data of the requested financial organization.
		
		Keyword arguments:
		orgName -- The financial organization's permalink string.
		'''
		queryString="financial-organization/"+orgName
		return self.loadJSON(queryString)
		
	def getCompanyInfo(self,companyName):
		'''Pulls the data of the requested financial organization.
		
		Keyword arguments:
		companyName -- The company's permalink string.
		'''
		queryString="company/"+companyName
		return self.loadJSON(queryString)
		