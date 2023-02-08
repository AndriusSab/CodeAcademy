
# We have 3 dictionaries :  dic_one={1:10, 2:20} dic_two={3:30, 4:40} dic_three={5:50,6:60}
# Create one final dictionary from all those 3.

#lists of dictionaries:

dic_one={1:10, 2:20}
dic_two={3:30, 4:40}
dic_three={5:50,6:60}

#adding dictionaries one by one
dic_one.update(dic_two)
dic_one.update(dic_three)
print(dic_one)



