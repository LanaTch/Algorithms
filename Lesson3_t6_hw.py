# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min = max = array[0]
pos_min = pos_max = 0
for i in range(SIZE):
    if array[i] < min:
        min = array[i]
        pos_min = i
    if array[i] > max:
        max = array[i]
        pos_max = i

if abs(pos_min - pos_max) == 1:
    print('между максимумом и минимумом нет элементов')
else:
    if pos_max > pos_min:
        start = pos_min
        stop = pos_max
    else:
        start = pos_max
        stop = pos_min

    summa = 0
    for i in range(stop - start - 1):
        summa += array[start + 1 + i]
    print(f'сумма элементов между максимумом и минимумом = {summa}')
