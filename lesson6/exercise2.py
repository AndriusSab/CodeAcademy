# Create a database (List of privileged users)
#  print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

user = input("Enter your name: ")
privileged_users = ["Andrius", "Darius", "Arturas"]
if user in privileged_users:
    print(f"Welcome back{user}")
else:
    print(f"Welcome"{user})