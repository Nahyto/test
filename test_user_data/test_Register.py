import random
import string
import requests
import urllib3
import unittest
import sys
import subprocess

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
my_args = sys.argv[1:]
del sys.argv[1:]

class testRegister(unittest.TestCase):

	def test_Register(self):

		verbose = ""
		email = ""
		domain = ""
		infra = ""
		if len(my_args) == 3:
			verbose = my_args[1]
			email = my_args[0]
			domain = my_args[2]

		elif len(my_args) == 2:
			email = my_args[0]
			domain = my_args[1]

		infra = domain.split(".")[0]
		username = email.split("@")[0]

		headers = {
 	   		'Content-Type': 'application/json',
    		'Accept': 'application/json',
		}

		addr = 'https://%s/_matrix/client/' %domain

		dataRegisterEmail = '{"client_secret":"abcd","id_server":"%s","send_attempt":"1","email":"%s","next_link":""}' %(domain,email)
		requestRegisterEmail = requests.post('%sr0/register/email/requestToken' %addr, headers=headers, data=dataRegisterEmail)
		self.assertEquals(200,requestRegisterEmail.status_code)
		bodyEmail = (requestRegisterEmail.text).split('"')
		sid = bodyEmail[5]
		
		registerToken = subprocess.check_output("ssh -i ~/team-playbook/ssh/id_rsa ansible@back-%s.tcs-citadeldev.cloud-omc.org \"docker exec sydent-container sqlite3 /opt/sydent/database/sydent.db 'select * from threepid_token_auths where validationSession=%s'\" | cut -d'|' -f3" %(infra,sid),shell=True).strip()
		params = (
    		('token', '%s' %registerToken),
    		('client_secret', 'abcd'),
   	 		('sid', '%s' %sid),
		)
		requestValidate = requests.post('https://%s/_matrix/identity/api/v1/validate/email/submitToken' %domain, params=params)
		self.assertIn("true",requestValidate.text)

		dataRegisterUser = '{"auth": {"type": "m.login.email.identity","threepid_creds":{"id_server": "%s","sid": "%s","client_secret": "abcd"}},"bind_email": true,"password": "Devinemoi_01","username": "%s"}' %(domain,sid,username)
		requestRegisterUser = requests.post('https://%s/_matrix/client/r0/register' %domain, headers=headers, data=dataRegisterUser, verify=True)
		self.assertEquals(200,requestRegisterUser.status_code)
		bodyUser = (requestRegisterUser.text).split("\"")
		access_token = bodyUser[3]

		fileAccessToken = open("fileAccessToken.txt","w")
		fileAccessToken.write(access_token)
		fileAccessToken.write("\n%s" %username)
		fileAccessToken.close()

		print "\ntest_Register : \n\nRegister for an account on this homeserver.\nThere are two kinds of user account:\n    -user accounts. These accounts may use the full API described in this specification. \n    -guest accounts. These accounts may have limited permissions and may not be supported by all servers."
		if verbose == '1':
			print "\nResponse server :\n%s\n" %requestRegisterUser.text


if __name__ == '__main__':
	unittest.main()
