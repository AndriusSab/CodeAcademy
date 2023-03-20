# Task Nr.2:

# Create an abstract class Money which takes currency and value as input and initializes it.
# A class must have these methods:
# get_value method which returns the value of the money.
# get_currency method which returns the currency of the money.
# convert_to_currency abstract method, which takes target currency and conversion rate as input and converts the value of the money to the target currency.
# Now create two subclasses of Money: Cash and Card. The Cash class should take the denomination of the cash as input in the constructor, and should implement the convert_to_currency method. The Card class should take the credit limit of the card as input in the constructor, and should implement the convert_to_currency method using the conversion rate to convert the value of the card to the target currency.

# Answer


from abc import ABC, abstractclassmethod


class Money(ABC):
    @abstractclassmethod
    def get_value(self) -> float:
        pass

    @abstractclassmethod
    def get_currency(self) -> float:
        pass

    @abstractclassmethod
    def convert_to_currency(self) -> float:
        pass


class Cash(Money):
    def __init__(self, cash: float) -> float:
        self.cash = cash

    @abstractclassmethod
    def convert_to_currency(self) -> float:
        pass


class Card(Money):
    def __init__(self, limit: float) -> float:
        self.limit = limit

    CONVERSATIO_RATE = 1, 4  # currency rate

    @abstractclassmethod
    def convert_to_currency(self) -> float:
        return self.limit * Card.CONVERSATIO_RATE

    @abstractclassmethod
    def get_value(self) -> float:
        pass

    @abstractclassmethod
    def get_currency(self) -> float:
        pass


card = Card(100)
print(card.convert_to_currency())
