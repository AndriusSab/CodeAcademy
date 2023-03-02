# reate a Book class that has two attributes:

# title
# author
# and two methods:

# A method named .get_title() that returns: "Title: " + the instance title.
# A method named .get_author() that returns: "Author: " + the instance author.
# and instantiate this class by creating 3 new books:

# Pride and Prejudice - Jane Austen (PP)
# Hamlet - William Shakespeare (H)
# War and Peace - Leo Tolstoy (WP)
# The name of the new instances should be PP, H, and WP, respectively. For instance, if I instantiated the following book using this Book class:

# Harry Potter - J.K. Rowling (HP)
# I would get the following attributes and methods:

# HP.title ➞ "Harry Potter"
# HP.author ➞ "J.K. Rowling"
# HP.get_title() ➞ "Title: Harry Potter"
# HP.get_author() ➞ "Author: J.K. Rowling"


class Book:
     def __init__(self, title:str, author: str):
        self.title: str = title
        self.author: str = author

     def fullname(self):
         Fullname = self.name + " " + self.surname
         return  f"Your fullname is: {Fullname}"
     