import sys
import platform
import os
args = sys.argv

import lin
import win

settings = open("defaults.txt")
if 

if platform.system() == "Linux":
    lin.start(args.pop(0))
else:
    win.start(args.pop(0))
