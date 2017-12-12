import requests
import urllib3
import unittest
import sys
from attribute import getUsername,getAddr

class testVersion(unittest.TestCase):

	def test_Version(self):
		version = "r0.2.0"
		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		r = requests.get('%sversions' % getAddr(), verify=False)
		self.assertIn(version,r.text)
		self.assertEquals(200,r.status_code)
		print "\ntest_Version: \n\nVerify if the versions of this homeserver is r0.2.0"

if __name__ == '__main__':
	unittest.main()