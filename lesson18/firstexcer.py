# 4 basic principles are called the four pillars of object-oriented programming (OOP). 
# These four pillars are: 
# Inheritance, Polymorphism, Encapsulation and Abstraction.

# class Names:
#     """This is a class about forgotten friend Antanas"""
#     def __init__(self, name:str, surname:str, age:int) -> None:
#         self.name = name 
#         self._surname = surname #
#         self.__age = age     
#     def print_out_name(self)->None:
#         print(self.name)
    
    # def change_name(self) -> None:
    #     self.name = name

# my_name = Names(name = "Antanas", surname="Betkas", age=18)

# print(my_name.name)
# print(my_name._surname)
# print(my_name.__age)


# class Car:
#     def __init__(self, make_year:int, cost:float, color:str)-> None:
#         self.make_year = make_year
#         self.cost = cost
#         self.color = color
#         self.full_info = f'Full info: {make_year} year  , {cost} eur, {color}..'
#         self.something = None
    
#     def get_car_color(self)-> None:
#         print(f"My car color: {self.color}")

#     def get_cost(self):
#         return self.cost
    
#     def get_full_info(self)->None:
#         print(f"My full info : {self.full_info}")

class Car:
  
    def get_car_color(self, color)-> None:
        print(f"My car color: {color}")

    def get_cost(self, cost):
        return cost
    
    def get_full_info(self)->None:
        print(f"My full info : {full_info}")

class Ferrari(Car):
     SPEED_CONSTANT = 20.5
     def __init__(self, hp:int)->None:
            self.hp = hp

     def get_max_speed(self)->float:
        return self.hp * self.SPEED_CONSTANT
        
my_uber_car = Ferrari(hp = 450)
print(f"My max speed: {my_uber_car.get_max_speed()} ")



            