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

		fileData = open("fileAccessToken.txt","r")
		catFileData = fileData.read()
		access_token = catFileData.split("\n")[0]
		user = catFileData.split("\n")[1]

		params = (
    		('access_token', access_token),
		)

		addr = 'https://%s.citadel.team/_matrix/client/' %my_args[0]
		dataDeactivate = '{"auth": {"user":"%s","password":"Devinemoi_01","session":"bidule","type": "m.login.password"}}' % user
		requestDeactivate = requests.post('%sr0/account/deactivate' %addr, headers=headers, params=params, data=dataDeactivate, verify=True)
		self.assertEquals(200,requestDeactivate.status_code)
		print "\ntest_Desactivate : \n\nDeactivate the user's account, removing all ability for the user to login again."

if __name__ == '__main__':
	unittest.main()