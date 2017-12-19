import requests
import urllib3
import unittest
import sys
import getpass
from attribute import *


class testDesactivate(unittest.TestCase):

	"""def test_Desactivate_User_Himself(self):

		global params
		lock = 1
		pwd = ""
		
		while lock:
			pwd = getpass.getpass("Write your password : ")

			if pwd == '':
				lock = 1

			else:
				lock = 0

		params = (
    		('access_token', getAccessToken()),
		)

		dataDeactivate = '{"auth": {"user":"%s","password":"%s","session":"bidule","type": "m.login.password"}}' %(getUsername(),pwd)
		requestDeactivate = requests.post('%sclient/r0/account/deactivate' %getAddr(), headers=getHeader(), params=params, data=dataDeactivate, verify=True)

		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestDeactivate.text

		
		if "flows" in requestDeactivate.text:
			print "\n\033[32;31mThe registration needs more informations !\n\033[32;m"
			self.assertEquals(401,requestDeactivate.status_code)
		
		elif requestDeactivate.status_code == 200:
			print "\n\n\033[32;40mSuccess !\n\033[32;m"
			self.assertEquals(200,requestDeactivate.status_code)

		else:
			print "\n\033[32;31mRequest rate-limited !\n\033[32;m"
			self.assertEquals(429,requestDeactivate.status_code)



	def test_Admin_Desactivate_User(self):

		user = raw_input("Write the Username of the guest you wanted to deactivate : ")
		user_id = "@" + user + ":" + getDomain()
		user_id = urllib.quote("%s" % (user_id))

		dataDeactivate = '{"target_user_id":"%s"}' %(user_id)
		requestDeactivate = requests.post('https://%s:8443/_matrix/adminhs/unstable/account/deactivate' %getDomain(), headers=getHeader(), params=params, data=dataDeactivate, verify=True)

		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestDeactivate.text

		
		if "flows" in requestDeactivate.text:
			print "\n\033[32;31mThe registration needs more informations !\n\033[32;m"
			self.assertEquals(401,requestDeactivate.status_code)
		
		elif requestDeactivate.status_code == 200:
			print "\n\n\033[32;40mSuccess !\n\033[32;m"
			self.assertEquals(200,requestDeactivate.status_code)

		else:
			print "\n\033[32;31mRequest rate-limited !\n\033[32;m"
			self.assertEquals(429,requestDeactivate.status_code)"""


	def test_User_Desactivate_User(self):

		user = raw_input("Write the Username of the guest you wanted to deactivate : ")
		user_id = "@" + user + ":" + getDomain()
		user_id = urllib.quote("%s" % (user_id))
		lock = 1
		pwd = ""
		
		while lock:
			pwd = getpass.getpass("Write the password of the other user: ")

			if pwd == '':
				lock = 1

			else:
				lock = 0

		params = (
    		('access_token', getAccessToken()),
		)

		dataDeactivate = '{"auth": {"user":"%s","password":"%s","session":"bidule","type": "m.login.password"}}' %(user,pwd)
		requestDeactivate = requests.post('%sclient/r0/account/deactivate' %getAddr(), headers=getHeader(), params=params, data=dataDeactivate, verify=True)

		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestDeactivate.text

		
		if "flows" in requestDeactivate.text:
			print "\n\033[32;31mThe registration needs more informations !\n\033[32;m"
			self.assertEquals(401,requestDeactivate.status_code)
		
		elif requestDeactivate.status_code == 200:
			print "\n\n\033[32;40mSuccess !\n\033[32;m"
			self.assertEquals(200,requestDeactivate.status_code)

		else:
			print "\n\033[32;31mRequest rate-limited !\n\033[32;m"
			self.assertEquals(429,requestDeactivate.status_code)


if __name__ == '__main__':
	print "\n\n\033[1;32;40mtest_Desactivate : \n\n\033[1;32;m"
	print "Deactivate the user's account, removing all ability for the user to login again.\n\n"
	unittest.main()
