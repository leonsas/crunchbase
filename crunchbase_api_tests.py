from crunchbase import crunchbase, NetworkError
import unittest

class APICallTests(unittest.TestCase):
	def setUp(self):
		self.cb = crunchbase()
		
	def test_CBInit(self):
		self.assertEqual(len(self.cb.api_key),24)
	
	def test_getAllCompanies(self):
		self.assertTrue(self.cb.getAllCompanies())
		
	def test_getAllFinancialOrganizations(self):
		self.assertTrue(self.cb.getAllFinancialOrganizations())
	
	def test_NetworkError(self):
		self.assertRaises(NetworkError,self.cb.loadJSON,"invalid-query")
if __name__ == '__main__':
    unittest.main()