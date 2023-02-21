
from typing import List

def war_odd_evenen(new_list:int)->List:
   even_sum = 0
   odd_sum = 0
   for number in new_list:
        if number % 2 == 0:
           even_sum += number    
        else:
            odd_sum += number

   return even_sum - odd_sum

if __name__ == "__main__":

     list1 = [1, 3, 4, 5, 6]

result = war_odd_evenen(list1)
print(result)