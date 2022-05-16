op1 = int(input("Podaj opinie "))
op2 = int(input("Podaj opinie "))
op3 = int(input("Podaj opinie "))

result = (op1 + op2 + op3) / 3
if result > 7:
    print("Bardzo dobry")
elif result >= 5:
    print("Przecietna")
else:
    print("Nie warta uwagi")