# Create a few examples of yourself where you show two pillars of OOP in action.
# Inheritance, Polymorphism

#  Inheritance, (child class) for organization and avoiding duplication:

class Fishes:
    def __init__(self, title:str, size:int)->None:
        self.title = title
        self.size = size
      

    def get_fish_title(self)->None:
        print(self.title) 

    def get_fish_size(self)->None:
        print(self.size)

    
class Perch(Fishes):

    def __init__(self, title:str, size:int, color:str)->None:
        super().__init__(title, size)
        self.color = color
    def get_color (self):
            print(self.color)    

class Pike(Fishes):

    def __init__(self, title:str, size:int, legal_size:int)->None:
        super().__init__(title, size)
        self.legal_size = legal_size
    
    def get_legal_size_to_catch(self):
        return f"Legal size to catch is 50cm"    
    

fish_name = Fishes("Perch", 50)
print(fish_name.get_fish_size())