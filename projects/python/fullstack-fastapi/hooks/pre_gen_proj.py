
import re
import sys
import os
import shutil

class bcolors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_CR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# -*- coding: utf-8 -*- 
cur_dir = os.getcwd()
print ("The current working directory is %s" % cur_dir)

