Write python program that asks user to enter name, surname, age. Put these values into a dictionary and print dictionary
name = input('Enter your name: ')
surname = input('Enter your surname: ')
age = input('Enter your age: ')

dictionary = {"name":name, "surname":surname, "age":age}

print(dictionary)

print(dictionary["name"])

#using zip funcion to join key and values

# converting two lists into a dictionary
# Note that lists must be of the same size here:

# test_keys = ["Albert", "Tom", "Stephen"]
# test_values = [1, 4, 5]
# my_dictionary= dict(zip(test_keys, test_values))
# print(my_dictionary)

name = input("Pease input you name: ")
surname = input("Please input you surname: ")
age = int(input("Please input you age: "))

my_dict_keys = ['name', 'surname', 'age']
my_dict_values = [name, surname, age]

my_dict = dict(zip(my_dict_keys, my_dict_values))
print(my_dict)

# dictionary = {'a': 1, 'b': 2, 'c':3}

# for key,value in dictionary.items():
# 	print(key, ':', value)

   
   #print all keys
# dictionary = {'a': 1, 'b': 2, 'c':3}

# for key in dictionary.keys():
# 	print(key)


# print all values

# dictionary = {'a': 1, 'b': 2, 'c':3}

# for value in dictionary.values():
# 	print(value)

# d1 = {'a': 10, 'b': 20, 'c': 30}
# d1.update([('b', 200), ('d', 400)])
# print(d1)


d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update(b=200, d=400)
print(d1)

#loopinimas dictionary

d = {'a': 10, 'b': 20, 'c': 30}
for key, value in d.items():
    print(key, value)

#removing from dictionary
d = {'a': 10, 'b': 20, 'c': 30}
d.pop('a')
print(d)