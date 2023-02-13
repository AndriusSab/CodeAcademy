# squares = []
# for number in range(10):
#     squares.append(number * i)
# print(squares)



# squares = [number * number for number in range(10)]
# print(squares)


# names = []

# name_list =["Andrius", "Tadas", "Mat", "Gied", "Dalius"]

# for name in name_list:
#     if len(name)>=5:
#        names.append(name) 
    
    
# print(f"name lst_one: , {names}")

# susikurti dic kuriame yra 5 key value pair, key stringas, valu = integeris,.double digits
# use dic coprehension to create a new dictionary were key are aas your currnet just all calpiital letters, and value are  reversed 25 =52

# names= {
#     "petras" : 21,
#     "antanas" : 32,
#     "marius" : 56,
#     "jonas" : 67,
#     "kazys" : 37
# }

# my_dict = {name.upper(): int(str(number)[::-1]) for (name, number) in names.items()}

# print(my_dict)

# my_new_dict = {}

# for name, number in names.items:
#      my_new_dict[name.upper()] = int(str(number)[::-1])
# print(my_new_dict)


names = ["andrius", "petras", "kazys", "antanas"]
enumer = enumerate(names, start=2)
new_dict = dict((name,index) for name, index in enumer)
print(new_dict)



# new_idct =dict()

#  l1=['aa','bb','cc','dd']
#  enum=enumerate(l1)

# d=dict((i,j) for i,j in enum)

# {0: 'aa', 1: 'bb', 2: 'cc', 3: 'dd'}




# for key in dict_1:  
    
# for item in dict_1:
#     item[::-1]
#     dict_1.append(dict_2)
# print(dict_2)

    

