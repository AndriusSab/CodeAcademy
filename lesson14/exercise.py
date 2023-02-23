# Write a function that moves all elements of one type to the end of the list:

import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
from typing import List

def move_number_to_end(rand_list: List[int], number:int) -> List[int]:
    logging.info("Entering list of numbers and number to add to the end of new list")
    for item in rand_list:
        if item == number:
            rand_list.remove(item)
            logging.info("Removing number from list if equal to given number")
            rand_list.append(item)
            logging.info("Adding removed number to the end of new list")
    return rand_list

if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 1, 2, 7, 1]

    sorted_list = move_number_to_end(my_list, 2)

    print(sorted_list)