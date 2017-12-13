import requests
import urllib3
import unittest
import os,sys

my_args = sys.argv[1:]
del sys.argv[1:]
class testVersion(unittest.TestCase):

	def test_Version(self):
		addr = 'https://%s-test.citadel.team/_matrix/client/' %my_args[0]
		version = "r0.2.0"
		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		r = requests.get('%sversions' % addr, verify=True)
		self.assertIn(version,r.text)
		self.assertEquals(200,r.status_code)
		print "\ntest_Version: \n\nVerify if the versions of this homeserver is r0.2.0"
		if my_args[1] == '1':
			print "\nResponse server :\n%s\n" %r.text

if __name__ == '__main__':
	unittest.main()