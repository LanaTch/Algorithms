# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

count_max = 0
count = 0
number_count_max = 0
array_number = []
for i in range(SIZE):
    current_number = array[i]
    if not (current_number in array_number):
        for j in range(SIZE):
            if array[j] == current_number:
                count += 1
        if count > count_max:
            count_max = count
            number_count_max = current_number
        array_number.append(current_number)
    count = 0

print(f'число {number_count_max} встречается в массиве чаще всего - {count_max} раз')
