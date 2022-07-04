class Student:
  university = 'New York Academy'
  min_avg = 4.5
  # university name abreviation UAM

  def __init__(self, first, last, age, avg):
    self.first = first
    self.last = last
    self.age = age
    self.avg = avg

  def __repr__(self):
    return self.first.capitalize() + " " + self.last.capitalize() + " średnia: " + str(self.avg)

  def email(self):
    return f'{self.last}.{self.first}@university.com' # abreviation

  def grant_scholarship(self):
    if self.avg >= self.min_avg:
      print('Gratulacje, otrzymano stypendium')
    else:
      print('Odmowa przydzielnia stypendium')

  @classmethod
  def set_min_avg(cls, average):
    cls.min_avg = average


obj_anna = Student('anna', 'kowalska', 23, 4.3)
obj_arek = Student('arkadiusz', 'nowak', 21, 4)

print(obj_anna)
Student.set_min_avg(4)
obj_anna.grant_scholarship()

print(obj_anna.min_avg)
print(obj_arek.min_avg)
print(Student.min_avg)

# print(obj_arek)
# obj_arek.grant_scholarship()