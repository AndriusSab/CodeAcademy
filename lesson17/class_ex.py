from datetime import date

class Person:
    description: str = "A simple normal human being"

    def __init__(self, name:str, surname: str):
        self.name: str = name
        self.surname: str = surname

  
    def greet(self):
        return f"Hello my name is {self.name}"
    def walk_away(self):
        return f"{self.name} is walking away..."
    def days_until_bl_friday(self):
        today = date.today()
        black_friday_date = date(2023, 11, 24)
        delta = black_friday_date - today
        return delta.days 
    
    def get_eye_color(Self, eye_color: str = "Brown") ->str:
        return eye_color

person = Person("Andrius", "Sabaliauskas")
print(person.get_eye_color())
print(person.days_until_bl_friday())

    
    
    # print(type(today))
    
person = Person("Andrius", "Sabaliauskas")
person2 = Person("Antanas", "Fontanas")

# # print(person.greet())
# # print(person2.walk_away())
# print(Person.description)

