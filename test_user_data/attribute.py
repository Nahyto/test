import random
import string
from automate import getInfra

__addr = 'https://%s-test.citadel.team/_matrix/client/' %getInfra()

print getInfra()

__username = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(7))

def getAddr():
	return __addr

def getUsername():
	return __username