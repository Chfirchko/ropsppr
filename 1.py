import numpy as np

x = 100


def soyJakkar(table):
    a = 0
    for i in table:
        if i[0] == i[1]:
            a += 1
    print('сходство Жаккара между объектами:', a / len(table))
    a = 0
    b = 0
    for i in table:
        if i[0] == i[1] == 1:
            a += 1
        if i[0] == 1 or i[1] == 1:
            b += 1
    print('сходство Жаккара для покупателей:', a / b)
    print('сходство Жаккара для людей, не купивших товар:', 1 - a / b)


def L(table):
    sum1 = 0
    for j in range(len(table['A'])):
        sum = 0
        for z, i in enumerate(table):
            if z != 0:
                table[i][j] = int('-' + str(table[i][j]))
            sum += table[i][j]
        sum1 += abs(sum)
    print('L1-норма =', sum1)
    sum1 = 0
    for j in range(len(table['A'])):
        sum = 0
        for z, i in enumerate(table):
            sum += table[i][j]
        sum1 += sum ** 2
    print('L2-норма =', np.sqrt((sum1)))


def Otiai(table):
    a = 0
    b = 0
    c = 0
    for i in table:
        a += i[0] * i[1]
    for i in table:
        b += i[0] ** 2
    for i in table:
        c += i[1] ** 2
    print('косинусное подобие =', a / (np.sqrt(b) * (np.sqrt(c))))


if __name__ == '__main__':
    table = [[1, 1],
             [1, 1],
             [1, 0],
             [0, 1],
             [0, 0],
             [0, 0]]
    soyJakkar(table)
    print()
    table = {'A': [6, 9],
             'B': [9, 4]}
    L(table)
    print()
    table = [[5, 3], [0, 0], [3, 2], [0, 0], [2, 1], [0, 1], [0, 0], [2, 1], [0, 0], [0, 1]]
    Otiai(table)
