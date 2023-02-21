# Create a function that takes one parameter as number - age , other as name which is default 'Anatnas', and some args and keywords.
# Print first Name with age;
# And then print all arguments with key arguments.


# from typing import Any

# def print_name_and_age_with_arguments(age:int, name: str = "Antanas", *args, **kwargs) -> None:
#     print (f"Name is: {name},age {age} ")
#     print(f"free arguments: {args if args else '' }, free key arguments: {kwargs if kwargs else 'Missing args and kwargs'}")

# print_name_and_age_with_arguments(25, "tom", "antanas petras", street = "Gedimino")

# from typing import Union

from ctypes import Union


def divider(number:Union[float,int] )-> Union[float, int]:
        return number/2 if isinstance(number, float) else number //2
try: 
     my_divided_number = divider(10)
     print (my_divided_number)
except TypeError:
     print ("please enter number or float")

try: 
     my_divided_number = divider(number=10)       # apsirasome kuri parametra paduodm "number" sikart
     print (my_divided_number)
except ZeroDivisionError:
      print("dalyba is nulio negalima")

except FileNotFoundError:
print('Failas nerastas')  #create new file toliau gali eiti bet kokia funkcija     
except Exception as e:          # apibudinam visus exception kaip "e" naudot visur
       print(f'Error:{e}')
else:  # else vykdomas kai musu kodas neissaukia jokiu klaidu, t.y attinka visas uzduotas salygas
   finally:
    print("atspausdinu visada kas beivyktu")    

# def phisics_is_fun(tem_c:float, preasure_bar: float, time,utc:int, weight_kg:float)-> None:
#     pass
# phisics_is_fun (tem_c = 55.87,preasure_bar=26.58,time_utc=125.89,weight_kg = 485)    # apsirasome kiekviena kintamaji

# def divider(number:Union[float,int] )-> Union[float, int]:
#      try:
#          return number/2 if isinstance(number, float) else number //2