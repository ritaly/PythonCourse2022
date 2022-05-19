txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

txt = txt.replace(',', '')
txt = txt.lower()
words = txt.split()

words_counter = {}

for word in words:
    if word in words_counter:
        words_counter[word] += 1
    else:
        words_counter[word] = 1

for k, v in words_counter.items():
    print(f'- {k} : {v}')

# text = """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""
#
# text = text.lower().replace(',', '')
#
# list_of_words = text.split()
# unique_words = set(list_of_words)
#
# words_dict = {}
#
# for i in unique_words:
#     words_dict[i] = list_of_words.count(i)
#
# print(words_dict)