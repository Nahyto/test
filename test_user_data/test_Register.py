import random
import string
import requests
import urllib3
import unittest
import sys
import subprocess
from attribute import *

class testRegister(unittest.TestCase):


	def test_Register_Email(self):
		global requestRegisterEmail
		dataRegisterEmail = '{"client_secret":"abcd","id_server":"%s","send_attempt":"1","email":"%s","next_link":""}' %(getDomain(),getEmail())

		requestRegisterEmail = requests.post('%sclient/r0/register/email/requestToken' %getAddr(), headers=getHeader(), data=dataRegisterEmail)

		self.assertEquals(200,requestRegisterEmail.status_code)

	def test_Wegister_User(self):
		dataRegisterUser = '{"auth": {"type": "m.login.email.identity","threepid_creds":{"id_server": "%s","sid": "%s","client_secret": "abcd"}},"bind_email": true,"password": "Devinemoi_01","username": "%s"}' %(getDomain(),sid,getUsername())
		requestRegisterUser = requests.post('%sclient/r0/register' %getAddr(), headers=getHeader(), data=dataRegisterUser, verify=True)
		self.assertEquals(200,requestRegisterUser.status_code)
		bodyUser = (requestRegisterUser.text).split("\"")
		access_token = bodyUser[3]

		fileAccessToken = open("fileAccessToken.txt","w")
		fileAccessToken.write(access_token)
		fileAccessToken.close()

		print "\ntest_Register : \n\nRegister for an account on this homeserver.\nThere are two kinds of user account:\n    -user accounts. These accounts may use the full API described in this specification. \n    -guest accounts. These accounts may have limited permissions and may not be supported by all servers."
		if getVerbose() == '1':
			print "\nResponse server :\n%s\n" %requestRegisterUser.text
		
	def test_Validate_Email(self):
		global sid

		bodyEmail = (requestRegisterEmail.text).split('"')
		sid = bodyEmail[5]

		registerToken = subprocess.check_output("ssh -i ~/team-playbook/ssh/id_rsa ansible@back-%s.tcs-citadeldev.cloud-omc.org \"docker exec sydent-container sqlite3 /opt/sydent/database/sydent.db 'select * from threepid_token_auths where validationSession=%s'\" | cut -d'|' -f3" %(getInfra(),sid),shell=True).strip()
		
		params = (
    		('token', registerToken),
    		('client_secret', 'abcd'),
   	 		('sid', sid),
		)

		requestValidate = requests.post('%sidentity/api/v1/validate/email/submitToken' %getAddr(), params=params)

		self.assertIn("true",requestValidate.text)


if __name__ == '__main__':
	unittest.main()
