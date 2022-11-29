import logging


class PrettyLogger(logging.Logger):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self, log_level=0):
        FORMAT = "%(message)s"
        logging.basicConfig(level=log_level, format=FORMAT)
        self.logger = logging.getLogger()

    def debug(self, foo: str):
        tmp = self.logger.debug(f"{self.OKGREEN}[DEBUG]:{self.ENDC} {foo}")

    def warning(self, foo: str):
        self.logger.warning(f"{self.WARNING}[WARNING]:{self.ENDC} {foo}")

    def error(self, foo: str):
        self.logger.error(f"{self.FAIL}[ERROR]:{self.ENDC} {foo}", stack_info=True)
