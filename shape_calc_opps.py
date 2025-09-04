
from abc import ABC, abstractmethod

class Cal(ABC):  # Abstract base class
    @abstractmethod
    def area(self):
        pass

class Rectangle(Cal):
    def area(self, l, b):  # Rectangle area: l × b
        return l * b

class Square(Cal):
    def __init__(self, s):
        self.__s = s

    def get_formula(self):
        return f"{self.__s} * {self.__s} = {self.__s * self.__s}"

    def area(self):
        return self.__s * self.__s

if __name__ == "__main__":
    s = Square(5)
    print("Square:")
    print("Formula:", s.get_formula())
    print("Area:", s.area())

    r = Rectangle()
    print("\nRectangle:")
    print("Area:", r.area(5, 10))
