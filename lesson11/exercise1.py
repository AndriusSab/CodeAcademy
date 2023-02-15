# Write a function that takes two lists and adds the first element in the first list with the first element 
# in the second list, the second element in the first list with the second element in the second list, 
# etc, etc. Return True if all element combinations add up to the same number. Otherwise, return
# False. Example:

# puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# # 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
# # Both lists sum to [5, 5, 5, 5]
# puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ True
# puzzle_pieces([1, 2], [-1, -1]) ➞ False
# puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False

# list1 = [1, 2, 3, 4]
# list2 = [4, 3, 2, 1]

# def add_list_numbers(my_list1:list[int], my_list2:list[int])-> bool:
#      new_list = []
#      for i in range(0, len(my_list1)):
#          new_list.append(my_list1[i] + my_list2[i])
#          return new_list 
#      for i in new_list:
#         if i == new_list[0]:
#              return True
#         if i != new_list[0]:
#             return False
#      return new_list 
     
# print(add_list_numbers(list1, list2))


# list1 = [1, 2, 3, 4]
# list2 = [4, 3, 2, 1]
# def add_list_numbers(my_list1:list[int], my_list2:list[int])-> bool:
#      new_list = []
#      for x, y in zip(my_list1, my_list2):
#           new_list.append(my_list1+my_list2)
#           if len(set(new_list)) ==1:
#             return True
#           else: 
#             return False
       
#      return new_list

# print(add_list_numbers(list1, list2))


from typing import List
item_list_1 = [1, 8, 5, 0, -1, 7]
item_list_2 = [0, -7, -4, 1, 2, -6]
def add_puzle(item1: List[int], item2: List[int]) -> bool:
    c = []
    for x, y in zip(item1, item2):
        c.append(x + y)
    if len(set(c)) == 1:
        return True    
    else:
        return False
print(add_puzle(item_list_1, item_list_2))


