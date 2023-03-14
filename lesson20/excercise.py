# Create a Person class which will have three properties:
#     Name
#     List of foods they like
#     List of foods they hate
# In this class, create the method taste():
#     It will take in a food name as a string.
#     Return {person_name} eats the {food_name}.
#     If the food is in the person's like list, add 'and loves it!' to the end.
#     If it is in the person's hate list, add 'and hates it!' to the end.
#     If it is in neither list, simply add an exclamation mark to the end.
#     p1 = Person("Sam", ["ice cream"], ["carrots"])
#     p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
#     p1.taste("cheese") ➞ "Sam eats the cheese!"
#     p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"





class Person:
    
    def __init__(self, name:str, liked_food:list[str], hated_food:list[str]) -> None:
        self.name = name
        self.liked_food = liked_food
        self.hated_food = hated_food
    
    
    def taste(self, food)-> None:
        
        if food in self.liked_food:
            print(f"{self.name} loves the {food}!")
        elif food in self.hated_food:
            print(f"{self.name} hates the {food}!")
        else: 
            print(f"{self.name} eats the {food}!")

   
liked_food = ["apple", "beer", "burger"]
hated_food = ["fish", "carrots", "soda"]

p1 = Person("Sam", ["ice cream"], ["carrots"])

p1.taste("ice cream") 
p1.taste("cheese")
p1.taste("carrots")