def calendar(month, days):
    print()
    print(month)
    list_day = []

    for day in days:
        if day < 10:
            list_day.append(f"0{str(day)}")
        else:
            list_day.append(f"{str(day)}")

    week = ""
    for index, day in enumerate(list_day):
        if (index + 1) % 7 != 0:
            week += f"{day} "
        else:
            week += f"{day}\n"
    print(week)


def calendar_year():
    data = [
        ('January', range(31)),
        ('February', range(28)),
        ('March', range(31)),
        ('April', range(30)),
        ('May', range(31)),
        ('June', range(30)),
        ('July', range(31)),
        ('August', range(31)),
        ('September', range(30)),
        ('October', range(31)),
        ('November', range(30)),
        ('December', range(31)),
    ]

    for t in data:
        calendar(t[0], t[1])


calendar_year()