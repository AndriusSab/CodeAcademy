
from typing import List

list1 = [5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]

def war_odd_evenen(new_list:int)->List:
   even_sum = 0
   odd_sum = 0
   for number in new_list:
        if number % 2 == 0:
           even_sum += number    
        else:
            odd_sum += number

   return even_sum - odd_sum

print(war_odd_evenen(list1)) 