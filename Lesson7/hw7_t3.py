# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random


def quickselect_m(m, array):
    pivot = random.choice(array)  # выбор случайного опорного элемента из массива

    left = [elem for elem in array if elem < pivot]  # массив из элементов меньше опорного
    if len(left) > m:  # значит медиана в левой части
        return quickselect_m(m, left)

    count_pivot = array.count(pivot)  # количество повторов опорного элемента в массиве
    if count_pivot + len(left) > m:  # медиана = опорный - удачный выбор :)
        return pivot

    # условия выше не выполнились, значит медиана в правой части:
    right = [elem for elem in array if elem > pivot]  # массив из элементов больше опорного
    return quickselect_m(m - len(left) - count_pivot, right)


m = 4
size = 2 * m + 1
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
print(array)
# m_test = sorted(array)[m]
# print(m_test)
median = quickselect_m(m, array)
print(f'median = {median}')
