import logging

#Create a Format 
adminFormat = logging.Formatter(' Process: %(process)d -- %(asctime)s -- %(levelname)s -- %(message)s')

#create a logger named admin
cust_logger = logging.getLogger("admin")

#create a handler
adminHandler = logging.FileHandler('handlerLog.log')
#set a debugging level
adminHandler.setLevel(logging.DEBUG)
#set a format leve;
adminHandler.setFormatter(adminFormat)

# add handler to logger 
cust_logger.addHandler(adminHandler)

outHandler = logging.StreamHandler()
outHandler.setFormatter(adminFormat)
outHandler.setLevel(logging.INFO)
cust_logger.addHandler(outHandler)

cust_logger.debug("This message is of the debug level")
cust_logger.info("This message is of the info level")
cust_logger.warning("This message is of the warning level")
cust_logger.critical("This message is of the critical level")
cust_logger.error("This message is of the error level")

print(cust_logger.level)
print(logging.root.level)