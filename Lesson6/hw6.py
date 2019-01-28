# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной
# и той же задачи. Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.
#
# Задача из урока 3:
# Определить, какое число в массиве встречается чаще всего.

import sys
import random
from collections import Counter

def deep_get_size(obj, seen=None):
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0

    seen.add(obj_id)
    if isinstance(obj, dict):
      size += sum([deep_get_size(v, seen) for v in obj.values()])
      size += sum([deep_get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
      size += deep_get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
      size += sum([deep_get_size(i, seen) for i in obj])
    return size

def decor_sizeof(fn):
    def into_fn(arg1, arg2=5):
        sum_size = 0
        local_var_fn = fn(arg1, arg2)
        for var in local_var_fn:
            spam = local_var_fn[var]
            eggs = deep_get_size(spam)
            sum_size += eggs
        print(f'функция {fn.__name__}\nn = {arg1} max_item = {arg2} memory_vars = {sum_size} байт')
    return into_fn

# цикл со словарем
# вариант 1
# v1
@decor_sizeof
def max_frequency_number_dict(size, max_abs_item=5):
    min_item = - max_abs_item
    array = [random.randint(min_item, max_abs_item) for _ in range(size)]

    dict_number_count = {}
    for i in range(size):
        dict_number_count[array[i]] = dict_number_count[array[i]] + 1 if array[i] in dict_number_count else 1

    count_max = 0
    for number in dict_number_count:
        if dict_number_count[number] > count_max:
            count_max = dict_number_count[number]
            num_freq_max = number
    return locals()
# n = 10    памяти = 1092
# n = 50    памяти = 2064
# n = 100   памяти = 2560                                           11160
# n = 300   памяти = 4184                                           26716
# n = 600   памяти = 7200                                           48748
# n = 1000  памяти = 10752  max_item = 5;   max_item = 300 памяти = 62600
# n = 1500  памяти = 14684                                          78288
# n = 1700  памяти = 16408                                          82928
# n = 2000  памяти = 18292                                          91192
# n = 5000  памяти = 44800
# n = 10000 памяти = 89384
# =========================


# цикл без словаря
# вариант 2
# v2
@decor_sizeof
def max_frequency_number_loop(size, max_abs_item=5):
    min_item = - max_abs_item
    array = [random.randint(min_item, max_abs_item) for _ in range(size)]
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    return locals()
# n = 10     памяти = 612
# n = 50     памяти = 1056
# n = 100    памяти = 1440                                            3852
# n = 300    памяти = 3064                                            10544
# n = 600    памяти = 6024                                            19632
# n = 1000   памяти = 9552    max_item = 5;   max_item = 300 памяти = 30920
# n = 1500   памяти = 13536                                           43160
# n = 1700   памяти = 15208                                           49088
# n = 2000   памяти = 17088                                           55980
# n = 5000   памяти = 43568
# n = 10000  памяти = 88152
# =========================

# встроенные функции
# вариант 3
# v3
@decor_sizeof
def max_frequency_number_python_func(size, max_abs_item=5):
    min_item = - max_abs_item
    array = [random.randint(min_item, max_abs_item) for _ in range(size)]
    spam = Counter(array)
    eggs = spam.most_common
    num, frequency = eggs(1)[0]
    return locals()
# n = 10     памяти = 1220
# n = 50     памяти = 2272
# n = 100    памяти = 2824                                           11452
# n = 300    памяти = 4420                                           26224
# n = 600    памяти = 7520                                           49376
# n = 1000   памяти = 11020 max_item = 5;    max_item = 300 памяти = 62584
# n = 1500   памяти = 15032                                          77768
# n = 1700   памяти = 16644                                          83080
# n = 2000   памяти = 18556                                          92128
# n = 5000   памяти = 45064
# n = 10000  памяти = 89648
# =========================

if __name__ == '__main__':
    # для запуска из терминала можно задавать размер и максимальное значение как параметры
    # python hw6.py 100 5
    n = 100 if len(sys.argv) < 2 else int(sys.argv[1])
    max_item = 5 if len(sys.argv) < 3 else int(sys.argv[2])
    max_frequency_number_dict(n, max_item)
    print('====================')
    max_frequency_number_loop(n, max_item)
    print('====================')
    max_frequency_number_python_func(n, max_item)

#
# затраты памяти в кБ в зависимости от размера массива n,
# разброс значений от -300 до 300
#    |  100	  |  300	|  600	  |  1000	|  1500	  |  1700	|   2000  |   5000
# ---------------------------------------------------------------------------------
# v1 | 10,90  |  26,09	|  47,61  |  61,13	|  76,45  |  80,98	|  89,05  |  162,00
# v2 |  3,76  |  10,30	|  19,17  |  30,20	|  42,15  |  47,94	|  54,67  |  126,80
# v3 | 11,18  |  25,61	|  48,22  |  61,12	|  75,95  |  81,13	|  89,97  |  162,34

#
# затраты памяти в кБ в зависимости от разброса допустимых значений в массиве
# размер массива n = 2000
#      |	10	  |   50    |	100	  |  300	 |   700   |   1000
# --------------------------------------------------------------------
# v1   |  31,95	  |  50,59  |	59,20 |	 88,37   | 131,86	|  139,06
# v2   |  30,77	  |  43,48	|   45,07 |	 55,00   |  66,04	|   68,67
# v3   |  31,63	  |  50,05	|   59,54 |	 86,82	 | 131,55	|  139,31


# Python 3.7.0, OS 64 bit Win10

# выводы:
#
# По замерам можно сказать, что чем больше разброс допустимых значений в массиве,
# тем больше памяти необходимо для функций v1 и v3. Это ожидаемо, так как эти функции
# используют словари для хранения частот. Чем больше разных значений в массиве,
# тем больше будет этот словарь. В этом смысле вариант с циклом v2 исползует
# в 2 раза меньше памяти при большом разбросе значений (> 500).
#
# Зависимость используемой памяти от размера массива при постоянном разбросе значений
# у всех функций примерно одинакова. Варианты v1 и v3 со словарями используют
# памяти под переменные больше примерно в 2 раза при n < 2000,
# при дальнейшем увеличении n разница уже почти не заметна -- около 40 кБ.
#
# В процессе решения выяснилась особенность:
# данный вариант подсчета переменных не подходит для программ, написанных кратко.
# например, при записи
# num, frequency = Counter(array).most_common(1)[0]
# в подсчете не будут учтены затраты памяти на Counter(array) и most_common

