import requests
import urllib3
import unittest
from test_Register import getAccesToken
from attribute import getUsername,getAddr

class testChangePassword(unittest.TestCase):

	def test_Change_Password(self):

		headers = {
   			'Content-Type': 'application/json',
    		'Accept': 'application/json',
		}

		params = (
    		('access_token', getAccesToken()),
		)

		dataPassword = '{"auth":{"user":"%s","password":"devine","session":"bidule","type": "m.login.password"},"new_password":"bananas"}' % getUsername()
		requestPassword = requests.post('https://localhost:8448/_matrix/client/r0/account/password', headers=headers, params=params, data=dataPassword, verify=False)
		self.assertEquals(200,requestPassword.status_code)
		print "\ntest_Change_Password : \n\nChanges the password for an account on this homeserver."

if __name__ == '__main__':
	unittest.main()