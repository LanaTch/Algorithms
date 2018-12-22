# 9. Среди натуральных чисел, которые были
# введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def calc_sum_digits(n: int):
    summa = 0
    while n > 0:
        summa += n % 10
        n //= 10
    return summa


max_sum_digits = 0
max_sum_n = 0

while True:
    n = int(input('Введите натуральное число или 0 для выхода: '))
    if n == 0:
        print('стоп')
        break

    sum_digits = calc_sum_digits(n)

    if sum_digits > max_sum_digits:
        max_sum_digits = sum_digits
        max_sum_n = n

if max_sum_n != 0:
    print(f'число {max_sum_n} с максимальной суммой цифр = {max_sum_digits}')
