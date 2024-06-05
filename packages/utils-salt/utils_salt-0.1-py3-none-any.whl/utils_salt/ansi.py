class ANSI:
    @classmethod
    @property
    def RED(cls):
        return '\033[31m'

    @classmethod
    @property
    def GREEN(cls):
        return '\033[32m'

    @classmethod
    @property
    def YELLOW(cls):
        return '\033[33m'

    @classmethod
    @property
    def BLUE(cls):
        return '\033[34m'

    @classmethod
    @property
    def MAGENTA(cls):
        return '\033[35m'

    @classmethod
    @property
    def CYAN(cls):
        return '\033[36m'

    @classmethod
    @property
    def WHITE(cls):
        return '\033[37m'
    
    @classmethod
    @property
    def BOLD(cls):
        return '\033[1m'

    @classmethod
    @property
    def ITALIC(cls):
        return '\033[3m'
    
    @classmethod
    @property
    def RESET(cls):
        return '\033[0m'