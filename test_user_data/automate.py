import os, sys
import subprocess


def run_test():
	verbose = 0
	varAll = 0
	test_file = []
	infra = ""

	if len(sys.argv) == 1:
		print "\nHello this is the automate-test 1.0 : If you want to execute some tests,\nYou can choose between this 2 options: \n    -v [Name of your test] : With that you can see the body response from the server\n    -a : With this you can run all tests\nIf you want to run one particular test, just write \"python automate.py --options [Name of your test]\".\nEnjoy ! \n"
	
	elif len(sys.argv) > 1:
		for args in sys.argv[1:]:
			if args == "-v":
				verbose = 1
			elif args == "-a":
				varAll = 1
			elif args.endswith(".py"):
				test_file.append(args)
			else:
				print "\nThere is a mistakes somewhere : check if you right correctly the options or the name of the test_file, and if the test_file is in the end of the arguments ! \n"

		if varAll == 1:
			if len(test_file) != 0:
				print "\nYou can't ask to execute one test if you select the options -a !\n"
			else:
				infra = raw_input("Write the name of your infra (Example: \"jla-test\") : ")
				for test in os.listdir("."):
					if test != "automate.py":
						subprocess.call("python %s" %(test),shell=True)

		else:
			if len(test_file) == 0:
				print "\nIf you didn't ask for running all tests, you have to write a test_file\n"
			else:
				infra = raw_input("Write the name of your infra (Example: \"jla-test\") : ")
				for test in test_file:
					subprocess.call("python %s %s %s" %(test,infra,verbose),shell=True)


if __name__ == '__main__':
	run_test()
