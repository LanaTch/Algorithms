# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_neg = 0
pos_max_neg = 0
for i in range(SIZE):
    if array[i] < 0 and array[i] > max_neg or max_neg >= 0:
        max_neg = array[i]
        pos_max_neg = i

print(f'максимальный отрицательный элемент = {max_neg}\nего позиция в массиве = {pos_max_neg}')
