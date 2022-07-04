from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def poop(self):
        pass


class Horse(Animal):
    def poop(self):
        print("Poop poop")

    def fly(self):
        print("Horse can't fly")


class Unicorn(Animal):
    def poop(self):
        print("Rainboooowww")

    def fly(self):
        print("Unicorn can fly with magical power")


class Cat(Animal):
    def meow(self):
        return 'meow meuw'

    def poop(self):
        print('idę do kuwety')

def family_test(animal):
    animal.poop()


arrow = Horse()
cute = Unicorn()
kitty = Cat()


family_test(arrow)
family_test(cute)
family_test(kitty)