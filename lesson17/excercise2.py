# Create the instance attributes fullname and email in the Employee class. 
# Given a person's first and last names:

# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, 
# and follow it with @company.com at the end. Make sure the entire email is in lowercase.

class Employer:
     def __init__(self, name:str, surname: str):
        self.name: str = name
        self.surname: str = surname
     def fullname(self):
         Fullname = self.name + " " + self.surname
         return  f"Your fullname is: {Fullname}"
     
     def name_surname_dot_joined(self):
         Fullname_with_dot = self.name +"." +self.surname
         return f"Your fullname with dot is: {Fullname_with_dot}"
     
     def email(self):
         Email = self.name.lower() +"." +self.surname.lower() + "@company.com"
         return f"Your email is:  {Email}"
     
naming = Employer("Andrius", "Sabaliauskas")

print(naming.fullname())
print(naming.name_surname_dot_joined())
print(naming.email())