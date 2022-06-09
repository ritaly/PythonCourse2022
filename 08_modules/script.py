# import longestwordfinder as finder

import example_package.module_2 as mod2
from longestwordfinder import find_longest_word, show, choice, letter



items = ['tent', 'bidon', 'glasses', 'mug', 'abrakadabra']

longest_word = find_longest_word(items)
show(longest_word)
print(choice(items))
print(letter)

print(mod2.get_name())