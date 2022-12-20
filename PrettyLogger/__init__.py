# Sources:
# 1. https://stackoverflow.com/a/17037016
# 2. https://stackoverflow.com/a/56944256


import abc
import logging


class PrettyLogger(abc.ABC, logging.Logger):
    def __init__(self):
        super().__init__(name="logger")
        logging.basicConfig(level=0)

    def getLogger(self, name, filename="log.txt", level=0):
        logger = logging.getLogger(name)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.setLevel(level=level)
        handler = self.getHandler(filename)
        handler.setFormatter(self.getFormatter())
        logger.addHandler(handler)
        logger.propagate = False
        return logger

    def getHandler(self, filename=None) -> logging.Handler:
        pass

    def getFormatter(self):
        pass


class PrettyFileLogger(PrettyLogger):
    def getHandler(self, filename: str) -> logging.Handler:
        return logging.FileHandler(filename=filename)

    def getFormatter(self):
        format = "%(asctime)s : %(levelname)s : %(message)s"
        return logging.Formatter(format)


class PrettyStreamLogger(PrettyLogger):
    def getHandler(self, filename: None) -> logging.Handler:
        return logging.StreamHandler()

    def getFormatter(self):
        format = f"%(levelname)s\t%(message)s"
        return CustomFormatter(format)


class CustomFormatter(logging.Formatter):
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDCOLOR = '\033[0m'

    color = {
        logging.DEBUG: GREEN,
        logging.INFO: BLUE,
        logging.WARNING: YELLOW,
        logging.ERROR: RED,
    }

    def format(self, record):
        formatter = logging.Formatter(
            f"{self.color.get(record.levelno)}%(levelname)s{self.ENDCOLOR}\n\t%(message)s\n"
        )
        return formatter.format(record)
