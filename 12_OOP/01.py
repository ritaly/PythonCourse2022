class Animal:
    def show_feature(self):
        return 'są cudzożywne'

class Mammal(Animal):
    def is_lifeborn(self):
        return True

class Dog(Mammal):
    def __init__(self, race):
        self.race = race

piesel = Dog('kundel')
print(piesel.race)
print(piesel.is_lifeborn())  # metoda z ssaków
print(piesel.show_feature()) # metoda z zwierząt
