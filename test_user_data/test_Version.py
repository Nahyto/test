import requests
import urllib3
import unittest
import os,sys
from attribute import *

class testVersion(unittest.TestCase):

	def test_Version(self):
		
		version = "r0.2.0"
		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		r = requests.get('%sclient/versions' %getAddr(), verify=True)
		self.assertIn(version,r.text)
		self.assertEquals(200,r.status_code)

		if getVerbose() == '1':
			print "\nResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %r.text

if __name__ == '__main__':
	print "\n\033[1;32;40mtest_Version: \033[1;32;m\n"
	print "Verify if the versions of this homeserver is r0.2.0\n\n"
	unittest.main()
