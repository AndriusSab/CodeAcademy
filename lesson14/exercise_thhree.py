# Create 3 functions, that are related to each other (one is being called in another), 
# and test all logger severity levels by your own design.


def fishing_line (line_lenght: float) -> float:
    if line_lenght in range(200): 
        return  line_lenght

def fishing_reel_capacity (capacity: float) -> float:
    if fishing_line(0):
        return 