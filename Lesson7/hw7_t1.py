# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
# и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random


def clever_bubble_sotr(array):
    n = 1
    flag = True  # если не было перестановок на данной итерации, то уже отсортирован
    last = len(array) - 1  # будем уменьшать верхнюю границу массива, т к конец будет отсортирован
    while n < len(array) and flag:
        flag = False
        for i in range(last):
            if array[i] < array[i + 1]:
                flag = True # есть перестановка, значит еще не отсортированн
                array[i], array[i + 1] = array[i + 1], array[i]
                last = i  # запомнить индекс очередного отсортированного
        n += 1


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'исходный массив {array}')
clever_bubble_sotr(array)
print(f'отсотрированный массив {array}')

