class Point:
    def __init__(self, num):
        self.__street = 'ul. Wileńska'
        self.num = num

    def get_address(self): #getter
        return self.__street

    def set_address(self, value): #setter
        self.__street = value

address = Point(10)
print(address.num)
print(address.get_address())
address.set_address('ul. Warszawska')
print(address.get_address())