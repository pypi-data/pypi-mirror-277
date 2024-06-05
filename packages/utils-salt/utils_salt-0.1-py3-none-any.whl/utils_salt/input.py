from .output import Output
from .ansi import ANSI

class Input:
    @classmethod
    def int(cls, prompt):
        while (1):
            try:
                val = int(input(prompt))
                break
            except ValueError:
                Output.print("*Invalid Input*: Input must be an int\n\n", ANSI.RED, 1, 1)
                
        return val
    
    @classmethod
    def float(cls, prompt):
        while (1):
            try:
                val = float(input(prompt))
                break
            except ValueError:
                Output.print("Invalid Input: Input must be a float\n\n", ANSI.RED, 1, 1)
                
        return val