def calc_circle_field(r):
    pi = 3.14
    return pi * r**2


# ---
radius = float(input('Podaj promień koła -> '))
field = calc_circle_field(radius)
print('Pole koła to:', field)
