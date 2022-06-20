# graph = {
#     "dom" : ["bar", "szkoła", "kościół"],
#     "szkoła" : ["szpital", "dom"],
#     "kościół" : ["dom", "bar", "kino"],
#     "bar" : ["kościół", "szpital", "dom"],
#     "szpital" : ["szkoła", "bar", "teatr", "kino"],
#     "kino" : ["kościół", "szpital", "teatr"],
#     "teatr" : ["szpital", "kino"]
# }
#
# for i in graph:
#     for j in graph[i]:
#         print(str(i)+" ----> " + str(j))
#

buildings = {
    0: 'house',
    1: 'school',
    2: 'church',
    3: 'bar',
    4: 'hospital',
    5: 'cinema',
    6: 'theater'
}

matrix = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 1]
]

for id_row, row in enumerate(matrix):
    for id_col, col in enumerate(row):
        if col == 1:
            print(buildings[id_row], '---->', buildings[id_col])
