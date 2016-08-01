"""
This file could contain the necessary calls to make plots etc for
case 1

"""
import os
import sys

# Get the testcase from filename when the script called and call a generic
# script
os.system('python ./caseX.py ' + filter(str.isdigit, sys.argv[0]))
