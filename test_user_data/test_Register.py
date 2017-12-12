import random
import string
import requests
import urllib3
import unittest
from attribute import getUsername,getAddr

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__data = '{\"username\":\"%s\", \"password\":\"devine\", \"auth\":{\"type\":\"m.login.dummy\"}}' % getUsername()

requestRegister = requests.post('%sr0/register' %getAddr(), data=__data, verify=False)

__body = (requestRegister.text).split('"')

__access_token = __body[3]

__user_id = __body[11]

class testRegister(unittest.TestCase):

	def test_Register(self):
		self.assertEquals(200,requestRegister.status_code)
		print "\ntest_Register : \n\nRegister for an account on this homeserver.\nThere are two kinds of user account:\n    -user accounts. These accounts may use the full API described in this specification. \n    -guest accounts. These accounts may have limited permissions and may not be supported by all servers."
		

def getAccesToken():
	return __access_token

def getUserID():
	return __user_id

if __name__ == '__main__':
	unittest.main()