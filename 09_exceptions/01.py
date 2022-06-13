numbers = [13, "hello", 3.14, True, None, [12, 4], 0, {}]

for i in numbers:
    try:
        result = 10/i
        print(result)
    except (TypeError, ZeroDivisionError):
        print(f"10/{i} Nie moge wykonać")