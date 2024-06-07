import logging
import decimal


logs = []


class InMemoryHandler(logging.Handler):
    def __init__(self )-> None:
        logging.Handler.__init__(self=self)

    def emit(self, record) -> None:
        logs.append(self.formatter.format(record))


def setup():
    decimal.getcontext().prec = 100
    decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s:%(levelname)s] - %(message)s",
        handlers=[InMemoryHandler(), logging.StreamHandler()
    ])
