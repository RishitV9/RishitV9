"""
    Interpreter of the ChungaPunga programing languange
    by: Rishit V
"""
from keywords import *
from errors import *

def check_for_errors(programs):
    # to be programmed later...
    pass

class Lang: # the language file will be passed into this class upon bieng parsed...
    def __init__(self, fileloc):
        program = open(fileloc, 'r')
        self.program = program.readlines() # list of lines in the program.
        self.global_vars = {}
        self.const_vars = {}
        self.exit_code = 0
        self.__line = 0
        check_for_errors(self.program)
    
    def run(self):
        # this is where program is executed...
        program = self.program
        while True:
            line = self.program[self.__line]
            # for every line...
            # detect keyword, and execute:
            linew = line.split()
            if print_key in line: # print function...
                linew.remove("print")
                new_string = ""
                for i in linew:
                    if "$" in i:
                        pass # this is var, progress will be done later...
                    else:
                        new_string += i + " "
                print(new_string)

            elif halt_key in line: # halt function...
                linew = line.split()
                if len(linew) != 2:
                    self.exit_code = syntaxerror("ERROR -> halt takes 1 argument, exit code")
                    exit(self.exit_code)
                try:
                    exit_code = int(linew[1])
                except:
                    self.exit_code = syntaxerror("ERROR -> halt takes int argument")
                    exit(self.exit_code)
                
                exit(self.exit_code)
            
            elif set_key in line:
                linew = line.split()
                

            else: # could not recognise command...
                self.exit_code = syntaxerror("ERROR -> Could not Understand Your Command")
                exit(self.exit_code)

            self.__line += 1