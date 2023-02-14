#Create a variables containing strings for username and password. Start Endless loop allowing to enter username and password. 
#If credentials are correct stop endless loop and print greeting message.

USER = "Andrius"
PASSWORD = "codeacademy"

while USER != input("Please enter user name: "):
    print("wrong user")
while PASSWORD != input("Please enter password: "):
     print("wrong password")
else:
    print("Hi Andrius")


# padaryti uzduoti kai ivedamas useris ir paswordas per viena karta