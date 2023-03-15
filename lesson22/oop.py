class Vehicle:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_namae(self) -> str:
        return self.name


class Golfiukas(Vehicle):
    def __init__(self, name: str, cost: float) -> None:
        super().__init__(name)
        self.cost = cost

    def get_cost(self) -> float:
        return self.cost


CAR_NAME = "Good car"
my_car = Golfiukas(name=CAR_NAME, cost=100)

print(my_car.get_cost())
