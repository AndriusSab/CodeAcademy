
Profile picture of Python (PTUA3) studijos.
General
Meet 
General

Join
Susitikimas vyksta kanale Bendrasis started
5 replies from Raimundas, Laimonas, Jakov, and Giedrius . Press Enter to expand replies.
5 replies from Raimundas, Laimonas, Jakov, and Giedrius
Reply
Tuesday, February 7, 2023
Profile picture of Artūras Ardzijauskas.
Artūras Ardzijauskas
2/7 7:46 PM

Task_02
Text
user_name = str(input("Please enter your name: "))
database_list = ['Tom', 'Den', 'Trump']

if user_name in database_list:
    print(f"{​user_name}​ greeting!!!")
else:
    print("Welcome otherwise")
Reply
Wednesday, February 8, 2023
Profile picture of Viktorija Žilinskaitė.
Viktorija Žilinskaitė
2/8 3:43 PM

Studijų kokybės apklausa
Sveiki! 👋
 Jau antroji studijų savaitė, tad labai norime sužinoti kokiais įspūdžiais gyvenate ir mokotės! 
 
Prašau užpildykite pirmąją studijų kokybės apklausą, pasisakykite kokių turite pastebėjimų, neramumų, pagyrimų ar klausimų 🙂
 Labai prašau visus sudalyvauti, tai truks tik kelias minutėles. Apklausą užpildykite iki vasario 10 d. 12 val.
 
---> Apklausą rasite paspaudę čia <---
 
Dėkoju 🙏
 General
Reply
Meeting ended: 17s
Profile picture of Remigijus Šamonskis.
Reply
Monday, February 13, 2023
Profile picture of Viktorija Žilinskaitė.
Viktorija Žilinskaitė
2/13 10:17 AM

Vasario 16 d. paskaita nevyks
Sveiki 👋
​ Noriu priminti, jog vasario 16-ąją yra nedarbo diena, tad tądien paskaita nevyks. General​​​​​​​
Profile picture of Tomas Svalbonas.
Tomas Svalbonas
2/13 11:08 AM

Sveiki, ačiū už informaciją 🙂
Reply
Today
General
01:59:00
Profile picture of Andrius Sabaliauskas.
Profile picture of Artūras Čekanauskas.
Profile picture of Vytautas Matevičius.
Profile picture of Laimonas Paura.
+15

Join
Profile picture of Viktorija Žilinskaitė.
Viktorija Žilinskaitė
1/27 12:59 PM

Scheduled a meeting
Python (PTUA3) paskaitos
Occurs every Mon, Tue, Wed and Thu @6:00 PM until 8/31/2023
397 replies from Viktorija, Tomas, Giedrius, and 20 others . Press Enter to expand replies.
397 replies from Viktorija, Tomas, Giedrius, and 20 others
Profile picture of Mindaugas Rudzevičius.
Mindaugas Rudzevičius
7:50 PM

OOP
Python
class Names:
    """This is a class about our forgotten friend Antanas"""
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name
        self._surnname = surname
        self.__age = age
    def print_out_the_name(self) -> None:
        print(self.name)
    def change_name(self, name: str) -> None:
        print(self.__age)
        self.name = name
# my_name = Names(name='Antanas', surname='Mindukas', age= 22)
# my_name.change_name(name='Minde')
# print(my_name.name)
# print(my_name._surnname)
# print(my_name.__age)
# my_name.name = 'Minde'
# print(my_name.name)
# class Car:
#     def __init__(self, make_year: int, cost: float, color: str) -> None:
#         self.make_year = make_year
#         self.cost = cost
#         self.color = color
#         self.full_info = f'Full info: {​cost}​ linero - {​make_year}​ years - {​color}​..'
#         self.smth = None
#     def get_car_color(self) -> None:
#         print(f'My car color: {​self.color}​')
#     def get_cost(self) -> float:
#         return self.cost
#     def get_full_info(self) -> None:
#         print(f'My full info: {​self.full_info}​')
class Car:
    def __init__(self, random_number: int) -> None:
        self._check_this_one: int = random_number
        self.__check_another_one: int = 2
    def get_car_color(self, color: str) -> None:
        print(f'My car color: {​color}​')
    def get_cost(self, cost: float) -> float:
        print(cost)
        return cost
    def get_full_info(self, full_info: str) -> None:
        print(f'My full info: {​full_info}​')
class Plane:
    pass
class Ferrari(Car, Plane):
    SPEED_CONSTANT = 20.5
    def __init__(self, hp: int, number: int) -> None:
        super().__init__(random_number=number)
        self.hp = hp
    def _get_max_speed(self) -> float:
        return self.hp * self.SPEED_CONSTANT
    def get_cost(self, cost: float) -> None:
        print(f'Cool Not COOl: {​cost}​')
    def calculate_consumption(self, distance: int) -> None:
        speed = self._get_max_speed()
        print(speed * distance)
test_car = Car(random_number=32550)
my_uber_car = Ferrari(hp= 450, number=555)
my_uber_car._get_max_speed()
print(test_car._check_this_one)
print(my_uber_car._check_this_one)
# print(my_uber_car.__check_another_one)
# print(my_uber_car.__check_another_one)
class My_Byke(Ferrari):
    pass
Reply

 New conversation

