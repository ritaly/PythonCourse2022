import datetime
import holidays


def academic_day(day):
    pl_holidays = holidays.Poland()
    if day.weekday() in (5, 6) or day in pl_holidays:
        return False
    else:
        return True


def main():
    today = datetime.date.today()
    print(today)
    print(academic_day(today))


if __name__ == '__main__':
    main()
