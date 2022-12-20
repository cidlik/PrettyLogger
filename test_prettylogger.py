import PrettyLogger

pl = PrettyLogger.PrettyLogger()
pl.setLevel(0)

pl.debug("test debug")
pl.info("test info")
pl.warning("test warning")
pl.error("test error")