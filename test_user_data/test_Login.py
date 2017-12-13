import random
import string
import requests
import urllib3
import unittest
import sys


class testLogin(unittest.TestCase):

	def test_Login(self):

		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		params = (
 			('access_token', getAccesToken()),	
		)
		dataLogin = '{"type":"m.login.password","user":"%s","password":"devine","session":"bidule"}' % getUsername()
		requestLogin = requests.post('%sr0/login' % getAddr(), data=dataLogin, verify=False)
		self.assertEquals(200,requestLogin.status_code)
		print "\ntest_Login : \n\nVerify if the user can login in this homeserver"

if __name__ == '__main__':
	unittest.main()
