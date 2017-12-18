import requests
import urllib3
import urllib
import unittest
from attribute import *

class testDisplayName(unittest.TestCase):

	def test_Display_Name(self):

		user_id = "@" + getUsername() + ":" + getDomain()
		user_id = urllib.quote("%s" % (user_id))

		params = (
    		('access_token', getAccessToken()),
		)

		dataDisplayName = '{"displayname":"Jean richard"}'
		requestPutDisplayName = requests.put('%sclient/r0/profile/%s/displayname' %(getAddr(),user_id), headers=getHeader(), params=params,data=dataDisplayName, verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestPutDisplayName.text
		
		self.assertEquals(200,requestPutDisplayName.status_code)

		requestGetDisplayName = requests.get('%sclient/r0/profile/%s/displayname' %(getAddr(),user_id), verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestGetDisplayName.text
		
		self.assertEquals(200,requestGetDisplayName.status_code)

		dataDisplayName = '{"displayname":"Jean Armand"}'
		requestPutDisplayName = requests.put('%sclient/r0/profile/%s/displayname' %(getAddr(),user_id), headers=getHeader(), params=params,data=dataDisplayName, verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestPutDisplayName.text

		self.assertEquals(200,requestPutDisplayName.status_code)




if __name__ == '__main__':
	print "\ntest_Display_Name : \n"
	print "Put and Get the user's display name."
	unittest.main()
