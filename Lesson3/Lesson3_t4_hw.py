# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

dict_number_count = {}
for i in range(SIZE):
    dict_number_count[array[i]] = dict_number_count[array[i]] + 1 if array[i] in dict_number_count else 1

count_max = 0
for number in dict_number_count:
    if dict_number_count[number] > count_max:
        count_max = dict_number_count[number]
        number_count_max = number

print(f'число {number_count_max} встречается в массиве чаще всего - {count_max} раз')
