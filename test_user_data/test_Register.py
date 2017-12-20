import random
import string
import requests
import urllib3
import unittest
import sys
import subprocess
from attribute import *

class testRegister(unittest.TestCase):


	def test_Request_Token(self):
		print "Send the request token at the email your write."
		global requestRegisterEmail

		dataRegisterEmail = '{"client_secret":"abcd","id_server":"%s","send_attempt":"1","email":"%s","next_link":""}' %(getDomain(),getEmail())

		requestRegisterEmail = requests.post('%sclient/r0/register/email/requestToken' %getAddr(), headers=getHeader(), data=dataRegisterEmail)

		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\033[1;32;m" %requestRegisterEmail.text

		if "M_THREEPID_IN_USE" in requestRegisterEmail.text:
			print "\n\033[32;31mEmail already used !\n\033[32;m"
			self.assertEquals(400,requestRegisterEmail.status_code)

		elif "M_SERVER_NOT_TRUSTED" in requestRegisterEmail.text:
			print "\n\033[32;31mThe homeserver doesn't trust this server !\n\033[32;m"
			self.assertEquals(400,requestRegisterEmail.status_code)
		else:
			print "\n\n\033[32;40mSuccess !\n\033[32;m"
			self.assertEquals(200,requestRegisterEmail.status_code)

		
	def test_Submit_Token(self):
		print "Submit the request token at the server."
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

		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\033[1;32;m" %requestValidate.text

		if "true" in requestValidate.text:
			print "\n\n\033[32;40mSuccess !\n\033[32;m" 
			self.assertIn("true",requestValidate.text)
		
		else:
			print "\n\033[32;31mSomething goes wrong with the validation...\n\033[32;m"
			self.assertIn("false",requestValidate.text)




	def test_User_Register(self):
		print "Register the user with the email."
		
		dataRegisterUser = '{"auth": {"type": "m.login.email.identity","threepid_creds":{"id_server": "%s","sid": "%s","client_secret": "abcd"}},"bind_email": true,"password": "Devinemoi_01","username": "%s"}' %(getDomain(),sid,getUsername())
		requestRegisterUser = requests.post('%sclient/r0/register' %getAddr(), headers=getHeader(), data=dataRegisterUser, verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\033[1;32;m" %requestRegisterUser.text

		if "M_USER_IN_USE" in requestRegisterUser.text:
			print "\n\033[32;31mUsername already used !\n\033[32;m"
			self.assertEquals(400,requestRegisterUser.status_code)

		elif "M_INVALID_USERNAME" in requestRegisterUser.text:
			print "\n\033[32;31mYour username is invalid !\n\033[32;m"
			self.assertEquals(400,requestRegisterUser.status_code)

		elif "M_EXCLUSIVE" in requestRegisterUser.text:
			print "\n\033[32;31mUsername has an invalid syntax !\n\033[32;m"
			self.assertEquals(400,requestRegisterUser.status_code)

		elif "flows" in requestRegisterUser.text:
			print "\n\033[32;31mThe registration needs more informations !\n\033[32;m"
			self.assertEquals(401,requestRegisterUser.status_code)

		elif requestRegisterUser.status_code == 200:
			print "\n\n\033[32;40mSuccess !\n\033[32;m"
			self.assertEquals(200,requestRegisterUser.status_code)

		else:
			print "\n\033[32;31mRequest rate-limited !\n\033[32;m"
			self.assertEquals(429,requestRegisterUser.status_code)
		
		






if __name__ == '__main__':
	print "\n\033[32;40mtest_Register :\033[32;m \n"
	print "Register for an account on this homeserver."
	print "There are two kinds of user account:"
	print "\033[32;33m    -user accounts.\033[32;m These accounts may use the full API described in this specification. "
	print "\033[32;33m    -guest accounts.\033[32;m These accounts may have limited permissions and may not be supported by all servers.\n\n"
	unittest.main()
