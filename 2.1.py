import numpy as np

steps = 3
start = 1

P = [[0.33, 0.33, 0.33],
     [0, 0.5, 0.5],
     [0.5, 0.5, 0]]

one = ' 1'
zero = ' 0'

Q = ''
for i in range(len(P)):
    if i + 1 == start:
        Q = Q + one
    else:
        Q += zero
Quota = np.matrix(Q)

A = np.matrix('0.33 0.33 0.33; 0 0.5 0.5; 0.5 0.5 0')
B = A
C = B
for i in range(steps):
    C = A.dot(C)
    print('Матрица вероятностей шага №', i + 1, ': \n', C, '\n')
    # if i == 0:
    #     print('Пусть Q = ', Quota, '. Найдем распределение вероятностей состояний\n')
    D = Quota.dot(C)
    print('Q(', i + 1, ') = ', D, '\n', sep='')