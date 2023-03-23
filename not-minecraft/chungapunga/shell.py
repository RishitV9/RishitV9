"""
    Shell for the ChungaPunga programming language...
    by: Rishit V
"""
from interpreter import *

print("Welcome to the Chunga Punga Programming language shell...")
print("press ctrl+c to exit...")

try:
    while True:
        string = input("> ")
        f = open("a.chung", "w")
        f.write(string)
        f.close()
        
        prog = Lang("a.chung")
        prog.run()
        print(f"exit code: {prog.exit_code}")
        
except KeyboardInterrupt:
    exit(-1)
