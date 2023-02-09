"""
    Lexer of the ChungaPunga programing languange
    by: Rishit V
"""
import keywords

def check_for_errors(programs):
    # to be programmed later...
    pass

class Lang: # the language file will be passed into this class upon bieng parsed...
    def __init__(self, fileloc):
        program = open(fileloc, 'r')
        self.program = program.readlines() # list of lines in the program.
        self.global_vars = []
        self.const_vars = []
        check_for_errors(self.program)
    
    def run():
        # this is where program is executed...
        pass
