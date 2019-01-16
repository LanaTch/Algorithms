# Определить, какое число в массиве встречается чаще всего.

import random
import  collections
import cProfile

# цикл со словарем
# вариант 1
def max_frequency_number_dict(size, max_abs_item=5):
    min_item = - max_abs_item
    array = [random.randint(min_item, max_abs_item) for _ in range(size)]
    # print(array)

    dict_number_count = {}
    for i in range(size):
        dict_number_count[array[i]] = dict_number_count[array[i]] + 1 if array[i] in dict_number_count else 1

    count_max = 0
    for number in dict_number_count:
        if dict_number_count[number] > count_max:
            count_max = dict_number_count[number]
            num_freq_max = number
    return f'число {num_freq_max} встречается в массиве чаще всего - {count_max} раз' if count_max != 1 else 'все элементы массива уникальны'
# python -m timeit -n 100 -s "import Lesson4_t1" "Lesson4_t1.max_frequency_number_dict(10000, 25)
# 100 loops, best of 5: 11.6 usec per loop - size = 10
# 100 loops, best of 5: 103 usec per loop  - size = 100
# 100 loops, best of 5: 254 usec per loop  - size = 250
# 100 loops, best of 5: 518 usec per loop  - size = 500
# 100 loops, best of 5: 1.02 msec per loop - size = 1000
# 100 loops, best of 5: 10.4 msec per loop - size = 10000
#=========================================================
# cProfile.run('max_frequency_number_dict(1000)')
# 5443 function calls in 0.002 seconds
# calls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 Lesson4_t1.py:11(<listcomp>)
#         1    0.000    0.000    0.002    0.002 Lesson4_t1.py:9(max_frequency_number_dict)

# цикл без словаря
# вариант 2
def max_frequency_number_loop(size, max_abs_item=5):
    min_item = - max_abs_item
    array = [random.randint(min_item, max_abs_item) for _ in range(size)]
    # print(array)
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

    return f'Число {num} встречется {frequency} раз(а)' if frequency > 1 else 'Все элементы уникальны'
# python -m timeit -n 100 -s "import Lesson4_t1" "Lesson4_t1.max_frequency_number_loop(10, 5)
# 100 loops, best of 5: 14.7 usec per loop   - size = 10
# 100 loops, best of 5: 361 usec per loop    - size = 100
# 100 loops, best of 5: 1.81 msec per loop   - size = 250
# 100 loops, best of 5: 7.62 msec per loop   - size = 500
# 100 loops, best of 5: 29.6 msec per loop   - size = 1000
# 100 loops, best of 5: 2.89 sec per loop    - size = 10000
#=========================================================
# cProfile.run('max_frequency_number_loop(1000)')
# 6462 function calls in 0.030 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.030    0.030 <string>:1(<module>)
#         1    0.028    0.028    0.030    0.030 Lesson4_t1.py:38(max_frequency_number_loop)

# встроенные функции
# вариант 3
def max_frequency_number_python_func(size, max_abs_item=5):
    min_item = - max_abs_item
    array = [random.randint(min_item, max_abs_item) for _ in range(size)]
    # print(array)
    num, frequency = collections.Counter(array).most_common(1)[0]
    return f'Число {num} встречется {frequency} раз(а)' if frequency > 1 else 'Все элементы уникальны'

# python -m timeit -n 100 -s "import Lesson4_t1" "Lesson4_t1.max_frequency_number_python_func(10)
# 100 loops, best of 5: 13.7 usec per loop  - size = 10
# 100 loops, best of 5: 97.1 usec per loop  - size = 100
# 100 loops, best of 5: 238 usec per loop   - size = 250
# 100 loops, best of 5: 468 usec per loop   - size = 500
# 100 loops, best of 5: 951 usec per loop  - size = 1000
# 100 loops, best of 5: 9.89 msec per loop - size = 10000
#=========================================================
# cProfile.run('max_frequency_number_python_func(1000)')
#     5533 function calls(5525 primitive calls) in 0.002 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.002    0.002 Lesson4_t1.py:72(max_frequency_number_python_func)
#         1    0.000    0.000    0.001    0.001 Lesson4_t1.py:74(<listcomp>)
#         1    0.000    0.000    0.000    0.000 __init__.py:548(__init__)
#         1    0.000    0.000    0.000    0.000 __init__.py:573(most_common)
#         1    0.000    0.000    0.000    0.000 __init__.py:617(update)
#         5    0.000    0.000    0.000    0.000 _collections_abc.py:392(__subclasshook__)
#         1    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
#       5/1    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
#         1    0.000    0.000    0.000    0.000 heapq.py:524(nlargest)
#      1000    0.000    0.000    0.001    0.000 random.py:174(randrange)
#      1000    0.000    0.000    0.001    0.000 random.py:218(randint)
#      1000    0.000    0.000    0.001    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
#       5/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
#         1    0.000    0.000    0.000    0.000 {built-in method _collections._count_elements}
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1500    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

# выводы:
# как видно из замеров с помощью timeit, реализация с помощью словаря и встроенными функциями
# имеют линейную зависимость от размер массива.
# А реализация с помощью вложенных циклов выдает экспоненциальну зависимость от размера массива.
# Значит первоначальная реализация очень даже неплохая :)



