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
