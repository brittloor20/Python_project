import time 
import logging 

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        eLapsed = end - start
        logging.info(f"{func.__name__} ejecutada en {eLapsed:.4f} seconds")
        return result
    return wrapper


def logit(func):
    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__} ejecutada")
        result = func(*args, **kwargs)
        logging.info("fCompletado {func.__name__}")
        return result 
    return wrapper