import random
import string
import requests
import urllib3
import unittest
from attribute import getUsername

my_args = sys.argv[1:]
del sys.argv[1:]

class testLogout(unittest.TestCase):

	def test_Logout(self):

		fileData = open("fileAccessToken.txt","r")
		catFileData = fileData.read()
		access_token = catFileData.split("\n")[0]

		params = (
    		('access_token', access_token)
		)

		addr = 'https://%s.citadel.team/_matrix/client/' %my_args[0]
		requestLogout = requests.post('%sr0/logout' %addr, params=params, verify=True)
		self.assertEquals(200,requestLogout.status_code)
		print "\ntest_Logout: \n\nVerify if the user can Logout from this homeserver."

if __name__ == '__main__':
	unittest.main()