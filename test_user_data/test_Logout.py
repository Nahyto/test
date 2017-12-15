import random
import string
import requests
import urllib3
import sys
import unittest
from attribute import *

class testLogout(unittest.TestCase):

	def test_Logout(self):

		params = (
    			('access_token', getAccessToken()),
		)

		requestLogout = requests.post('%sclient/r0/logout' %getAddr(), params=params, verify=True)
		self.assertEquals(200,requestLogout.status_code)
		

if __name__ == '__main__':
	print "\n\n\033[1;32;40mtest_Logout: \n\n\033[1;32;m"
	print "Verify if the user can Logout from this homeserver."
	unittest.main()
