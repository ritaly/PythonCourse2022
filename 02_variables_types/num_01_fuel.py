# Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny. Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.

price = 5.04
usage = 6.4
distance = 120

cost = price * usage * distance / 100

print('Koszt podrozy to:', round(cost,2), 'PLN')