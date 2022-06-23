class Student:
    university_code = 'UAM'

    def __init__(self, imie, nazwisko, wiek):
        self.first = imie
        self.last = nazwisko
        self.age = wiek

    def email(self):
        return f'{self.first}.{self.last}@{self.university_code}.com'.lower()

    def hello(self):
        print('HEEEEEJ!!!')


anna = Student('Anna', 'Kowalska', 23)
print(anna.first)
print(anna.last, anna.first, anna.age, anna.email())
anna.last = 'Smith'
print(anna.last, anna.first, anna.age, anna.email())

anna.hello()
Student.hello(anna)

print(Student.email(anna))


# piotr = Student('Piotr', 'Nowak', 23)
#
# print(piotr.last, piotr.first, piotr.email)



