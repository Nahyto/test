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
 		print 'https://%s:8443/_matrix/adminhs/r0/profiledspn/%s' %(getDomain(),user_id)
		dataDisplayName = '{"displayname":"Jean richard"}'
		requestPutDisplayName = requests.put('https://%s:8443/_matrix/adminhs/r0/profiledspn/%s' %(getDomain(),user_id), headers=getHeader(), params=params,data=dataDisplayName, verify=True)
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestPutDisplayName.text
		
		self.assertEquals(200,requestPutDisplayName.status_code)




	def test_Put_Get_Display_Name_Admin(self):	
		params = (
                        ('access_token', getAccessToken()),
                )

		user_id = "@" + getUsername() + ":" + getDomain()
	        user_id = urllib.quote("%s" % (user_id))

		requestGetDisplayName = requests.get('https://%s:8443/_matrix/adminhs/r0/profiledspn/%s' %(getDomain(),user_id), verify=True)
		
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
		requestPutDisplayName = requests.put('https://%s:8443/_matrix/adminhs/r0/profiledspn/%s' %(getDomain(),user_id), headers=getHeader(), params=params,data=dataDisplayName, verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestPutDisplayName.text


		self.assertEquals(200,requestPutDisplayName.status_code)



	def test_Put_Get_Put_Get_Display_Name_Admin(self):	
		params = (
                        ('access_token', getAccessToken()),
                )

		user_id = "@" + getUsername() + ":" + getDomain()
		user_id = urllib.quote("%s" % (user_id))

		requestGetDisplayName = requests.get('https://%s:8443/_matrix/adminhs/r0/profiledspn/%s' %(getDomain(),user_id), verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestGetDisplayName.text
		
		self.assertEquals(200,requestGetDisplayName.status_code)

	

	def test_Change_Display_Name_Guest(self):
		params = (
                        ('access_token', getAccessToken()),
                )

		user = raw_input("Write the Username of the guest you wanted to change his display_name : ")
		user_id = "@" + user + ":" + getDomain()
		user_id = urllib.quote("%s" % (user_id))

		dataDisplayName = '{"displayname":"Jean Tristan"}'
		requestPutDisplayName = requests.put('https://%s:8443/_matrix/adminhs/r0/profiledspn/%s' %(getDomain(),user_id), headers=getHeader(), params=params,data=dataDisplayName, verify=True)
		
                if getVerbose() == '1':
                        print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestPutDisplayName.text

                self.assertEquals(200,requestPutDisplayName.status_code)

		requestPutDisplayName = requests.put('%sclient/r0/profile/%s/displayname' %(getAddr(),user_id), headers=getHeader(), params=params,data=dataDisplayName, verify=True)

		if getVerbose() == '1':
                        print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestPutDisplayName.text

       	       self.assertEquals(401,requestPutDisplayName.status_code)
		


if __name__ == '__main__':
	print "\ntest_Display_Name : \n"
	print "Put and Get the user's display name."
	unittest.main()
