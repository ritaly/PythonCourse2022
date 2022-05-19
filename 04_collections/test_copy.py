import copy as c

oryginal_tab = [[1, 2], [3, 4], [5, 6]]
copy_tab = c.copy(oryginal_tab)
deep_tab = c.deepcopy(oryginal_tab)

print('old', oryginal_tab)
print('copy', copy_tab)
print('deep copy', deep_tab)

oryginal_tab[1][0] = '🦄'

print('old modified', oryginal_tab)
print('copy is also modified', copy_tab)
print('but not deep copy', deep_tab)
