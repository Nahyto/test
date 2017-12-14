
import sys
my_args = sys.argv[1:]
del sys.argv[1:]

verbose = ""
email = ""
domain = ""
test = ""

if len(my_args) == 3:
	verbose = my_args[1]
	email = my_args[0]
	domain = my_args[2]

elif len(my_args) == 2:
	email = my_args[0]
	domain = my_args[1]

print verbose
print email
print domain