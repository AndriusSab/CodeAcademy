
# Let user enter name, surname and age.
#  Print if user is allowed to enter an online casino or not. 21 is the age cap.

name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
age = int(input("Please enter you age: "))


if age>=21:
    print("You are allowed to enter Casino")
else:
    print("You are not allowed to enter Casino")