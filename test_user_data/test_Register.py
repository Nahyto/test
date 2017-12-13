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

		dataRegister = '{"client_secret":"abcd","id_server":"%s-test.citadel.team","send_attempt":"1","email":"%s@outlook.fr","next_link":""}' %(my_args[0],getUsername())
		requestRegister = requests.post('%sr0/register/email/requestToken' %addr, headers=headers, data=dataRegister)
		self.assertEquals(403,requestRegister.status_code)
		
		body = (requestRegister.text).split('"')
		sid = body[2]

		registerToken = subprocess.check_output("ssh -i ~/team-playbook/ssh/id_rsa ansible@back-%s.tcs-citadeldev.cloud-omc.org \"docker exec sydent-container sqlite3 /opt/sydent/database/sydent.db 'select * from threepid_token_auths where validationSession=$%s'\" | cut -d'|' -f3" %(my_args[0],sid),shell=True)
		params = (
    		('token', registerToken),
    		('client_secret', 'abcd'),
    		('sid', sid),
		)

		requestValidate = requests.post('https://%s.citadel.team/_matrix/identity/api/v1/validate/email/submitToken' %my_args[0], params=params)
		self.assertIn("True",requestValidate.text)

		print "\ntest_Register : \n\nRegister for an account on this homeserver.\nThere are two kinds of user account:\n    -user accounts. These accounts may use the full API described in this specification. \n    -guest accounts. These accounts may have limited permissions and may not be supported by all servers."
		if my_args[1] == '1':
			print "\nResponse server :\n%s\n" %requestRegister.text


if __name__ == '__main__':
	unittest.main()