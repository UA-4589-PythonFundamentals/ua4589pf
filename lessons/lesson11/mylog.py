import logging

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='app.log',
                    filemode='w'
                    )
# logger = logging.getLogger(__name__)


logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error("Attempted to divide by zero", exc_info=True)
        return None
    else:
        logging.info("Division successful")
        return result
    
if __name__ == "__main__":
    divide(10, 2)
    divide(10, 0)