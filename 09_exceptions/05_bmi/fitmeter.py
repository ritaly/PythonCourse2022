import bmi


def open_advice(filename):
    with open(f'{filename}.txt') as f:
        advice = f.read()

    return advice


def get_value(message, min_max):
    while True:
        try:
            value = float(input(message))
            minium, maxium = min_max

            if not (value in range(minium, maxium)):
                raise ValueError

        except (TypeError, ValueError):
            print('Wartośc jest nie prawidłowa, spróbuj jeszcze raz...')
        else:
            return value

def main():
    w = get_value("Podaj wagę [kg]", (20, 200))
    h = get_value("Podaj wzrost [cm]", (140, 250)) / 100

    result = bmi.calc_bmi(h, w)
    status = bmi.get_bmi_status(result)
    advice = open_advice(status)
    print(status.upper(), '***************')
    print(advice)

if __name__ == "__main__":
    main()