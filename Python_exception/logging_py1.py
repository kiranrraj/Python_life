import logging

logging.basicConfig(filename='basic_log.log', level=logging.DEBUG, 
            format=' Process: %(process)d -- Time: %(asctime)s -- Level name: %(levelname)s -- Message: %(message)s')

logging.debug("This message is of the debug level")
logging.info("This message is of the info level")
logging.warning("This message is of the warning level")
logging.critical("This message is of the critical level")
logging.error("This message is of the error level")
