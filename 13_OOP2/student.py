import datetime
import holidays


class Student:
    university = 'New York Academy'
    min_avg = 4.5
    university_code = 'UAM'

    def __init__(self, first, last, age, avg):
        self.first = first
        self.last = last
        self.age = age
        self.avg = avg

    def __repr__(self):
        return self.first.capitalize() + " " + self.last.capitalize() + " średnia: " + str(self.avg)

    def email(self):
        return f'{self.last}.{self.first}@{self.university_code}.com'

    def grant_scholarship(self):
        if self.avg >= self.min_avg:
            print('Gratulacje, otrzymano stypendium')
        else:
            print('Odmowa przydzielnia stypendium')

    @classmethod
    def set_min_avg(cls, average):
        cls.min_avg = average

    @classmethod
    def set_university_code(cls, code):
        cls.university_code = code

    @staticmethod
    def academic_day(day):
        pl_holidays = holidays.Poland()
        if day.weekday() in (5, 6) or day in pl_holidays:
            return False
        else:
            return True


def main():
    obj_anna = Student('anna', 'kowalska', 23, 4.3)
    obj_arek = Student('arkadiusz', 'nowak', 21, 4)

    # print(obj_anna)
    # Student.set_min_avg(4)
    # obj_anna.grant_scholarship()
    #
    # print(obj_anna.min_avg)
    # print(obj_arek.min_avg)
    # print(Student.min_avg)
    #
    # print(obj_arek)
    # obj_arek.grant_scholarship()

    obj_arek.set_university_code('uniadam')
    print(obj_anna.email())

    today = datetime.date.today()
    print('Is Anna on university?', obj_anna.academic_day(today))

    saturday = datetime.datetime.strptime('2022-07-09', '%Y-%m-%d')
    print('2022-06-09 is academic day? ', Student.academic_day(saturday))

    polish_holiday = datetime.datetime.strptime('2022-01-06', '%Y-%m-%d')
    print('2022-01-06 is academic day? ', Student.academic_day(saturday))



if __name__ == '__main__':
    main()
