import random
import string
import requests
import urllib3
import unittest
from test_Register import getAccesToken
from attribute import getUsername,getAddr

class testLogout(unittest.TestCase):

	def test_Logout(self):

		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


		params = (
    		('access_token', getAccesToken()),
		)

		requestLogout = requests.post('%sr0/logout' % getAddr(), params=params, verify=False)
		self.assertEquals(200,requestLogout.status_code)
		print "\ntest_Logout: \n\nVerify if the user can Logout from this homeserver."

if __name__ == '__main__':
	unittest.main()