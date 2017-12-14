import sys
my_args = sys.argv[1:]
del sys.argv[1:]

def initList():

	listInitVar = []
	verbose = 0
	email = ""
	domain = ""
	infra = ""
	username = ""
	addr = ""
	access_token = ""
	login_token = ""
	headers = {
 	'Content-Type': 'application/json',
 	'Accept': 'application/json',
	}

	listInitVar.append(verbose)
	listInitVar.append(email)
	listInitVar.append(domain)
	listInitVar.append(infra)
	listInitVar.append(username)
	listInitVar.append(addr)
	listInitVar.append(headers)
	listInitVar.append(access_token)
	listInitVar.append(login_token)
	
	return listInitVar

def instantiateList(listInitVar):

	if len(my_args) == 3:
		listInitVar[0] = my_args[0]
		listInitVar[1] = my_args[1]
		listInitVar[2] = my_args[2]

	elif len(my_args) == 2:
		listInitVar[1] = my_args[1]
		listInitVar[2] = my_args[2]

	listInitVar[3] = (listInitVar[2].split(".")[0]).split("-")[0]
	listInitVar[4] = listInitVar[1].split("@")[0]
	listInitVar[5] = 'https://%s/_matrix/' %listInitVar[2]

	return listInitVar 

listArguments = instantiateList(initList())

def getVerbose():
	return listArguments[0]

def getEmail():
	return listArguments[1]

def getDomain():
	return listArguments[2]

def getInfra():
	return listArguments[3]

def getUsername():
	return listArguments[4]

def getAddr():
	return listArguments[5]

def getHeader():
	return listArguments[6]

def setAccessToken(access_token):
	listArguments[7] = access_token

def getAccessToken():
	return listArguments[7]

def setLoginToken(login_token):
	listArguments[8] = login_token

def getLoginToken():
	return listArguments[8]