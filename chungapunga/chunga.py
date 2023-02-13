"""
    Command Line Interface for the Chunga Punga programing language
    by: Rishit V
"""
import sys
from interpreter import *

arguments = sys.argv # python(3) chunga.py location/filename.chung
prog = Lang(arguments[2])
prog.run()
