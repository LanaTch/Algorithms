# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
n = int(input('Введите номер буквы в алфавите: '))

s = chr(ord('a') + n - 1)

print(f'это буква {s}')