import requests
import urllib3
import unittest
import sys
from attribute import *


class testDesactivate(unittest.TestCase):

	def test_Desactivate(self):

		params = (
    		('access_token', getAccessToken()),
		)

		dataDeactivate = '{"auth": {"user":"%s","password":"Devinemoi_01","session":"bidule","type": "m.login.password"}}' %getUsername()
		requestDeactivate = requests.post('%sclient/r0/account/deactivate' %getAddr(), headers=getHeader(), params=params, data=dataDeactivate, verify=True)
		self.assertEquals(200,requestDeactivate.status_code)
		

if __name__ == '__main__':
	print "\n\n\033[1;32;40mtest_Desactivate : \n\n\033[1;32;m"
	print "Deactivate the user's account, removing all ability for the user to login again.\n\n"
	unittest.main()
