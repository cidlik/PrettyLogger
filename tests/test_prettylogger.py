import pathlib
import sys


sys.path.append("../PrettyLogger")
import PrettyLogger

FILENAME = "tmp.log"

# TODO: Добавить fixture "file", которая создает и удаляет файл

def test_filelogger():
    pl1 = PrettyLogger.PrettyFileLogger()
    logger1 = pl1.getLogger(filename=FILENAME)
    logger1.debug("logger1.debug()")
    with open(FILENAME) as f:
        log = f.read()


def test_streamlogger():
    pl2 = PrettyLogger.PrettyStreamLogger()
    logger2 = pl2.getLogger()
    logger2.debug("logger2.debug()")
    logger2.warning("logger2.debug()")
