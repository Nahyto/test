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
		self.assertEquals(200,requestLogout.status_code)
		os.remove("AccessToken.txt")
		

if __name__ == '__main__':
	print "\ntest_Logout: \n"
	print "Verify if the user can Logout from this homeserver."
	unittest.main()
