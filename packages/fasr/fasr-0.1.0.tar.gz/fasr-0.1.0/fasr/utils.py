import time
from typing import Callable
from loguru import logger


def timer(tag: str):
    def outter(func: Callable):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            res = func(*args, **kwargs)
            end = time.perf_counter()
            logger.info(f"{tag} run in {(end - start):.2f} seconds")
            return res

        return wrapper

    return outter
