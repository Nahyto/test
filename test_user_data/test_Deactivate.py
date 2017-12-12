import requests
import urllib3
import unittest
from test_Register import getAccesToken
from attribute import getUsername,getAddr

class testDesactivate(unittest.TestCase):

	def test_Desactivate(self):

		headers = {
   			'Content-Type': 'application/json',
    		'Accept': 'application/json',
		}

		params = (
    		('access_token', getAccesToken()),
		)

		dataDeactivate = '{"auth": {"user":"%s","password":"devine","session":"bidule","type": "m.login.password"}}' % getUsername()
		requestDeactivate = requests.post('%sr0/account/deactivate' %getAddr(), headers=headers, params=params, data=dataDeactivate, verify=False)
		self.assertEquals(200,requestDeactivate.status_code)
		print "\ntest_Desactivate : \n\nDeactivate the user's account, removing all ability for the user to login again."

if __name__ == '__main__':
	unittest.main()