import requests
import urllib3
import urllib
import unittest
from attribute import *

class testDisplayNameAdmin(unittest.TestCase):

	
	
	def test_Put_Display_Name_Admin(self):
		params = (
        		('access_token', getAccessToken()),
        	)

		user_id = "@" + getUsername() + ":" + getDomain()
	        user_id = urllib.quote("%s" % (user_id))
 
		dataDisplayName = '{"displayname":"Jean richard"}'
		requestPutDisplayName = requests.put('%sadmin/r0/profile/%s/displayname' %(getAddr(),user_id), headers=getHeader(), params=params,data=dataDisplayName, verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestPutDisplayName.text
		
		self.assertEquals(200,requestPutDisplayName.status_code)




	def test_Put_Get_Display_Name_Admin(self):	
		params = (
                        ('access_token', getAccessToken()),
                )

		user_id = "@" + getUsername() + ":" + getDomain()
	        user_id = urllib.quote("%s" % (user_id))

		requestGetDisplayName = requests.get('%sadmin/r0/profile/%s/displayname' %(getAddr(),user_id), verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestGetDisplayName.text
		
		self.assertEquals(200,requestGetDisplayName.status_code)




	def test_Put_Get_Put_Display_Name_Admin(self):
		params = (
                        ('access_token', getAccessToken()),
                )

		user_id = "@" + getUsername() + ":" + getDomain()
	        user_id = urllib.quote("%s" % (user_id))
		
		dataDisplayName = '{"displayname":"Jean Armand"}'
		requestPutDisplayName = requests.put('%sadmin/r0/profile/%s/displayname' %(getAddr(),user_id), headers=getHeader(), params=params,data=dataDisplayName, verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestPutDisplayName.text


		self.assertEquals(401,requestPutDisplayName.status_code)



	def test_Put_Get_Put_Get_Display_Name_Admin(self):	
		params = (
                        ('access_token', getAccessToken()),
                )

		user_id = "@" + getUsername() + ":" + getDomain()
	    user_id = urllib.quote("%s" % (user_id))

		requestGetDisplayName = requests.get('%sadmin/r0/profile/%s/displayname' %(getAddr(),user_id), verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestGetDisplayName.text
		
		self.assertEquals(200,requestGetDisplayName.status_code)




if __name__ == '__main__':
	print "\ntest_Display_Name : \n"
	print "Put and Get the user's display name."
	unittest.main()