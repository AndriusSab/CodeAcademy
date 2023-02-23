# Create a simple program that would log all inputs from the terminal. 
# Configs must show all additional data (time, date, level etc.)
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# input_one = print(int(input("Please enter number lover than 6: ")))  
# input_two = print(int(input("Please enter number 2: "))) 
# input_three = print(int(input("Please enter number higher than 0: ")))


def input_info_log(first_input: int, second_input: int, third_input: int) -> int:
     logging.info(f"The first imput is:  {first_input}, second: {second_input}, third: {third_input}")

if first_input < 6: 
     logging.warning("as input expected number lover than 6")

elif input_two == 2:
     logging.warning("s input expected number not equal 2")

elif input_three < 0:
     logging.warning("s input expected positive")

    return input_one, input_one

if __name__ == "__main__":
    input_one = int(input("Please enter any number"))            
    input_two = int(input("Please enter any word")) 
    input_three = int(input("Please enter any word"))

    my_input = im

