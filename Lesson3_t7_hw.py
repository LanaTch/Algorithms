# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min = min_early = MAX_ITEM
for i in range(SIZE):
    if array[i] < min:
        min_early = min
        min = array[i]
    elif array[i] < min_early:
        min_early = array[i]

print(f'два минимальных элемента массива: {min}, {min_early}')
