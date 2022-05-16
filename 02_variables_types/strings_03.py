quote = "Honesty is the first chapter in the book of wisdom."

# Policz wszystkie znaki w napisie
print('Liczba liter w ciąg ->',len(quote))

# Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[-7:-1])

# Wyświetl tylko pierwszą połowę tekstu
id_half = len(quote)//2
print(quote[:id_half+1])

# Wyświetl tylko kropkę
print(quote[-1])

# Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[id_half::3])

# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[::2])

# Wyświetl cały cytat odwrotnie
print(quote[::-1])

# Zamień wisdom na słowo friendship
new_quote = quote.replace('wisdom', 'friendship')
print(new_quote)