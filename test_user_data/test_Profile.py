import requests
import urllib3
import unittest
from attribute import *

class testProfile(unittest.TestCase):

	def test_Profile(self):

		requestProfile = requests.get('%sclient/r0/profile/%s' %(getAddr(),getUserID()), verify=False)
		self.assertEquals(200,requestProfile.status_code)
		print "\ntest_Profile : \n Get the combined profile information for this user."

if __name__ == '__main__':
	unittest.main()