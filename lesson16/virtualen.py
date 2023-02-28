# import numpy as np
# import panda as pd
from random_word import RandomWords

words =[]

r = RandomWords()
for word in range (5):
    word = r.get_random_word().upper()
    words.append(word)
words.sort()
print(words)        
  
 