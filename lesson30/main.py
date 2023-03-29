# Lambdas section:

# Write a Python program to find if a given string starts with a given character using Lambda. Sample Output: True False
# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
# Write a Python program to add two given lists using map and lambda.
# Write a Python program to square and cube every number in a given list of integers using Lambda
# Write a Python program to extract year, month, date and time using Lambda. Sample Output: 2020-01-15 09:03:32.744178 2020 1 15 09:03:32.744178


# first_letter_check = lambda x: x.startswith("A")
# print(first_letter_check("Andrius"))
# print(first_letter_check("Saulius"))

# add_numer = lambda x: (x + 15)
# multiply_numbs = lambda x, y: (x * y)

# print(add_numer(10))
# print(multiply_numbs(5, 10))


list1 = [1, 2, 3]
list2 = [2, 2, 2]

result = map(lambda x, y: x + y, list1, list2)

print(list(result))

# list_nums = [1, 2, 3, 4]
# square_cube_list = map(lambda x: [x**2, x**3], (list_nums))
# print(list(square_cube_list))


import datetime

currentDateTime = datetime.datetime.now()
print(currentDateTime)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
minutes = lambda x: x.minute
second = lambda x: x.second
print("Year - ", year(currentDateTime))
print("Month - ", month(currentDateTime))
print("Day - ", day(currentDateTime))
print("Minutes - ", minutes(currentDateTime))
print("Seconds - ", second(currentDateTime))

# Listas = [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]

# sorted_list = sorted(Listas, key=lambda x: x[1], reverse=False)

# print(sorted_list)

# # Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
# # Write a Python program to sort a list of dictionaries using Lambda.
# original_list = [
#     {"make": "Nokia", "model": 216, "color": "Black"},
#     {"make": "Mi Max", "model": "2", "color": "Gold"},
#     {"make": "Samsung", "model": 7, "color": "Blue"},
# ]


# sorted_dictionaries = sorted(original_list, key=lambda x: x["color"])

# print(list(sorted_dictionaries))
