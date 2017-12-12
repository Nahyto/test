import requests
import urllib3
import unittest
from test_Register import getAccesToken
from attribute import getUsername,getAddr

class testWhoAmI(unittest.TestCase):

	def test_Who_Am_I(self):

		headers = {
   			'Content-Type': 'application/json',
    		'Accept': 'application/json',
		}

		params = (
    		('access_token', getAccesToken()),
		)

		requestWhoAmI = requests.get('%sr0/account/whoami' %getAddr(), headers=headers, params=params, verify=False)
		self.assertEquals(200,requestWhoAmI.status_code)
		print "\ntest_Who_Am_I : \n\nGets information about the owner of a given access token."

if __name__ == '__main__':
	unittest.main()