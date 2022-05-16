numbers = '325354756'
mixed = 'q34324ffagtr43'

print(f'Ciąg {numbers} zawiera same cyfry ->', numbers.isdigit())
print(f'Ciąg {mixed} zawiera same cyfry ->', mixed.isdigit())

# ----

txt = 'mata'
centered_txt = txt.center(10, '*')
print(centered_txt)

# ---
url = 'www.example.com'
new_url = url.lstrip('w.')
print(new_url)


dna = 'AAATTTGGCCAAAAAA'
cleaned_dna = dna.rstrip('A')
print(cleaned_dna)
# ---

password = 'AdminAdminTakNieRobHasla'

includes_at_least_1_upper = password.isalpha() and (not password.islower() and not password.isupper() )

print(includes_at_least_1_upper)

# ---
fruit = 'banana'
counter = fruit.count('na')
print(counter)