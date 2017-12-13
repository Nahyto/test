import random
import string


__username = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(7))


def getUsername():
	return __username