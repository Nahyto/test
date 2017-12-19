import requests
import urllib3
import urllib
import unittest
from attribute import *

class testDisplayName(unittest.TestCase):

	
	
	def test_Put_Display_Name(self):
		global user_id
		global params

		params = (
        		('access_token', getAccessToken()),
        	)

		user_id = "@" + getUsername() + ":" + getDomain()
	    user_id = urllib.quote("%s" % (user_id))
 
		dataDisplayName = '{"displayname":"Jean richard"}'
		requestPutDisplayName = requests.put('%sclient/r0/profile/%s/displayname' %(getAddr(),user_id), headers=getHeader(), params=params,data=dataDisplayName, verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestPutDisplayName.text
		
		if requestGetDisplayName.status_code == 200:
			print "\n\n\033[32;40mSuccess !\n\033[32;m"
			self.assertEquals(200,requestPutDisplayName.status_code)

		else:
			print "\n\033[32;31mRequest rate-limited !\n\033[32;m"
			self.assertEquals(429,requestPutDisplayName.status_code)





	def test_Put_Get_Display_Name(self):

		requestGetDisplayName = requests.get('%sclient/r0/profile/%s/displayname' %(getAddr(),user_id), verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestGetDisplayName.text
		
		if requestGetDisplayName.status_code == 404:
			print "\n\033[32;31mThere is no display name for this user or this user does not exist !\n\033[32;m"
			self.assertEquals(404,requestGetDisplayName.status_code)

		else:
			print "\n\n\033[32;40mSuccess !\n\033[32;m"
			self.assertEquals(200,requestGetDisplayName.status_code)




	def test_Put_Get_Put_Display_Name(self):
		
		dataDisplayName = '{"displayname":"Jean Armand"}'
		requestPutDisplayName = requests.put('%sclient/r0/profile/%s/displayname' %(getAddr(),user_id), headers=getHeader(), params=params,data=dataDisplayName, verify=True)
		
		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestPutDisplayName.text
		

		if requestPutDisplayName.status_code == 200:
			print "\n\n\033[32;40mAwkward the request worked...\n\033[32;m"
			self.assertEquals(200,requestPutDisplayName.status_code)
		elif requestPutDisplayName.status_code == 401:
			print "\n\033[32;31mYou can't change your display_name twice as a guest !\n\033[32;m"
			self.assertEquals(401,requestPutDisplayName.status_code)

		else:
			print "\n\033[32;31mRequest rate-limited !\n\033[32;m"
			self.assertEquals(429,requestPutDisplayName.status_code)


	
	def test_User_Change_Display_Name_Admin(self):

		user = raw_input("Write the Username of the guest you wanted to change his display_name : ")
        user_id = "@" + user + ":" + getDomain()
        user_id = urllib.quote("%s" % (user_id))

        dataDisplayName = '{"displayname":"Jean Armand"}'
        requestPutDisplayName = requests.put('https://%s:8443/_matrix/adminhs/r0/profiledspn/%s' %(getDomain(),user_id), headers=getHeader(), params=params,data=dataDisplayName, verify=True)

   	    if getVerbose() == '1':
  			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestPutDisplayName.text

        if requestPutDisplayName.status_code == 200:
			print "\n\n\033[32;40mAwkward the request worked...\n\033[32;m"
			self.assertEquals(200,requestPutDisplayName.status_code)
		elif requestPutDisplayName.status_code == 401:
			print "\n\033[32;31mYou can't change change the display_name of another guest !\n\033[32;m"
			self.assertEquals(401,requestPutDisplayName.status_code)

		else:
			print "\n\033[32;31mRequest rate-limited !\n\033[32;m"
			self.assertEquals(429,requestPutDisplayName.status_code)



	
	def test_User_Change_Display_Name_Guest(self):
        
        dataDisplayName = '{"displayname":"Jean Armand"}'
        requestPutDisplayName = requests.put('https://%s:8443/_matrix/adminhs/r0/profiledspn/%s' %(getDomain(),user_id), headers=getHeader(), params=params,data=dataDisplayName, verify=True)

       	if getVerbose() == '1':
       		print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestPutDisplayName.text

        if requestPutDisplayName.status_code == 200:
			print "\n\n\033[32;40mAwkward the request worked...\n\033[32;m"
			self.assertEquals(200,requestPutDisplayName.status_code)
		elif requestPutDisplayName.status_code == 401:
			print "\n\033[32;31mYou can't change change the display_name of another guest !\n\033[32;m"
			self.assertEquals(401,requestPutDisplayName.status_code)

		else:
			print "\n\033[32;31mRequest rate-limited !\n\033[32;m"
			self.assertEquals(429,requestPutDisplayName.status_code)




if __name__ == '__main__':
	print "\ntest_Display_Name : \n"
	print "Put and Get the user's display name."
	unittest.main()
