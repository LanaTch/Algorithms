# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

import math
import cProfile

def evaluation_n(i):
    n = i
    if n > 1:
        n2 = i ** 2
        while n2 - n > 1:
            n_next = int((n + n2) / 2)
            if (i - int(n_next / math.log(n_next))) > 0:
                n = n_next
            else:
                n2 = n_next
    return n
# cProfile.run('evaluation_n(10000)')
# 33 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson4_t2.py:8(evaluation_n)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        29    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ========================
# python -m timeit -n 100 -s "import Lesson4_t2" "Lesson4_t2.evaluation_n(10000)
# ------
# 100 loops, best of 5: 3.49 usec per loop  - 10
# 100 loops, best of 5: 5.51 usec per loop  - 50
# 100 loops, best of 5: 6.96 usec per loop  - 100
# 100 loops, best of 5: 8.06 usec per loop  - 200
# 100 loops, best of 5: 9.32 usec per loop  - 500
# 100 loops, best of 5: 10.4 usec per loop  - 1000
# 100 loops, best of 5: 12.6 usec per loop  - 5000
# 100 loops, best of 5: 13.6 usec per loop  - 10000

def counting_prime_with_sieve_er(i_num):
    n = evaluation_n(i_num)
    a = [0] * n
    for i in range(n):
        a[i] = i

    a[1] = 0
    b = []
    m = 2
    while m < n:
        if a[m] != 0:
            # b.append(a[m])
            # if len(b) == i_num:
            #     break
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    for i in a:
        if a[i] != 0:
            b.append(a[i])

    return f'с решетом: {i_num}-е простое число = {b[i_num - 1]}'
# python -m timeit -n 100 -s "import Lesson4_t2" "Lesson4_t2.counting_prime_with_sieve_er(10)
# -------------
# 100 loops, best of 5: 11.3 usec per loop  - 10
# 100 loops, best of 5: 12.7 usec per loop  : with loop for b.append
# 100 loops, best of 5: 64.6 usec per loop  - 50
# 100 loops, best of 5: 77 usec per loop    : with loop for b.append
# 100 loops, best of 5: 161 usec per loop   - 100
# 100 loops, best of 5: 187 usec per loop   : with loop for b.append
# 100 loops, best of 5: 380 usec per loop   - 200
# 100 loops, best of 5: 425 usec per loop   : with loop for b.append
# 100 loops, best of 5: 1.19 msec per loop  - 500
# 100 loops, best of 5: 1.3 msec per loop   : with loop for b.append
# 100 loops, best of 5: 2.86 msec per loop  - 1000
# 100 loops, best of 5: 2.85 msec per loop  : with loop for b.append
# 100 loops, best of 5: 17.5 msec per loop  - 5000
# 100 loops, best of 5: 18.6 msec per loop  : with loop for b.append
# 100 loops, best of 5: 37.8 msec per loop  - 10000
# 100 loops, best of 5: 41 msec per loop    : with loop for b.append
# 100 loops, best of 5: 90.7 msec per loop  - 20000 with loop for b.append
# 100 loops, best of 5: 145 msec per loop   - 30000 with loop for b.append
# ================================================
# cProfile.run('counting_prime_with_sieve_er(10000)')
# 20034 function calls in 0.038 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.038    0.038 <string>:1(<module>)
#         1    0.036    0.036    0.037    0.037 Lesson4_t2.py:26(counting_prime_with_sieve_er)
#         1    0.000    0.000    0.000    0.000 Lesson4_t2.py:8(evaluation_n)
#         1    0.000    0.000    0.038    0.038 {built-in method builtins.exec}
#     10000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        29    0.000    0.000    0.000    0.000 {built-in method math.log}
#     10000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ===========================
# 11049 function calls in 0.045 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.045    0.045 <string>:1(<module>)
#         1    0.043    0.043    0.043    0.043 Lesson4_t2.py:26(counting_prime_with_sieve_er)
#         1    0.000    0.000    0.000    0.000 Lesson4_t2.py:8(evaluation_n)
#         1    0.000    0.000    0.045    0.045 {built-in method builtins.exec}
#        29    0.000    0.000    0.000    0.000 {built-in method math.log}
#     11015    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def counting_prime_not_sieve(i_prime):
    a_prime = [2]
    i = 3
    while len(a_prime) < i_prime:
        if (i > 10) and (i % 10 == 5):
            i += 2
            continue
        for j in a_prime:
            if j * j - 1 > i:
                a_prime.append(i)
                break
            if (i % j == 0):
                break
        else:
            a_prime.append(i)
        i += 2
    return f'без решета: {i_prime}-е простое число = {a_prime[i_prime-1]}'
# python -m timeit -n 100 -s "import Lesson4_t2" "Lesson4_t2.counting_prime_not_sieve(10)
#----------
# 100 loops, best of 5: 5.14 usec per loop  - 10
# 100 loops, best of 5: 48.2 usec per loop  - 50
# 100 loops, best of 5: 134 usec per loop   - 100
# 100 loops, best of 5: 346 usec per loop   - 200
# 100 loops, best of 5: 1.28 msec per loop  - 500
# 100 loops, best of 5: 3.31 msec per loop  - 1000
# 100 loops, best of 5: 32 msec per loop    - 5000
# 100 loops, best of 5: 91.8 msec per loop  - 10000
# 100 loops, best of 5: 212 msec per loop   - 20000
# 100 loops, best of 5: 366 msec per loop   - 30000
# ================================================
# cProfile.run('counting_prime_not_sieve(1000)')
# --------
# 4963 function calls in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.003    0.003    0.004    0.004 Lesson4_t2.py:115(counting_prime_not_sieve)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#      3960    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# выводы:
# Наглядно можно посмотреть на графиках graf_1.png (10 <= i <= 500) и graf_2.png (1000 <= i <= 30000)
# для небольших значений вычисление с решетом не дает  значимых преимуществ в скорости.
# Преимущество становится явно заметно при значениях >= 1000. Обе функции можно аппроксимировать прямой
# на этом участке, но функция с решетом возрастает медленнее, чем функция без решета.
#
# Для оценки размера решета написана функция evaluation_n. это нужно для минимизации размера решета,
# а соответственно и времени вычисления. Алгоритм оценки работает быстро и почит константа, поэтому
# существенно не замедляет функцию с решетом.