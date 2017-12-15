import os, sys
import subprocess
from pathlib import Path


def run_test():

	if len(sys.argv) == 1:
		welcomeText()
		return 1
	
	elif len(sys.argv) > 1:
		run_bash_command(checkArguments(initList()))


def run_bash_command(listArguments):

	attribut_file = Path("./attribute.py")

	if listArguments[1] == 1:

		if len(listArguments[2]) != 0:
			print "\n\033[1;32;31mYou can't ask to execute one test if you select the options \033[1;32;33m-a \033[1;32;31m!\033[1;32;m\n"
			return 0

		else:
			listArguments[3] = raw_input("\n\033[1;32;40mWrite your email\033[1;32;m (\033[1;32;33mExample: \033[1;32;m\"somebody@something.com\") : ")
			listArguments[4] = subprocess.check_output("./get_domain.sh %s" %listArguments[3],shell=True)

			if listArguments[4] == "NOK\n":
				print "\n\033[1;32;31mYou right an email with a wrong domain name !\n\033[1;32;m"
				return 0

			else:
				listArguments[2] = ["test_Version.py","test_Register.py","test_Login.py","test_Who_Am_I.py","test_Logout.py","test_Login.py","test_Deactivate.py"]
				
				for test in listArguments[2]:
			
					if attribut_file.exists():
						subprocess.call("python %s %s %s %s " %(test,listArguments[0],listArguments[3],listArguments[4]),shell=True)

					else:
						print "\n\033[1;32;31mThe file \033[1;32;33m\"attribute.py\"\033[1;32;31m is needed for the automate, check if he is in the directory with the others tests !"
                        			return 0
				
				try:
    					os.remove("AccessToken.txt")
				except OSError:
					pass
				return 1

	else:

		if attribut_file.exists():
			subprocess.call("python attribute.py %s %s %s " %(listArguments[0],listArguments[3],listArguments[4]),shell=True)

		else:
			print "\n\033[1;32;31mThe file \033[1;32;33m\"attribute.py\"\033[1;32;31m is needed for the automate, check if he is in the directory with the others tests !"
			return 0

		if len(listArguments[2]) == 0:
			print "\n\033[1;32;31mIf you didn't ask for running all tests, you have to write a test_file !\033[1;32;m\n"
			return 0

		else:
			listArguments[3] = raw_input("\n\033[1;32;40mWrite your email\033[1;32;m (\033[1;32;33mExample: \033[1;32;m\"somebody@something.com\") : ")
			listArguments[4] = subprocess.check_output("./get_domain.sh %s" %listArguments[3],shell=True)
			
			if listArguments[4] == "NOK\n":
				print "\n\033[1;32;31mYou right an email with a wrong domain name !\n\033[1;32;m"
				return 0

			else:
				for test in listArguments[2]:
					subprocess.call("python %s %s %s %s" %(test,listArguments[0],listArguments[3],listArguments[4]),shell=True)
				try:
                                        os.remove("AccessToken.txt")
                                except OSError:
                                        pass
				return 1


def welcomeText():

	print "\n\033[1;32;40mWelcome,to automate-test 1.0 ! "
	print "\033[0;32;mIf you want to execute some \033[1;32;31mtests,\033[0;32;m You can choose between this 2 options:"    
	print "   \033[1;32;33m-v [Name of your test] :\033[0;32;m With that you can see the body response from the server"
	print "   \033[1;32;33m-a :\033[0;32;m With this you can run all tests\nIf you want to run one particular test, just write \"\033[1;32;33mpython automate.py --options [Name of your test]\033[0;32;m\"."
	print "\033[1;32;40mEnjoy !\033[0;32;m  \n"


def initList():
	verbose = 0
	varAll = 0
	test_file = []
	email = ""
	domain = ""
	listInitArgs = []
	listInitArgs.append(verbose)
	listInitArgs.append(varAll)
	listInitArgs.append(test_file)
	listInitArgs.append(email)
	listInitArgs.append(domain)

	return listInitArgs


def checkArguments(listInitArgs):

	for args in sys.argv[1:]:

		if args == "-v":
			listInitArgs[0] = 1

		elif args == "-a":
			listInitArgs[1] = 1

		elif args.endswith(".py"):
			listInitArgs[2].append(args)

		else:
			print "\nThere is a mistakes somewhere : check if you right correctly the options or the name of the \033[1;32;33mtest_file \033[0;32;m! \n"

	return listInitArgs


if __name__ == '__main__':
	run_test()
