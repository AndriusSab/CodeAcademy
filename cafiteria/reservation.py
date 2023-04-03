# # #  a specific number single, double or family tables)
# # import time


# # class TableReservation:
# #     def __init__(self):
# #         self.reserved_tables = {
# #             # "Single": {
# #             #     "Table_one": {"name": "Antanas", "status": "Reserved"},
# #             #     "Table_two": {"name": "None", "status": "Available"},
# #             #     "Table_tree": {"name": "None", "status": "Available"},
# #             #     "Table_four": {"name": "None", "status": "Available"},
# #             # },
# #             # "Double": {
# #             #     "Table_one": {"name": "None", "status": "Available"},
# #             #     "Table_two": {"name": "Andrius", "status": "Reserved"},
# #             #     "Table_tree": {"name": "None", "status": "Available"},
# #             #     "Table_four": {"name": "None", "status": "Available"},
# #             # },
# #             # "Family": {
# #             #     "Table_one": {"name": "None", "status": "Available"},
# #             #     "Table_two": {"name": "Jonas", "status": "Reserved"},
# #             #     "Table_tree": {"name": "None", "status": "Available"},
# #             #     "Table_four": {"name": "None", "status": "Available"},
# #             # },
# #         }

# #     def reserve_table(self, name:str, num_guests:int, res_time:time.time) -> None:

# #     def get_table_status(self, name:str) -> str:

# #     def get_table_num_guests(self, name:str) -> int:

# #     def get_table_name(self, name:str) -> str:

# #     def get_table_reserved_time(self, name:str) -> time.time:


# # if __name__ == "__main__":
# #     table_reservation = TableReservation()
# #     fulname = input("Please enter your surname: ")
# #     num_guests = int(input("Please enter the number of guests: "))
# #     res_time = int(input("Please enter time for reservation: "))
# #     table_reservation.reserve_table(name, surname, num_guests, res_time)


# # import time


# # class TableReservation:
# #     def __init__(self):
# #         self.reserved_tables = {
# #             "Single": {
# #                 "Table_one": {"name": "Antanas", "status": "Reserved"},
# #                 "Table_two": {"name": "None", "status": "Available"},
# #                 "Table_tree": {"name": "None", "status": "Available"},
# #                 "Table_four": {"name": "None", "status": "Available"},
# #             },
# #             "Double": {
# #                 "Table_one": {"name": "None", "status": "Available"},
# #                 "Table_two": {"name": "Andrius", "status": "Reserved"},
# #                 "Table_tree": {"name": "None", "status": "Available"},
# #                 "Table_four": {"name": "None", "status": "Available"},
# #             },
# #             "Family": {
# #                 "Table_one": {"name": "None", "status": "Available"},
# #                 "Table_two": {"name": "Jonas", "status": "Reserved"},
# #                 "Table_tree": {"name": "None", "status": "Available"},
# #                 "Table_four": {"name": "None", "status": "Available"},
# #             },
# #         }

#     def reserve_table(self, name:str, surname:str, num_guests:int, res_time:time) -> None:
#         # Find an available table and reserve it
#         for table_type, tables in self.reserved_tables.items():
#             for table_name, table in tables.items():
#                 if table["status"] == "Available":
#                     table["name"] = f"{name} {surname}"
#                     table["num_guests"] = num_guests
#                     table["res_time"] = res_time
#                     table["status"] = "Reserved"
#                     print(f"Table {table_name} has been reserved for {name} {surname}.")
#                     return
#         print("Sorry, there are no tables available.")

#     def get_table_status(self, name:str) -> str:
#         # Find the table with the given name and return its status
#         for table_type, tables in self.reserved_tables.items():
#             for table_name, table in tables.items():
#                 if table["name"] == name:
#                     return table["status"]
#         return "Table not found."

#     def get_table_num_guests(self, name:str) -> int:
#         # Find the table with the given name and return the number of guests
#         for table_type, tables in self.reserved_tables.items():
#             for table_name, table in tables.items():
#                 if table["name"] == name:
#                     return table["num_guests"]
#         return -1

#     def get_table_name(self, name:str) -> str:
#         # Find the table with the given name and return its name
#         for table_type, tables in self.reserved_tables.items():
#             for table_name, table in tables.items():
#                 if table["name"] == name:
#                     return table_name
#         return "Table not found."

#      def get_table_reserved_time(self, name:str) -> time:
#         """
#         Returns the reservation time for the table with the given name.
#         If the table is not found or not reserved, returns None.
#         """
#         for table_type in self.reserved_tables:
#             for table_name, table_info in self.reserved_tables[table_type].items():
#                 if table_name == name and table_info["status"] == "Reserved":
#                     return table_info["reserved_time"]
#         return None


#     if __name__ == "__main__":
#     table_reservation = TableReservation()
#     fulname = input("Please enter your surname: ")
#     num_guests = int(input("Please enter the number of guests: "))
#     res_time = int(input("Please enter time for reservation: "))
#     table_reservation.reserve_table(name, surname, num_guests, res_time)


# from datetime import datetime, time


# class TableReservation:
#     def __init__(self):
#         self.reserved_tables = {
#             "small": {
#                 "T1": {
#                     "name": "",
#                     "num_guests": 2,
#                     "res_time": None,
#                     "status": "Available",
#                 },
#                 "T2": {
#                     "name": "",
#                     "num_guests": 2,
#                     "res_time": None,
#                     "status": "Available",
#                 },
#             },
#             "large": {
#                 "T3": {
#                     "name": "",
#                     "num_guests": 4,
#                     "res_time": None,
#                     "status": "Available",
#                 },
#                 "T4": {
#                     "name": "",
#                     "num_guests": 4,
#                     "res_time": None,
#                     "status": "Available",
#                 },
#             },
#         }

