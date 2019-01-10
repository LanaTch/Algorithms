# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_in_array = min_early = array[0]
for i in range(SIZE):
    if array[i] < min_in_array:
        min_early = min_in_array
        min_in_array = array[i]
    elif array[i] < min_early:
        min_early = array[i]

print(f'два минимальных элемента массива: {min_in_array}, {min_early}')
