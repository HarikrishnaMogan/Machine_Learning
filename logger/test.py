from logger import logger1

def add(a,b):
    logger1.debug("This is inside add")
    return a+b

logger1.debug("This is test")
add(10,5)