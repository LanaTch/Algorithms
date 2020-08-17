# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
#
# Примечание. Решите задачу при помощи построения графа.

# для ршения задачи сгенерируем матрицу смежности для такого графа
# количество рукопожатий - это сумма единиц матрицы смежности деленная на 2
N = 5
g = [[0 for j in range(N)] for i in range(N)]
s = 0
for i in range(N):
    for j in range(N):
        if i == j:
            g[i][j] = 0
        else:
            g[i][j] = 1
            s += 1

g = [[0 if i == j else 1 for j in range(N)] for i in range(N)]
print(g)
print(f'число рукопожатий: {int(s/2)}')
