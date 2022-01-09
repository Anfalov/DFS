#простейшая реализация dfs
def dfs(v):
    used[v] = 1
    for to in g[v]:
        if not used[to]:
            dfs(to)


n, m = map(int, input().split()) #кол-во вершин и рёбер

# ~ #хранение графа в виде матрицы смежности (граф приходит ввиде списка рёбер)
# ~ matr = [[0] * n for i in range(n)]
# ~ for i in range(m):
    # ~ a, b = map(int, input().split())
    # ~ a -= 1
    # ~ b -= 1
    # ~ matr[a][b] = 1
    # ~ matr[b][a] = 1 #если граф неориентирован

#хранение графа в виде списка смежности
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a) #если граф неориентирован
    
#связен ли граф?    
used = [0] * n
dfs(0)
if sum(used) != n:
    print("Не свяен")
else:
    print("Связен")
    




