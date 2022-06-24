names = input("Enter names separated by commas: ").title().split(",")
tasks = input("Enter task counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} tasks left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, task, grade in zip(names, tasks, grades):
    print(message.format(name, task, grade, int(grade) + 1))
