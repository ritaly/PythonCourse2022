# Stwórz abstrakcyjną klasę Pojazdy.
# Utwórz potomne klasy pojazdy np. Samochód, Rower, Autobus, Ciężarówki.
# Dodaj opisy zgodne z tym jak te pojazdy są klasyfikowane.
# Jaki rodzaj dokumentu jest potrzebny, by kierować poszczegolnym pojazdem.
#
# AM rower
# B auto
# C cieżarówka
# D autobus

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def desc(self):
        pass

    @abstractmethod
    def licence(self):
        pass


class Bike(Vehicle):
    def licence(self):
        return 'AM'

    def desc(self):
        return 'you can pass your bike card in age: 10+'


class Car(Vehicle):
    def licence(self):
        return 'B'

    def desc(self):
        return 'you can pass your car licence in age: 18+'

    def max_speed(self):
        return '180'

class Truck(Vehicle):
    def licence(self):
        return 'C'

    def desc(self):
        return '...'

class Bus(Vehicle):
    def licence(self):
        return 'E'

    def desc(self):
        return 'bus category'

def main():
    b = Bike()
    print(b.licence())

    c = Car()
    print(c.licence())
    print(c.max_speed())

    #...
    # bus, truck


if __name__ == '__main__':
    main()