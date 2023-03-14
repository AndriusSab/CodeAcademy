class Item:

    def __init__(self, name, price, quantity):
        
        assert price >= 0, f"Price {price} should be greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} should be greater or equal to zero!"

        self.name = name,
        self.price = price
        self.quantity = quantity
    
    def calculaate_total_price (self):
        return  self.price * self.quantity
    
    def calculate_print_quantiy(self):

        print(f"Total left: {self.quantity}")   

item1 = Item("Iphone", -10, 0)
# print(item1.calculaate_total_price())

# print(item1.name)
# print(item1.quantity)
item1.calculate_print_quantiy()


# class Elektricity:
#     def __init__(self, price_kw: float, watts: int) -> None:
        
#         voltage = 240
#         self.price_kw = price_kw
#         self.watts = watts  
        

#     def price_calculator(self):
#         return self.watts * self.price_kw

# class Ignitis:
    

