# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
import collections as cs
from operator import itemgetter


class MyNode:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f'/value: {self.value}, left: {self.left}, right: {self.right}/'

    def walk(self, code, acc):
        if self.value is not None:  # это лист
            code[self.value] = acc or '0'
        else:  # это узел
            self.left.walk(code, acc + '0')
            self.right.walk(code, acc + '1')


def huffman_coding(s):
    h = []
    for ch, freq in cs.Counter(s).most_common():
        h.append((freq, MyNode(ch)))

    while len(h) > 1:  # пока есть больше 1 символа в строке
        freq1, left = h.pop()
        freq2, right = h.pop()
        # добавляем элемент в очередь
        h.append((freq1 + freq2, MyNode(None, left, right)))
        # сортируем очередь по частоте
        h.sort(key=itemgetter(0), reverse=True)

    code = {}

    if h:  # если очередь не пустая, то обходим от корня
        [(_freq, root)] = h
        root.walk(code, '')
    return code


def huffman_decoding(encoded, code):
    s_array = []
    enc_ch = ''
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                s_array.append(dec_ch)
                enc_ch = ''
                break
    print(s_array)
    return ''.join(s_array)


s = input('введите любую строку: ')
print(f'исходная строка:\n{s}\n')
code = huffman_coding(s)  # возвращает словарь кодировки символов

# декодирование
encoded = ''.join(code[ch] for ch in s)
print(f'закодированная:\n{encoded}\n')

print(f'декодированная строка:\n{huffman_decoding(encoded, code)}')
