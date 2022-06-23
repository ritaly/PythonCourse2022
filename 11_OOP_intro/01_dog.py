class Dog:
    def __init__(self, name, color, race):
        self.name = name
        self.color = color
        self.race = race

    def how(self):
        print(f"{self.name} - How How")

    def tail_whip(self):
        return f"{self.name} whips his tail"


def main():
    tuptus = Dog("Tuptuś", "black", "Jamnik")
    benek = Dog("Benek", "Grey", "Kundel")
    tuptus.how()
    print(benek.tail_whip())

if __name__ == '__main__':
    main()