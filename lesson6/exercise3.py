#allow user to enter two numbers, print out which one is higher than the other, or are they equal?

number_1= int(input("Enter first number: "))
number_2= int(input("Enter secondnumber: "))



if number_1>number_2:
    print ("First number is higher than second number")
elif number_1<number_2:
    print("Second number is higher than first number")
elif number_1==number_2:
   print("First and second numbers are equal")
else:
    print("Fisnish!")
