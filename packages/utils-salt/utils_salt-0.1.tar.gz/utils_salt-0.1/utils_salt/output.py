from .ansi import ANSI

class Output:
    @classmethod
    def print(cls, str, color, bold = False, italic = False):
        bold = ANSI.BOLD if bold else ''
        italic = ANSI.ITALIC if italic else ''
        
        print(color, bold, italic, str, ANSI.RESET, sep="", end="")