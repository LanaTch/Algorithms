# 8. Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать,
# задаются вводом с клавиатуры.

def find_and_count_digit(number: int, digit: int):
    count = 0
    while number > 0:
        if number % 10 == digit:
            count += 1
        number //= 10
    return count


count_number = int(input('Сколько чисел будет? '))
digit = int(input('Какую цифру будем искать? '))

count_digit = 0

for _ in range(count_number):
    number = int(input('Введите целое положительное число:  '))
    count_digit += find_and_count_digit(number, digit)

print(f'цифра {digit} встечается {count_digit} раз')
