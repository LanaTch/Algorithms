# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

count_digits = 0
number = int(input('введите целое положительное число: '))
n = number

while n != 0:
    count_digits += 1
    n //= 10
print(f'цифр в числе {count_digits}')

result_number = 0
for i in range(count_digits):
    result_number += number % 10 * 10 ** (count_digits - i - 1)
    number //= 10

print(f'обартное число: {result_number}')
