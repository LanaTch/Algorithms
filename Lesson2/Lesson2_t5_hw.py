# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа
# под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ"
# в каждой строке.
FIRST_CODE = 32
LAST_CODE = 127

count = 0

for code in range(FIRST_CODE, LAST_CODE + 1):
    char = chr(code)
    print(f'{code}-{char}', end='')
    print('\n', end='') if count == 9 else print('\t', end='')
    count = (count + 1) % 10
