# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random


def merge_sort(array):
    if len(array) <= 1:
        return

    middle = len(array) // 2
    left_list = array[:middle]
    right_list = array[middle:]
    merge_sort(left_list)
    merge_sort(right_list)
    i = k = n = 0
    while i < len(left_list) and k < len(right_list):
        if left_list[i] <= right_list[k]:
            array[n] = left_list[i]
            i += 1
        else:
            array[n] = right_list[k]
            k += 1
        n += 1
    # переливаем остаток длинной части. выполнится только 1 из циклов:
    while i < len(left_list):
        array[n] = left_list[i]
        n += 1
        i += 1
    while k < len(right_list):
        array[n] = right_list[k]
        n += 1
        k += 1


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49.9 # если поставить 50, то из-за округления может быть включено
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'исходный {array}')
merge_sort(array)
print(f'сортированный {array}')
