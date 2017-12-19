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
		lock = 1

		while lock:
			pwd = getpass.getpass("Write your password : ")

			if pwd == '':
				lock = 1

			else:
				lock = 0

		dataLogin = '{"type":"m.login.password","user":"%s","password":"%s"}' %(getUsername(),pwd)
		requestLogin = requests.post('%sclient/r0/login' %getAddr(), data=dataLogin, verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestLogin.text

		if "Invalid password" in requestLogin.text:
			print "\n\033[32;31mInvalid Email or Password !\n\033[32;m"
			self.assertEquals(403,requestLogin.status_code)

		else:
			self.assertEquals(200,requestLogin.status_code)


if __name__ == '__main__':
	print "\n\n\033[1;32;40mtest_Login : \n\n\033[1;32;m"
	print "Verify if the user can login on this homeserver.\n\n"
	unittest.main()
