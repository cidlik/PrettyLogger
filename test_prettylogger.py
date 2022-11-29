import PrettyLogger

pl = PrettyLogger.PrettyLogger()
pl.setLevel(0)

pl.debug("test debug")
pl.warning("test warning")
pl.error("test error")