#dfs и поиск циклов в неорграфе
# + покраска рёбер дерева обхода графа
# на прямые и обратные
def dfs(v, parent):
    global cycle
    used[v] = 1
    for x in g[v]:
        to = x[0]
        if not used[to]:
            x[1] = 1 #прямое ребро
            dfs(to, v)
        elif to != parent:
            cycle = True
            x[1] = 2 #обратное ребро
            

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append([b, 0])
    g[b].append([a, 0])

used = [0] * n
cycle = False
for i in range(n):
    if not used[i]:
        dfs(i, -1)
#например, выведем рёбра, которые нужно оставить
#чтобы получить граф без циклов (дерево, если
#комп. связности - одна)
for i in range(n):
    for x in g[i]:
        if x[1] == 1:
            print(i + 1, x[0] + 1)
