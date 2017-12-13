import subprocess
import sys

test = subprocess.check_output(["ls -l"],shell=True)
print test