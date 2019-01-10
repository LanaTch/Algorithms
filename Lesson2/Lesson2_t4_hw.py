# 4. Найти сумму n элементов следующего ряда чисел:
#  1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def sum_progres_rec(FIRST, D, n):
    return FIRST if n == 1 else FIRST * D ** (n - 1) + sum_progres_rec(FIRST, D, n - 1)


DELTA = -0.5
FIRST = 1

n = int(input('сумму скольки элементов прогресии 1, -0.5, 0.25, -0.125, ... посчитать? '))
summa = sum_progres_rec(FIRST, DELTA, n)
print(f'сумма {n} элементов прогрессии = {summa}')
