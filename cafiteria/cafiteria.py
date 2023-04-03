from ast import List
import datetime


# class Reservation:
#     """Self tables dictionary key stands for table type "single", "double" and "family", and values
#     stands for number of available table"""

#     def __init__(self, fulname:str, time: dateime) ->None:
#         self.fulname = fulname
#         self.time = time

# class Table:
#     def __init__(self, nummber_of_seats:int) -> None:
#                  ) -> None:

#     def check_reservation(self, name):
#         if name in self.reservations:
#             return f"Your table is reserved for table {self.reservations[name]}."
#         else:
#             return f"There is no reservation by {name}"


#     def assign_table(self, name):

#         for table in range(1, 11):
#             if table not in self.reservations.values():
#                 self.reservations[name] = table
#                 return f"You have been assigned table {table} for a party of {self.tables[size]}."
#             break
#         else:
#             print("Sorry, there are no free tables available.")


# def main():
#     reservation = Reservation()
#     name = input("Hello, what is your full name? ").upper()
#     print(f"Hello {name}")
#     print(reservation.check_reservation(name))
#     print(reservation.assign_table(name))
#     if name not in self.reservations:
#         size = input("What size table would you like? (single, double, or family) ")
#     while size not in self.tables:
#         size = input("Invalid size. Please choose single, double, or family. ")


# while size not in reservation.tables:
# size = input("Invalid size. Please choose single, double, or family. ")
# reservation.check_reservation(name)

# if __name__ == "__main__":
#     main()


# class Table:
#     def __init__(self, time: dateime) -> None:
#         pass

#     tables = {
#         "Single": {
#             "Table_one": {"name": "Antanas", "status": "Reserved"},
#             "Table_two": {"name": "None", "status": "Available"},
#             "Table_tree": {"name": "None", "status": "Available"},
#             "Table_four": {"name": "None", "status": "Available"},
#         },
#         "Double": {
#             "Table_one": {"name": "None", "status": "Available"},
#             "Table_two": {"name": "Andrius", "status": "Reserved"},
#             "Table_tree": {"name": "None", "status": "Available"},
#             "Table_four": {"name": "None", "status": "Available"},
#         },
#         "Family": {
#             "Table_one": {"name": "None", "status": "Available"},
#             "Table_two": {"name": "Jonas", "status": "Reserved"},
#             "Table_tree": {"name": "None", "status": "Available"},
#             "Table_four": {"name": "None", "status": "Available"},
#         },
#     }

#     client = input("Welcome to cafeteria. Please say Your name: ")
#     for key, value in tables.items():
#         for key1, value1 in value.items():
#             for key2, value2 in value1.items():
#                 if value2 == client:
#                     print(f"Your {value2} table is reserved")
#                 break
#             else:
#                 print("No table is reserved with this name")


# class Restaurant:
#     def __init__(self) -> None:
#         pass


# class Reservation:
#     def __init__(self, name: str, surname: str, time: datetime) -> None:
#         self.name = name
#         self.surname = surname
#         self.time = time


# class Table:
#     def __init__(self, number_of_seats: int):
#         self.number_of_seats = number_of_seats
#         self.reservations: List[Reservation] = []

#     def create_reservation(self, name: str, surname: str, time: datetime):
#         reservation = Reservation(name, surname, time)
#         self.reservations.append(reservation)

#     def check_availability(self, time: datetime) -> bool:
#         for reservation in self.reservations:
#             if reservation.time == time:
#                 return False
#         return True


# class Meniu:
#     def __init__(self):
#         pass

#     def get_meniu():
#         pass

#     def put_order():
#         pass


from datetime import datetime
from typing import List


# class Restaurant:
#     def __init__(self) -> None:
#         self.tables = [Table(2), Table(4), Table(4), Table(6)]
#         self.menu = Menu()

#     def find_available_table(self, num_of_people: int, time: datetime) -> Table:
#         for table in self.tables:
#             if table.number_of_seats >= num_of_people and table.check_availability(time):
#                 return table
#         return None


class Reservation:
    def __init__(self, name: str, surname: str, time: datetime) -> None:
        self.name = name
        self.surname = surname
        self.time = time


class Table:
    def __init__(self, number_of_seats: int):
        self.number_of_seats = number_of_seats
        self.reservations: List[Reservation] = []

    def create_reservation(self, name: str, surname: str, time: datetime):
        reservation = Reservation(name, surname, time)
        self.reservations.append(reservation)

    def check_availability(self, time: datetime) -> bool:
        for reservation in self.reservations:
            if reservation.time == time:
                return False
        return True


class Menu:
    def __init__(self):
        self.menu_items = {
            "Burger": 10.99,
            "Pizza": 12.99,
            "Pasta": 8.99,
            "Salad": 6.99,
        }

    def get_menu(self):
        return self.menu_items

    def place_order(self, item: str, quantity: int) -> float:
        if item not in self.menu_items:
            return None
        return self.menu_items[item] * quantity

        reserved_tables = {}


# Get user input for name, surname, number of guests, and reservation time
name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
num_guests = int(input("Please enter the number of guests: "))
res_time = int(input("Please enter time for reservation: "))

# Check if the requested table is available
if reserved_tables.get(res_time):
    if len(reserved_tables[res_time]) >= 10:
        print("Sorry, there are no available tables for that time.")
    else:
        table_num = max(reserved_tables[res_time]) + 1
        reserved_tables[res_time].append(table_num)
        print(
            f"{name}, {surname} your table is: {table_num} reserved at {res_time} o'clock"
        )
else:
    reserved_tables[res_time] = [1]
    print(f"{name}, {surname} your table is: 1 reserved at {res_time} o'clock")
