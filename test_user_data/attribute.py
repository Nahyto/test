
import sys
my_args = sys.argv[1:]
del sys.argv[1:]

__verbose = ""
__email = ""
__domain = ""

if len(my_args) == 3:
	__verbose = my_args[1]
	__email = my_args[0]
	__domain = my_args[2]

elif len(my_args) == 2:
	__email = my_args[0]
	__domain = my_args[1]

__infra = (__domain.split(".")[0]).split("-")[0]
__username = __email.split("@")[0]
__addr = 'https://%s/_matrix/' %__domain
__headers = {
 	'Content-Type': 'application/json',
 	'Accept': 'application/json',
}

def getVerbose():
	return __verbose

def getEmail():
	return __email

def getDomain():
	return __domain

def getInfra():
	return __infra

def getUsername():
	return __username

def getAddr():
	return __addr

def getHeader():
	return __headers