import random
import string
import requests
import urllib3
import sys
import unittest
import os
import subprocess
from attribute import *

class testLogout(unittest.TestCase):

	def test_Logout(self):

		params = (
    			('access_token', getAccessToken()),
		)
		user_id = "@" + getUsername() + ":" + getDomain()
		user_id = urllib.quote("'%s'" % (term))
		test = subprocess.check_output("ssh -i ~/team-playbook/ssh/id_rsa ansible@back-jla.tcs-citadeldev.cloud-omc.org \"docker exec -t bdd-container psql synapse --command 'SELECT token FROM access_tokens WHERE user_id = ;'\"")
		print test
		requestLogout = requests.post('%sclient/r0/logout' %getAddr(), params=params, verify=True)

		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestLogout.text

		self.assertEquals(200,requestLogout.status_code)
		

if __name__ == '__main__':
	print "\n\n\033[1;32;40mtest_Logout: \n\n\033[1;32;m"
	print "Verify if the user can Logout from this homeserver.\n\n"
	unittest.main()
