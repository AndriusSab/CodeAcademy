# A country can be said as being big if it is:
# Big in terms of population.
# Big in terms of area.
# Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

# Population is greater than 250 million.
# Area is larger than 3 million square km.
# Also, create a method which compares a country's population density to another country object. Return a string in the following format:

# {country} has a {smaller / larger} population density than {other_country}
# Examples:

# australia = Country("Australia", 23545500, 7692024)
# andorra = Country("Andorra", 76098, 468)

# australia.is_big ➞ True
# andorra.is_big ➞ False
# andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"

class Country:
        def __init__(self,  country: str, population:int, area: int):
               self.country: str = country
               self.populution: int = population
               self.area: int = area
        
        def is_big(self)-> bool:
               if self.area > 3000000 and self.populution > 25000000:
                    status = True
               else:
                     status = False
               return status 
            
        def compare_pd(self, second:"Country"):
              if (self.populution/self.area)>(second.populution/second.area):
                    print(f"{self.country} has larger population density than {second.country}") 
              else:
                    print(f"{second.country} has larger population density than {self.country}") 
                  
australia = Country("Australia", 235555550, 765662626)
andorra = Country("Andora", 76098, 468)

print(australia.is_big())
andorra.compare_pd(australia)
                    
                        
                        