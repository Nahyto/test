import random
import string
import requests
import urllib3
import unittest
import sys
import subprocess
from attribute import *

class testLogin(unittest.TestCase):

	def test_Login(self):
		
		user_id = subprocess.check_output("ssh -i ~/team-playbook/ssh/id_rsa ansible@back-%s.tcs-citadeldev.cloud-omc.org \"docker exec -ti bdd-container psql synapse --command 'select user_id from user_threepids where email = %s;'\"" %getEmail())
		print user_id
		access_token = subprocess.check_output("ssh -i ~/team-playbook/ssh/id_rsa ansible@back-%s.tcs-citadeldev.cloud-omc.org \"docker exec -ti bdd-container psql synapse --command 'select token from access_tokens where user_id = %s;'\"" %user_id)
		params = (

 			('access_token', access_token),	
		
		)
		dataLogin = '{"type":"m.login.password","user":"%s","password":"Devinemoi_01"}' % getUsername()
		requestLogin = requests.post('%sr0/login' %getAddr(), data=dataLogin, verify=True)

		self.assertEquals(200,requestLogin.status_code)

		body = (requestLogin.text).split("\"")
		login_token = body[3]

		setLoginToken(login_token)

		

if __name__ == '__main__':
	print "\n\n\033[1;32;40mtest_Login : \n\n\033[1;32;m"
	print "Verify if the user can login in this homeserver."
	unittest.main()
