from logging import getLogger
from logging.handlers import RotatingFileHandler

from currency import get_currencies
from decorators import logger

log = getLogger("fileLogger")
handler = RotatingFileHandler("./logs.txt")
log.addHandler(handler)
log.setLevel(1)
get_currencies = logger(get_currencies, handle=log)
print(get_currencies(["USD", "EUR"]))
get_currencies(["PUPU"])
handler.close()