# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_COL = 4
SIZE_ROW = 5
MIN_ITEM = -10
MAX_ITEM = 20
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_COL)] for _ in range(SIZE_ROW)]
for i in range(SIZE_ROW):
    for j in range(SIZE_COL):
        print(matrix[i][j], end='\t')
    print()

for j in range(SIZE_COL):
    min_of_columns = matrix[0][j]
    for i in range(SIZE_ROW):
        if matrix[i][j] < min_of_columns:
            min_of_columns = matrix[i][j]
    if j == 0 or min_of_columns > max_of_min_columns:
        max_of_min_columns = min_of_columns

print(f'максимум среди минимумов столбцов: {max_of_min_columns}')
