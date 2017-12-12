import random
import string

__addr = 'https://jla-test.citadel.team/_matrix/client/'

__username = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(7))

def getAddr():
	return __addr

def getUsername():
	return __username