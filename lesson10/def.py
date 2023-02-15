# a =2
# b = 5

# def addition(number1, number2):
#     sum = number1 + number2
#     return sum
# c = addition(a,b)
# print (c)

# c= addition(10,15)
# print(c)

# def find_sum(num1, num2):
#     return num1+num2 # galima ir taip aprasyti funkcija, praleidziant sum veiksma




# import random

# def get_random_number():
#     print(random.randint(0, 10))
# print(get_random_number())  # printina none 

# def find_sum(num1, num2):
#     '''Returns the sum of num1 and num2.'''
#     sum_nums = num1 + num2  # Finds the sum of num1 and num2
#     return sum_nums  # Returns the sum of the numbers


# def even_odd(num):

#     '''
#     Returns "even" if num is even, and "odd" if num is odd.    
#     Parameters:
#         num (int): Any integer    Returns:
#         type (string): "even" if num is even; "odd" if num is odd
#     '''

#     if num % 2 == 0:  # Checks if num/2 has a remainder of 0
#         return "even"  # If it has a remainder of 0, return "even"
#     else:
#         return "odd"  # If it doesn't, return "odd"
    
#  def check_if_exist(a=None):
#          if a:
#             return a


# def find_sum(num1, num2=50): # default reiksmes dedamos i gala saraso
#     '''Returns the sum of num1 and num2.'''
#     sum_nums = num1 + num2  # Finds the sum of num1 and num2
#     return sum_nums  # Returns the sum of the numbers

# print(find_sum(5))

# def add_two_int_numbers(a:int, b:int)->int: # apsirasome funkcija, kad ivedami integeriai ir iseitis int
#     return a + b

# number1 = add_two_int_numbers(50, 50)
# # number1 = add_two_int_numbers("stringas", 50)
# print(number1)


# type_annotation_int: int = 43
# type_annotation_float: float = 2.54
# type_annotation_string: str = 'efe'
# type_annotation_bool: bool = True.

# from typing import List, Tuple, Union
# Dicttype_annotation_tuple: Tuple[str] = ('1','2','3')
# type_annotation_list: List[str] = ['a', 'b', 'c']
# type_annotation_dict: Dict[str, int] = {'a': 1, 'b': 2}

# import random

# def get_random_object() ->Union[int, str. List[str]]: # union pazymi kad gali buti keletas skirtingu tipu
#     number = random.randint(0, 3)
#     if number ==0:
#         return 0
#     elif number == 1:
#         return "str"
#     else:
#         return ["1", "2", "3"]

from typing import Tuple, Optional, Union

def the_func(x: Union[int, float], y: Tuple[str], z: Optional[float] = None) -> str:
   return 'You called the_func with ' + str(x) + str(y) + str(z)

print(the_func(2, ("1", "2")))

