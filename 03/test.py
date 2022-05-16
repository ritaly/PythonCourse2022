txt = "abrakadabra"

for letter in txt:
    print('- ', letter)


names = ["Ada", "Julia", "Ruby", "Perl"]

for step in names:
    print('Hello!', step)


for number in range(5, 20, 2):
    print('->', number)

print('----------------')
for index in range(4):
    print(index, names[index])

for index, elem in enumerate(txt):
    print(index, elem)

print('---------')

counter = len(txt)
for index in range(0, counter, 2):
    print(index, txt[index])
