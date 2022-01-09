#dfs с разметкой компонент связности
def dfs(v, color):
    used[v] = color
    for to in g[v]:
        if not used[to]:
            dfs(to, color)


n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

used = [0] * n
color = 0
for i in range(n):
    if not used[i]:
        color += 1
        dfs(i, color)

print(color) #кол-во компонент связности
components = [[] for i in range(color)]
for i in range(n): #каждую вершину помещаем в массив своей компоненты
    components[used[i] - 1].append(i + 1)
    
for comp in components:
    print(*comp)
    




