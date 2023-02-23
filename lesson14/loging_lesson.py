import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
#creates datalog faila



# logging.debug('This is a 
# debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# def add_number(a: int, b: int) -> int:
#     logging.debug(f"Received numbers: {a} and b:{b}")
#     return a + b
# add_number(a =6, b = 7)

def money_collected(amount: float ) -> None:
    logging.info(f"Amount of money received {amount}")   #apsirasom programa
    if amount == 0:
        logging.warning("Expected amount larger than 0")
    

    #doing smt else 
# try:
#     #some code here
# except: Exception as e:
#     logging.error(f"Error received: {e}")

def emergency_stop(is_stop_event: bool) -> None:
    if is_stop_event:
        logging.critical(f"Had to stop device due to unexpected stop event")

emergency_stop(True)
