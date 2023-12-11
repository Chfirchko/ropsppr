import sympy


def det(lst):
    det1 = lst[0][0] * lst[1][1] * lst[2][2]
    det2 = lst[0][1] * lst[1][2] * lst[2][0]
    det3 = lst[0][2] * lst[1][0] * lst[2][1]
    det4 = lst[0][2] * lst[1][1] * lst[2][0]
    det5 = lst[0][0] * lst[1][2] * lst[2][1]
    det6 = lst[0][1] * lst[1][0] * lst[2][2]
    return det1 + det2 + det3 - det4 - det5 - det6


def change_matrix(n, lst):
    for i in range(len(lst)):
        lst[i][n] = 1
    return lst


# lst = [[0.7, 0.2, 0.1],
#        [0.8, 0.1, 0.1],
#        [0.8, 0.05, 0.15]]

lst = [[0.25, 0.5, 0.25],
       [0, 0.5, 0.5],
       [0.33, 0.33, 0.34]]

for z in range(len(lst)):
    for z1 in range(len(lst)):
        if z != z1:
            lst[z1][z] += 1

lst1 = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 9]]

for z in range(len(lst)):
    for z1 in range(len(lst)):
        lst1[z1][z] = lst[z][z1]

lst_of_dets = [1, 2, 3, 4]

for i in range(len(lst_of_dets)):
    lst2 = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 9]]
    for j in range(len(lst1)):
        for z in range(len(lst1)):
            lst2[j][z] = lst1[j][z]
    if i != 0:
        lst_of_dets[i] = det(change_matrix(i - 1, lst2))
    else:
        lst_of_dets[i] = det(lst2)

P3 = lst_of_dets[3] / lst_of_dets[0]


print(lst_of_dets)

print(P3)
print( 1 - P3)

