# Write a small calculator application, that allows user to enter two numbers and a symbol, 
# given and then do the operation and print an answer.



first_number = int(input('Enter first number: '))
second_number = int(input("Enter second number: "))
simb = input('Enter symbol of calc operation you want to make from list [+-*/]:  ')

#patikrino ar yra reiksmes simb liste
operation_list = ['+', '-', '*', '/' ]

if simb in operation_list:
    if simb == '+':
        answer = first_number + second_number
    if simb == '-':
        answer = first_number - second_number
    if simb == '*':
        answer = first_number * second_number
    if simb == '/':
        answer = first_number + second_number
    print(answer)
else: 
    print('too much of symbols')
    

# #ver1

# firstnumber = int(input("Enter first number: "))
# secondnumber = int(input("Enter second number: "))
# simb = input("Enter symbol of calc operation you want to make+ for addition - for subtraction * for multiplication / for division ")
# summary = firstnumber+secondnumber
# subtraction = firstnumber-secondnumber
# multiplication = firstnumber*secondnumber
# division = firstnumber/secondnumber
# if simb == '+':
#     print(f"Sum of firstnumber + secondnumber =  : ", {summary})
# if simb == '-':
#     print(f"Subtraction of firstnumber - secondnumber =  : ", {subtraction})
# if simb == '*':
#     print(f"Multiplication of firstnumber * secondnumber =  : ", {multiplication})
# if simb == '/':
#     print(f"Division of firstnumber / secondnumber =  : ", {division})
# else:
#     print("Entered symbol is not from this list (+-*/)")



# first_number = int(input('Enter first number: '))
# second_number = int(input("Enter second number: "))
# simb = input('Enter symbol of calc operation you want to make from list [+-*/]:  ')

# operation_list = ['+','-', '*', '/' ]
# summary = first_number + second_number
# subtraction = first_number - second_number
# multiplication = first_number * second_number
# division = first_number / second_number

# suma = f'Sum of first number + second number = '
# atimtis = f'Subtraction of first number - second number =  '
# daugyba =f'Multiplication of first number * second number = '
# dalyba = f'Division of first number / second number = '