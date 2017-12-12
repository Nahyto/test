import requests
import urllib3
import unittest
from test_Register import getAccesToken
from attribute import getUsername,getAddr

class test3pid(unittest.TestCase):

	def test_3pid(self):

		headers = {
   			'Content-Type': 'application/json',
    		'Accept': 'application/json',
		}

		params = {
			('acces_token',getAccesToken())
		}

		data3pid = '{"bind":false,"three_pid_creds":{"client_secret":"someSecret","id_server":"localhost","sid":"abc123987"}}'
		requestPost3pid = requests.post('%sr0/account/3pid' % getAddr(),headers=headers,params=params,data=data3pid, verify=False)
		self.assertEquals(401,requestPost3pid.status_code)

		requestGet3pid = requests.get('%sr0/account/3pid' % getAddr(),headers=headers,params=params, verify=False)
		self.assertEquals(401,requestGet3pid.status_code)

		print "\ntest_3pid: \n\n Create and Gets a list of the third party identifiers that the homeserver has associated with the user's account."

if __name__ == '__main__':
	unittest.main()
