import requests
import urllib3
import unittest
from test_Register import getAccesToken,getUserID
from attribute import getUsername,getAddr

class testDisplayName(unittest.TestCase):

	def test_Display_Name(self):

		headers = {
   			'Content-Type': 'application/json',
    		'Accept': 'application/json',
		}

		params = (
    		('access_token', getAccesToken()),
		)

		dataDisplayName = '{"displayname":"Jean richard"}'
		requestPutDisplayName = requests.put('%sr0/profile/%s/displayname' %(getAddr(),getUserID()), headers=headers, params=params,data=dataDisplayName, verify=False)
		self.assertEquals(200,requestPutDisplayName.status_code)

		requestGetDisplayName = requests.get('%sr0/profile/%s/displayname' %(getAddr(),getUserID()), verify=False)
		self.assertEquals(200,requestGetDisplayName.status_code)
		print "\ntest_Display_Name : \n\nPut and Get the user's display name."


if __name__ == '__main__':
	unittest.main()