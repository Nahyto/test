import random
import string
import requests
import urllib3
import sys
import unittest
import os
from attribute import *

class testLogout(unittest.TestCase):

	def test_Logout(self):

		params = (
    			('access_token', getAccessToken()),
		)
		
		requestLogout = requests.post('%sclient/r0/logout' %getAddr(), params=params, verify=True)

		if getVerbose() == '1':
			print "\n\033[32;40mResponse server :\033[1;32;36m\n%s\n\n\033[32;m" %requestLogout.text

		if "No row found" in requestLogout.text:
			print "\n\033[32;31mThis email has no \033[32;33maccess_token\033[32;m, verify if he's registered and logged in !\n\033[32;m"
			self.assertEquals(404,requestLogout.status_code)
		else:
			print "\n\n\033[32;40mSuccess !\n\033[32;m"
			self.assertEquals(200,requestLogout.status_code)
		

if __name__ == '__main__':
	print "\n\n\033[32;40mtest_Logout: \n\n\033[32;m"
	print "Verify if the user can Logout from this homeserver.\n\n"
	unittest.main()
