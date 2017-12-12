import requests
import urllib3
import unittest
from test_Register import getAccesToken,getUserID
from attribute import getAddr

class testAvatar(unittest.TestCase):

	def test_Avatar(self):

		headers = {
   			'Content-Type': 'application/json',
    		'Accept': 'application/json',
		}

		params = (
    		('access_token', getAccesToken()),
		)

		data = 'https://images.sk-static.com/images/media/profile_images/artists/381562/huge_avatar'
		requestPutAvatar = requests.put('%sr0/profile/%s/avatar_url'%(getAddr(),getUserID()), headers=headers, params=params, data=data, verify=False)
		self.assertEquals(400,requestPutAvatar.status_code)

		requestGetAvatar = requests.get('%sr0/profile/%s/avatar_url' %(getAddr(),getUserID()), verify=False)
		self.assertEquals(200,requestGetAvatar.status_code)
		print "\ntest_Avatar : \n\nPut and Get the user's avatar URL."

if __name__ == '__main__':
	unittest.main()