people = [
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]


for person in people:
    for index, value in enumerate(person):
        if index == 1:
            print(value, end=" | ")
        else:
            print(value, end=" ")
    print()