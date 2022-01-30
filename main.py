"""Домашнее задание для курса "Основы Python". Переменные, условия и циклы"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt

X = [0, 2, 5, 6, 8] # Координаты Х
Y = [2, 5, 2, 6, 3] # Координаты Y
n = len(X)

Road = []
RW = []
RIB = []
s = []

for ib in np.arange(0, n, 1):
    M = np.zeros([n, n])
    for i in np.arange(0, n, 1):
        for j in np.arange(0, n, 1):

            if i != j:
                M[i, j] = sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
            else:
                M[i, j] = float('inf')
    way = [ib]
    for i in np.arange(1, n, 1):
        s = []
        for j in np.arange(0, n, 1):
            s.append(M[way[i - 1], j])
        way.append(s.index(min(s)))
        for j in np.arange(0, i, 1):
            M[way[i], way[j]] = float('inf')
            M[way[i], way[j]] = float('inf')
    S = sum([sqrt((X[way[i]] - X[way[i + 1]]) ** 2 + (Y[way[i]] - Y[way[i + 1]]) ** 2) for i in
             np.arange(0, n - 1, 1)]) + sqrt((X[way[n - 1]] - X[way[0]]) ** 2 + (Y[way[n - 1]] - Y[way[0]]) ** 2)
    Road.append(S)
    RW.append(way)
    RIB.append(ib)
S = min(Road)
way = RW[Road.index(min(Road))]
ib = RIB[Road.index(min(Road))]
X1 = [X[way[i]] for i in np.arange(0, n, 1)]
Y1 = [Y[way[i]] for i in np.arange(0, n, 1)]
#
plt.title('Общий путь-%s.-%i-%i.\n Координаты X,Y заданы' % (round(S, 3), ib, n), size=14)
plt.plot(X1, Y1, color='r', linestyle=' ', marker='o')
plt.plot(X1, Y1, color='b', linewidth=1)
X2 = [X[way[n - 1]], X[way[0]]]
Y2 = [Y[way[n - 1]], Y[way[0]]]
#
plt.plot(X2, Y2, color='g', linewidth=2, linestyle='-', label='Путь от  последней точки \n к первой')
plt.legend(loc='best')
plt.grid(True)
plt.show()
