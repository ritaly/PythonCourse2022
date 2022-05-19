# numbers = (1, 3, 4, 20, 13, 16, 9)
#
# num = input("Podaj liczbę od 1 do 20 ->")
# flag = False
#
# for i, v in enumerate(numbers):
#     if int(num) == v:
#         print('znalazłem, pod indexem:', i)
#         flag = True
#         break
#
# if not flag:
#     print('nie ma takiej liczby')

num = input("Podaj liczbę od 1 do 20 ->")
num = int(num)
numbers = (1, 3, 4, 20, 13, 16, 9)

if num in numbers:
    print('znalazłem, pod indexem:', numbers.index(num))
else:
    print('nie ma takie liczby')
