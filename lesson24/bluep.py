# from abc import ABC, abstractclassmethod


# class Vehicle(ABC):

#     @abstractclassmethod
#     def get_name(self) -> None:
#         pass

#      @abstractclassmethod
#     def get_vehicle_cost(self) -> None:
#         pass


# class Car(Vehicle):
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age

#     def get_age(self) -> None:
#         print(self.age)


# my_car = Car(name="Audi - A6", age=2018)
# my_car.get_age()
# print(my_car.get_vehicle_cost())

# from abc import ABC, abstractclassmethod


# class Animal(ABC):
#     def __init__(self, name: str) -> None:
#         self.name = name

#     @abstractclassmethod
#     def speak(self) -> str:
#         pass

#     def get_name(self) -> str:
#         return self.name


# class Dog(Animal):
#     def __init__(self, name: str) -> str:
#         self.name = name
#         super().__init__(name=name)

#     def speak(self) -> str:
#         return "Dog says woof"


# class Cat(Animal):
#     def __init__(self, name: str) -> str:
#         self.name = name
#         super().__init__(name=name)

#     def speak(self) -> str:
#         return "Cat says meow"


# cat = Cat("Murka")
# dog = Dog("Amsis")
# print(cat.speak())
# print(dog.speak())


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError

    def get_name(self) -> str:
        return self.name


class Dog(Animal):
    def __init__(self, name: str) -> str:
        self.name = name
        super().__init__(name=name)

    def speak(self) -> str:
        return "Dog says woof"


class Cat(Animal):
    def __init__(self, name: str) -> str:
        self.name = name
        super().__init__(name=name)

    def speak(self) -> str:
        return "Cat says meow"


cat = Cat("Murka")
dog = Dog("Amsis")
print(cat.speak())
print(dog.speak())