#     def reserve_table(
#         self, name: str, surname: str, num_guests: int, res_time: time
#     ) -> None:
#         # Find an available table and reserve it
#         for table_type, tables in self.reserved_tables.items():
#             for table_name, table in tables.items():
#                 if table["status"] == "Available":
#                     table["name"] = f"{name} {surname}"
#                     table["num_guests"] = num_guests
#                     table["res_time"] = res_time
#                     table["status"] = "Reserved"
#                     print(f"Table {table_name} has been reserved for {name} {surname}.")
#                     return
#         print("Sorry, there are no tables available.")

#     def get_table_status(self, name: str) -> str:
#         # Find the table with the given name and return its status
#         for table_type, tables in self.reserved_tables.items():
#             for table_name, table in tables.items():
#                 if table["name"] == name:
#                     return table["status"]
#         return "Table not found."

#     def get_table_num_guests(self, name: str) -> int:
#         # Find the table with the given name and return the number of guests
#         for table_type, tables in self.reserved_tables.items():
#             for table_name, table in tables.items():
#                 if table["name"] == name:
#                     return table["num_guests"]
#         return -1

#     def get_table_name(self, name: str) -> str:
#         # Find the table with the given name and return its name
#         for table_type, tables in self.reserved_tables.items():
#             for table_name, table in tables.items():
#                 if table["name"] == name:
#                     return table_name
#         return "Table not found."

#     def get_table_reserved_time(self, name: str) -> time:
#         # Find the table with the given name and return its reserved time
#         for table_type, tables in self.reserved_tables.items():
#             for table_name, table in tables.items():
#                 if table["name"] == name and table["status"] == "Reserved":
#                     return table["res_time"]
#         return None


# if __name__ == "__main__":
#     table_reservation = TableReservation()
#     fulname = input("Please enter your surname: ")
#     num_guests = int(input("Please enter the number of guests: "))
#     res_time = int(input("Please enter time for reservation: "))
#     table_reservation.reserve_table(fulname, num_guests, res_time))


from datetime import time


class TableReservation:
    def __init__(self):
        self.reserved_tables = {
            "single": {
                "1": {
                    "name": "Andrius Sabaliauskas",
                    "num_guests": 1,
                    "res_time": None,
                    "status": "Available",
                },
                "2": {
                    "name": "",
                    "num_guests": 1,
                    "res_time": None,
                    "status": "Reserved",
                },
                "3": {
                    "name": "",
                    "num_guests": 1,
                    "res_time": None,
                    "status": "Reserved",
                },
            },
            "double": {
                "1": {
                    "name": "",
                    "num_guests": 2,
                    "res_time": None,
                    "status": "Reserved",
                },
                "2": {
                    "name": "",
                    "num_guests": 2,
                    "res_time": None,
                    "status": "Reserved",
                },
                "3": {
                    "name": "",
                    "num_guests": 2,
                    "res_time": None,
                    "status": "Reserved",
                },
            },
            "family": {
                "1": {
                    "name": "",
                    "num_guests": 6,
                    "res_time": None,
                    "status": "Reserved",
                },
                "2": {
                    "name": "",
                    "num_guests": 6,
                    "res_time": None,
                    "status": "Reserved",
                },
                "3": {
                    "name": "",
                    "num_guests": 6,
                    "res_time": None,
                    "status": "Reserved",
                },
            },
        }

    def check_table_by_name(
        self, fullname: str, num_guests: int, res_time: time
    ) -> None:
        for table_type, tables in self.reserved_tables.items():
            for table_name, table in tables.items():
                if table["name"] == fullname:
                    print(f"Sorry, {fullname} already has a table reserved.")
                    return

    def reserve_table(self, fullname: str, num_guests: int, res_time: time) -> None:
        if num_guests <= 2:
            table_type = "small"
        elif num_guests <= 10:
            table_type = "family"
        else:
            table_type = "large"

        for table_type, tables in self.reserved_tables.items():
            for table_name, table in tables.items():
                if table["status"] == "Available":
                    table["name"] = fullname
                    table["num_guests"] = num_guests
                    table["res_time"] = res_time
                    table["status"] = "Reserved"
                    print(
                        f"Table {table_type, table_name} has been reserved for {fullname}."
                    )
                    return
        print("Sorry, there are no tables available.")

    def get_table_status(self, name: str) -> str:
        for table_type, tables in self.reserved_tables.items():
            for table_name, table in tables.items():
                if table["name"] == name:
                    return table["status"]
        return "Table not found."

    def get_table_num_guests(self, name: str) -> int:
        for table_type, tables in self.reserved_tables.items():
            for table_name, table in tables.items():
                if table["name"] == name:
                    return table["num_guests"]
        return -1

    def get_table_name(self, name: str) -> str:
        for table_type, tables in self.reserved_tables.items():
            for table_name, table in tables.items():
                if table["name"] == name:
                    return table_name
        return "Table not found."

    def get_table_reserved_time(self, name: str) -> time:
        for table_type, tables in self.reserved_tables.items():
            for table_name, table in tables.items():
                if table["name"] == name and table["status"] == "Reserved":
                    return table["res_time"]
        return None


if __name__ == "__main__":
    table_reservation = TableReservation()
    fullname = input("Please enter your full name: ").upper()
    num_guests = int(input("Please enter the number of guests: "))
    res_time = int(input("Please enter time for reservation: "))
    # table_reservation.reserve_table(fullname, num_guests, res_time)
    print(table_reservation.get_table_name(fullname))
