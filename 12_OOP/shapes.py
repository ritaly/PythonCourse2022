from abc import ABC, abstractmethod

class AbstractShape(ABC): #klasa abstrakcyjna
    @abstractmethod
    def sides(self):
        pass


class Triangle(AbstractShape):
    def sides(self):
        return 3


class Square(AbstractShape):
    def sides(self):
        return 4

    def area(self, side):
        return side * side

# t = Triangle()
# print(t.sides())

s = Square()
print(s.sides())
print(s.area(3))