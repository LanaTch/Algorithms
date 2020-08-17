# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

def count_unique_substr(s):
    sub_str_hash = set()

    len_sub = 1
    while len_sub < len(s):
        for i in range(len(s) - len_sub + 1):
            sub_hash = hash(s[i:i + len_sub])
            if sub_hash not in sub_str_hash:
                sub_str_hash.add(sub_hash)
                print(s[i:i + len_sub])
        len_sub += 1
    return len(sub_str_hash)


s = 'test'

print(count_unique_substr(s))
