import bmi

DEFAULT_W = 60

def open_advice(filename):
    with open(f'{filename}.txt') as f:
        advice = f.read()

    return advice

def get_user_values():
    while True:
        try:
            w = float(input("Podaj swoja mase kg"))
            h = float(input("Podaj swoj wzrost w m "))
            return w, h
        except (TypeError, ValueError):
            print('Podaj wartosci ponownie')


def main():
    w, h = get_user_values()

    result = w * h # metoda licząca bmi
    print(result)




    h = 1.6

    result = bmi.calc_bmi(h, w)
    status = bmi.get_bmi_status(result)
    advice = open_advice(status)
    print(status.upper(), '***************')
    print(advice)

if __name__ == "__main__":
    main()