# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

SIZE_COL = 4
SIZE_ROW = 5
matrix = []

for i in range(SIZE_ROW):
    summa = 0
    row = []
    for j in range(SIZE_COL - 1):
        row.append(int(input(f'введите элемент матрицы ({i},{j}):')))
        summa += row[j]
    row.append(summa)
    matrix.append(row)

for i in range(SIZE_ROW):
    for j in range(SIZE_COL):
        print(matrix[i][j], end='\t')
    print()
