import requests
import urllib3
import unittest
import urllib
from attribute import *

class testProfile(unittest.TestCase):

	def test_Profile(self):
		
		user_id = "@" + getUsername() + ":" + getDomain()
		user_id = urllib.quote("%s" % (user_id))
		print user_id
		requestProfile = requests.get('%sclient/r0/profile/%s' %(getAddr(),user_id), verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestProfile.text

		self.assertEquals(200,requestProfile.status_code)
		print "\ntest_Profile : \n Get the combined profile information for this user."

if __name__ == '__main__':
	unittest.main()
