# Task Nr.4:

# Create a Calculator program : it should contain abstract class with methods
#  (abstract and not), base class, geometry, arithmetic calculator classes.
#  Every subclass should have at least 5 methods to make some meaningful calculus operations.

from abc import ABC, abstractmethod


class AbstractCalc(ABC):
    @abstractmethod
    def get_volume_sphere(self) -> float:
        pass


class Calculator(AbstractCalc):
    def __init__(
        self, lenght: float, width: float, height: float, number1: float, number2: float
    ) -> None:
        self.lenght = lenght
        self.width = width
        self.height = height
        self.number1 = number1
        self.number2 = number2

    def get_lenght(self) -> float:
        return self.lenght

    def get_width(self) -> float:
        return self.width

    def get_height(self) -> float:
        return self.height

    def get_number1(self) -> float:
        return self.number1

    def get_number2(self) -> float:
        return self.number2


class Geommetry(Calculator):
    PI = 3, 14

    def __init__(
        self,
        radius: float,
        lenght: float,
        width: float,
        height: float,
        number1: float,
        number2: float,
    ) -> None:
        self.radius = radius
        super().__init__(lenght, width, height, number1, number2)

    def get_area_rectangular(self):
        return self.lenght * self.width

    def get_volume_rectangular(self):
        return self.lenght * self.width * self.height

    def get_area_triangle(self):
        return self.lenght * self.width * 1 / 2

    def get_volume_sphere(self) -> float:
        return 3 / 4 * Geommetry.PI * self.radius**3

    def get_volume_cilinder(self) -> float:
        return Geommetry.PI * self.radius**2 * self.height


# class Arithmetic(Calculator):
#     def __init__(
#         self, lenght: float, width: float, height: float, number1: float, number2: float
#     ) -> None:
#         super().__init__(lenght, width, height, number1, number2)


parameters = Geommetry(1, 8, 5, 1, 7, 8)

print(parameters.get_volume_sphere())
