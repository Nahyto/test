import random
import string
import requests
import urllib3
import urllib
import sys
import unittest
import os
import paramiko
import subprocess
from attribute import *

class testLogout(unittest.TestCase):

	"""def test_Logout(self):
			params = (
    			('access_token', getAccessToken()),
		)
		user_id = "@" + getUsername() + ":" + getDomain()
		user_id = urllib.quote("'%s'" % (term))
		test = subprocess.check_output("ssh -i ~/team-playbook/ssh/id_rsa ansible@back-jla.tcs-citadeldev.cloud-omc.org \"docker exec -t bdd-container psql synapse --command 'SELECT token FROM access_tokens WHERE user_id = %s;'\"" %user_id,shell=True)
		print test
		requestLogout = requests.post('%sclient/r0/logout' %getAddr(), params=params, verify=True)

		if getVerbose() == '1':
			print "\n\033[1;32;40mResponse server :\033[1;32;36m\n%s\n\n\033[1;32;m" %requestLogout.text

		self.assertEquals(200,requestLogout.status_code)"""

	client = None
 
    def __init__(self):
    	k = paramiko.RSAKey.from_private_key_file("~/team-playbook/ssh/id_rsa")
        print("Connecting to server.")
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect("back-jla.tcs-citadeldev.cloud-omc.org", username='ansible', pkey = k)
 
    def sendCommand(self):
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command("docker exec -t bdd-container psql synapse --command \"SELECT token FROM access_tokens WHERE user_id = '@nelsonthales59147:jla-test.citadel.team';\"")
            while not stdout.channel.exit_status_ready():
                # Print data when available
                if stdout.channel.recv_ready():
                    alldata = stdout.channel.recv(1024)
                    prevdata = b"1"
                    while prevdata:
                        prevdata = stdout.channel.recv(1024)
                        alldata += prevdata
 
                    print(str(alldata, "utf8"))
        else:
            print("Connection not opened.")
		

if __name__ == '__main__':
	print "\n\n\033[1;32;40mtest_Logout: \n\n\033[1;32;m"
	print "Verify if the user can Logout from this homeserver.\n\n"
	unittest.main()
