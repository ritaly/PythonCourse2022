def greet(hello, name):
    name = name.capitalize()
    print(hello, name, '***')


def main():
    phase = 'HEEEELLLOOO!'

    girl = 'anna'
    greet(phase, girl)

    print(phase, girl, name) # !!! błąd - name jest zmienną lokalną w funkcji greet

main()

