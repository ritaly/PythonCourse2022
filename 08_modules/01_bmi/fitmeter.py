import bmi


def open_advice(filename):
    with open(f'{filename}.txt') as f:
        advice = f.read()

    return advice


def main():
    w = float(input("Podaj wagę [kg]"))
    h = float(input("Podaj wzrost [m]"))

    result = bmi.calc_bmi(h, w)
    status = bmi.get_bmi_status(result)
    advice = open_advice(status)
    print(status.upper(), '***************')
    print(advice)

if __name__ == "__main__":
    main()