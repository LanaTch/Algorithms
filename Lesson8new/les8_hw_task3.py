# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
#
#
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
import random

def generation_graph(n):
    g = []
    for i in range(n):
        p = [j for j in range(i)] + [_ for _ in range(i + 1, n)]
        li = sorted(random.sample(p, random.randint(1, n - 1)))
        g.append(set(li))
    return g


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


n = int(input('Сколько вершин в графе: '))
start = int(input('От какой вершины идти: '))

g = generation_graph(n)
print(g)
dfs(g, start)