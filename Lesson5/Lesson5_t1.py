# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
# квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.
from collections import namedtuple

Company = namedtuple('Company', ['name', 'q1', 'q2', 'q3', 'q4'])
enterprises = []
n = int(input('Сколько предприятий? '))

for _ in range(n):
    name_i = input('введите название предприятия: ')
    quarts_i = []
    for i in range(4):
        quarts_i.append(float(input(f'введите прибыль предприятия за {i+1} квартал: ')))
    enterprises.append(Company(name_i, *quarts_i))

average_all_company = 0
average_enterprises = []

for i in range(n):
    sum_en_i = sum(enterprises[i][1:5])
    average_enterprises.append(sum_en_i)
    print(f'годовая прибыль компании {enterprises[i].name}: {average_enterprises[i]}')

average_all_company = sum(average_enterprises) / n

print(f'средняя прибыль по всем компаниям: {average_all_company}')

index_lower_average = []
index_upper_average = []
for i in range(n):
    if average_enterprises[i] < average_all_company:
        index_lower_average.append(i)
    elif average_enterprises[i] != average_all_company:
        index_upper_average.append(i)

print('компании с годовой прибылью меньше средней:')
for index_l in index_lower_average:
    print(enterprises[index_l].name)

print('компании с годовой прибылью больше средней:')
for index_u in index_upper_average:
    print(enterprises[index_u].name)
