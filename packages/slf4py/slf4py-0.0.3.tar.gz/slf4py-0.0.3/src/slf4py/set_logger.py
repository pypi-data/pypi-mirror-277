import os
from logging import getLogger, StreamHandler, Formatter, getLevelName
from typing import Literal


def set_logger[T](
    cls: T | None = None,
    format: str = os.getenv("SLF4PY_LOG_FORMAT", "[%(levelname)s] [%(asctime)s] [%(filename)s:%(lineno)d] %(message)s"),
    level: Literal['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'] = os.getenv("SLF4PY_LOG_LEVEL", "DEBUG")
):
    def _set_logger(cls: T):
        def wrapper(*args, **kwargs):
            log = getLogger(cls.__name__)

            level_name = getLevelName(level)
            handler = StreamHandler()
            handler.setLevel(level_name)
            handler.setFormatter(Formatter(format))

            log.setLevel(level_name)
            log.addHandler(handler)
            log.propagate = False

            setattr(cls, "log", log)

            return cls(*args, **kwargs)
        return wrapper

    if cls is None:
        return _set_logger

    return _set_logger(cls)
