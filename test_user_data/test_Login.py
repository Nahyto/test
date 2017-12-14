import random
import string
import requests
import urllib3
import unittest
import sys
from attribute import getUsername

my_args = sys.argv[1:]
del sys.argv[1:]

class testLogin(unittest.TestCase):

	def test_Login(self):
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

		fileDataRead = open("fileAccessToken.txt","r")
		catFileData = fileDataRead.read()
		access_token = catFileData.split("\n")[0]
		params = (
 			('access_token', access_token),	
		)
		addr = 'https://%s/_matrix/client/' %domain
		dataLogin = '{"type":"m.login.password","user":"%s","password":"Devinemoi_01"}' % username
		requestLogin = requests.post('%sr0/login' %addr, data=dataLogin, verify=True)
		self.assertEquals(200,requestLogin.status_code)

		fileDataWrite = open("fileLoginToken.txt","w")
		body = (requestLogin.text).split("\"")
		fileDataWrite.write(body[3])
		fileDataWrite.write("\n")
		print "\ntest_Login : \n\nVerify if the user can login in this homeserver"

if __name__ == '__main__':
	unittest.main()
