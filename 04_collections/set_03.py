tuple_1 = ("a", "b", "c", "d", "e", "f", 1, 2, 3)
tuple_2 = tuple(range(10))

effect = tuple_1[::2] + tuple_2[1::2]
effect = list(effect)
print(effect)

result_set = set(effect)
print(result_set)
