# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
# число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
hex_dict_reverse = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def sum_hex_func(a, b):
    len_a, len_b = len(a), len(b)
    (n1, n2) = (a, b) if len_a > len_b else (b, a)
    n1.reverse()
    n2.reverse()

    for _ in range(len(n1) - len(n2)):
        n2.append('0')

    sum_hex = deque()
    transfer = 0
    for i in range(len(n1)):
        spam = hex_dict[n1[i]] + hex_dict[n2[i]] + transfer
        (digit, transfer) = (spam, 0) if spam <= 15 else (spam - 16, 1)
        sum_hex.appendleft(hex_dict_reverse[digit])
    if transfer != 0:
        sum_hex.appendleft(hex_dict_reverse[transfer])
    return sum_hex


def mult_hex_func(a, b):
    len_a, len_b = len(a), len(b)
    (n1, n2) = (a, b) if len_a > len_b else (b, a)
    n1.reverse()
    n2.reverse()
    mult_hex_i = []
    for j in range(len(n2)):
        digit = hex_dict[n2[j]]
        transfer = 0
        mult_hex_i.append(deque())
        for i in range(len(n1)):
            spam = hex_dict[n1[i]] * digit + transfer
            (transfer, spam) = divmod(spam, 16)
            mult_hex_i[j].appendleft(hex_dict_reverse[spam])
        if transfer != 0:
            mult_hex_i[j].appendleft(hex_dict_reverse[transfer])

    for j in range(1, len(mult_hex_i)):
        for i in range(1, j + 1):
            mult_hex_i[j].extend('0')

    mult_hex_res = mult_hex_i[0].copy()
    for i in range(1, len(mult_hex_i)):
        mult_hex_res = sum_hex_func(mult_hex_res.copy(), mult_hex_i[i].copy())
    return mult_hex_res

numbers_hex = deque()
i = 1
while i < 3:
    a = deque(*(input(f'введите {i}-е 16-ричное число: ')).upper().split())
    for digit in a:
        if digit not in '0123456789ABCDEF':
            print('неправильное 16-ричное число. допустимы только цифры и буквы "abcdef"')
            break
    else:
        numbers_hex.append(a)
        i += 1

print(f'сумма = {sum_hex_func(numbers_hex[0].copy(), numbers_hex[1].copy())}')
print(f'произведение = {mult_hex_func(numbers_hex[0].copy(), numbers_hex[1].copy())}')
