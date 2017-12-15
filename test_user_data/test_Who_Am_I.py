import requests
import urllib3
import unittest
from attribute import *

class testWhoAmI(unittest.TestCase):

	def test_Who_Am_I(self):

		params = (
    		('access_token', getAccessToken()),
		)

		requestWhoAmI = requests.get('%sclient/r0/account/whoami' %getAddr(), headers=getHeader(), params=params, verify=True)

		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestWhoAmI.text


		self.assertEquals(200,requestWhoAmI.status_code)
		

if __name__ == '__main__':
	print "\n\n\033[1;32;40mtest_Who_Am_I : \033[1;32;m\n"
	print "Gets information about the owner of a given access token.\n\n"
	unittest.main()
