numbers = input("Podaj liczby podzielone spacją -> ")
numbers = numbers.split()
print(numbers)

print('Czy pierwszy i ostatni są takie same ->', numbers[0] == numbers[-1])
