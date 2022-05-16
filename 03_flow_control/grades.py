sum_grades = 0
for i in range(3):
    subject = input("Podaj nazwę przedmiotu: ")
    grade = int(input(f'Podaj ocenę z {subject}: '))
    print(f'Ocena z {subject} to {grade}')
    sum_grades += grade

print(f'Twoja średnia ocen z 3 przedmiotów to { round(sum_grades/3, 2)}')

tries = 0
while tries < 3:
    sub = input("Subject")
    grade = int(input("Grade in a scale 1-6 (integers only)"))
    tries = tries+1
    print(f'Your subject is {str(sub)} and grade is {grade}')