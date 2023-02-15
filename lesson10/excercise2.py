# Create at least 5 different functions by your own and test it.

# def sum_two_integers(a:int, b:int)-> int:
#     """sums two integers"""
#     return a + b

# def  check_lenght_two_strings (string1:str, string2:str)->str:
#      """checks for leght of two strings"""
#      if len(string1) > len(string2):
#         print (f"Lenght of {string1} is higher than {string2}")
#      elif len(string1) < len(string2):   
#         print (f"Lenght of {string1} is less than {string2}")
#      else:
#         print(f"{string1} is equal {string2}")

# print(check_lenght_two_strings("labas", "karas"))

# def check_for_input_value(input:int)->int:
#     while input!=int:   
#         return print("Please eneter integer")
# print(check_for_input_value("bv"))




# Create a function that adds a string ending to each member in a list

# def add_ending_string(list: list)-> list:
#     for name in list:
#          return list.append("endin")



# list = ["andrius", "tadas", "marius"]

# print(add_ending_string([list]))

# from typing import Listuser_string = input("Enter your string: ")
# str_list = ["1", "2", "3", "4", "5", "6", "7"]
# def add_str(my_list: List[str], my_string: str) -> List[str]:
#     str_added = []
#     for item in my_list:
#         str_added.append(item + my_string)
#     return str_addeda = add_str(str_list, user_string)
# print(a)


number1 = int(input("Please enter number: "))
number2 = int(input("Please enter number: "))


def easy_calculator(a:int, b:int)->int:
    sum = a + b
    subtraction = a - b
    division = a / b 
    multiplication = a * b
    return sum, subtraction, division, multiplication  
print(sum(number1, number2))

# Create a function that returns only strings with unique characters.



from typing import List


name_list = ["a","a" "b", "b", "c" "c", "g","g"] 

def find_character (my_list:List[str])->List[str]:
    unique_character_list = []    

    for item in my_list:
        if item not in unique_character_list:
            unique_character_list.append(item)     
        return unique_character_list

filtered_list = find_character(name_list)
print (filtered_list)


