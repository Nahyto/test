import random
import string
import requests
import urllib3
import unittest
import sys
from attribute import getUsername

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
my_args = sys.argv[1:]
del sys.argv[1:]

class testLogin(unittest.TestCase):

	def test_Login(self):

		fileData = open("fileAccessToken.txt","r")
		catFileData = fileData.read()
		access_token = catFileData.split("\n")[0]
		user = catFileData.split("\n")[1]
		params = (
 			('access_token', fileAccessToken.read()),	
		)
		addr = 'https://%s.citadel.team/_matrix/client/' %my_args[0]
		dataLogin = '{"type":"m.login.password","user":"%s","password":"Devinemoi_01"}' % user
		requestLogin = requests.post('%sr0/login' % getAddr(), data=dataLogin, verify=False)
		self.assertEquals(200,requestLogin.status_code)
		print "\ntest_Login : \n\nVerify if the user can login in this homeserver"

if __name__ == '__main__':
	unittest.main()
