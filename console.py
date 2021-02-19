class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class console:
    @staticmethod
    def log(msg=""):
        print(msg,end="")
    @staticmethod
    def error(msg=""):
        print(bcolors.WARNING+msg,end="")
    @staticmethod
    def success(msg=""):
        print(bcolors.OKGREEN+msg,end="")


# console.log("Hello, World!")
