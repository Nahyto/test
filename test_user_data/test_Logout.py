import random
import string
import requests
import urllib3
import sys
import unittest
from attribute import *

class testLogout(unittest.TestCase):

	def test_Logout(self):
		user_id = "@%s:%s" %(getUsername(),getDomain())
		docker = "" %user_id
		access_token = subprocess.check_output("""ssh -i ~/team-playbook/ssh/id_rsa ansible@back-%s.tcs-citadeldev.cloud-omc.org  "docker exec -t bdd-container psql synapse --command \"SELECT token FROM access_tokens WHERE user_id = '%s';\"" """ %(getInfra(),user_id),shell=True).strip()
		params = (
    			('access_token', access_token),
		)

		requestLogout = requests.post('%sclient/r0/logout' %getAddr(), params=params, verify=True)
		self.assertEquals(200,requestLogout.status_code)
		print "\ntest_Logout: \n\nVerify if the user can Logout from this homeserver."

if __name__ == '__main__':
	unittest.main()
