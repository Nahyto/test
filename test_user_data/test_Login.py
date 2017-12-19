import random
import string
import requests
import urllib3
import unittest
import sys
import subprocess
import getpass
from attribute import *

class testLogin(unittest.TestCase):

	def test_Login(self):
		pwd = getpass.getpass("Write your password : ")
		dataLogin = '{"type":"m.login.password","user":"%s","password":"%s"}' %(getUsername(),pwd)
		requestLogin = requests.post('%sclient/r0/login' %getAddr(), data=dataLogin, verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestLogin.text

		self.assertEquals(200,requestLogin.status_code)


if __name__ == '__main__':
	print "\n\n\033[1;32;40mtest_Login : \n\n\033[1;32;m"
	print "Verify if the user can login on this homeserver.\n\n"
	unittest.main()
