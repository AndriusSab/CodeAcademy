#Create at least 5 different functions and try to handle at least 5 built-in Python Exceptions.


from typing import List, Union

def sum_of_two_numbers(number_one: Union[int, float], number_two: Union[int, float]) -> Union[int, float]:
    
    return number_one + number_two
try:
   new_sum = sum_of_two_numbers(number_one = 5.5, number_two = 8)
except TypeError:
    print("Error Input must be a list of numbers")
except ValueError:
    print("Error List contains non numeric elements")
else:
    print(f"sum of list equal: {new_sum}")




