import logging

# %(asctime)s -- %(levelname)s -- %(message)s

logging.basicConfig(filename="log.txt" ,level=logging.DEBUG,
                        format= '%(asctime)s -- %(levelname)s -- %(message)s')

print('---------------------------------------')                        
logging.debug('----------Start of program---------------')

def factorial(n):
    logging.debug(f'Start of factorial {n}')
    total = 1
    for i in range(1,n+1):
        total *=i
        logging.debug(f'Value of i is {i} and total is {total}')
    logging.debug(f'End of factorial {n}')
    return total

print(f" The final output is : {factorial(6)}")
logging.debug('------------End of program--------------')
print('---------------------------------------')   