# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
n1 = int(input('введите первое число n1 '))
n2 = int(input('введите первое число n2 '))
n3 = int(input('введите первое число n3 '))

ns = n3

if n1 < n2 < n3 or n3 < n2 < n1:
    ns = n2
elif n2 < n1 < n3 or n3 < n1 < n2:
    ns = n1

print('среднее число: ', ns)