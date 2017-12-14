import requests
import urllib3
import unittest
import sys
from attribute import getUsername

my_args = sys.argv[1:]
del sys.argv[1:]

class testDesactivate(unittest.TestCase):

	def test_Desactivate(self):

		verbose = ""
		email = ""
		domain = ""
		infra = ""
		if len(my_args) == 3:
			verbose = my_args[1]
			email = my_args[0]
			domain = my_args[2]

		elif len(my_args) == 2:
			email = my_args[0]
			domain = my_args[1]
		username = email.split("@")[0]

		headers = {
   			'Content-Type': 'application/json',
    		'Accept': 'application/json',
		}

		fileDataRead = open("fileLoginToken.txt","r")
		catFileData = fileDataRead.read()
		access_token = catFileData.split("\n")[0]

		params = (
    		('access_token', access_token),
		)

		addr = 'https://%s_matrix/client/' %domain
		dataDeactivate = '{"auth": {"user":"%s","password":"Devinemoi_01","session":"bidule","type": "m.login.password"}}' % username
		requestDeactivate = requests.post('%sr0/account/deactivate' %addr, headers=headers, params=params, data=dataDeactivate, verify=True)
		self.assertEquals(200,requestDeactivate.status_code)
		print "\ntest_Desactivate : \n\nDeactivate the user's account, removing all ability for the user to login again."

if __name__ == '__main__':
	unittest.main()