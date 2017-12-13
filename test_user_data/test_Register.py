import random
import string
import requests
import urllib3
import unittest
import sys
import subprocess
from attribute import getUsername

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
my_args = sys.argv[1:]
del sys.argv[1:]

class testRegister(unittest.TestCase):

	def test_Register(self):

		headers = {
 	   		'Content-Type': 'application/json',
    		'Accept': 'application/json',
		}

		addr = 'https://%s.citadel.team/_matrix/client/' %my_args[0]

		dataRegisterEmail = '{"client_secret":"abcd","id_server":"%s.citadel.team","send_attempt":"1","email":"%s@outlook.fr","next_link":""}' %(my_args[0],getUsername())
		requestRegisterEmail = requests.post('%sr0/register/email/requestToken' %addr, headers=headers, data=dataRegisterEmail)
		self.assertEquals(200,requestRegisterEmail.status_code)
		bodyEmail = (requestRegisterEmail.text).split('"')
		sid = bodyEmail[5]
		
		domain = (my_args[0]).split("-")
		registerToken = subprocess.check_output("ssh -i ~/team-playbook/ssh/id_rsa ansible@back-%s.tcs-citadeldev.cloud-omc.org \"docker exec sydent-container sqlite3 /opt/sydent/database/sydent.db 'select * from threepid_token_auths where validationSession=%s'\" | cut -d'|' -f3" %(domain[0],sid),shell=True).strip()
		params = (
    		('token', '%s' %registerToken),
    		('client_secret', 'abcd'),
   	 		('sid', '%s' %sid)
		)
		requestValidate = requests.post('https://%s.citadel.team/_matrix/identity/api/v1/validate/email/submitToken' %my_args[0], params=params)
		self.assertIn("true",requestValidate.text)

		dataRegisterUser = '{"auth": {"type": "m.login.email.identity","threepid_creds":{"id_server": "%s.citadel.team","sid": "%s","client_secret": "abcd"}},"bind_email": true,"password": "Devinemoi_01","username": "%s"}' %(my_args[0],sid,getUsername())
		requestRegisterUser = requests.post('https://%s.citadel.team/_matrix/client/r0/register' %my_args[0], headers=headers, data=dataRegisterUser, verify=True)
		self.assertEquals(200,requestRegisterUser.status_code)
		bodyUser = (requestRegisterUser.text).split("\"")
		access_token = bodyUser[3]

		fileAccessToken = open("fileAccessToken.txt","w")
		fileAccessToken.write(access_token)
		fileAccessToken.write("\n%s" %getUsername())
		fileAccessToken.close()

		print "\ntest_Register : \n\nRegister for an account on this homeserver.\nThere are two kinds of user account:\n    -user accounts. These accounts may use the full API described in this specification. \n    -guest accounts. These accounts may have limited permissions and may not be supported by all servers."
		if my_args[1] == '1':
			print "\nResponse server :\n%s\n" %requestRegisterUser.text


if __name__ == '__main__':
	unittest.main()
