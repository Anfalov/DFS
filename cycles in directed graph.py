def dfs(v):
    global cycle
    used[v] = 1
    for to in g[v]:
        if not used[to]:
            dfs(to)
        elif used[to] == 1:
            cycle = True
    used[v] = 2

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)

cycle = False
used = [0] * n
for i in range(n):
    if not used[i]:
        dfs(i, 1)

if cycle:
    print("Есть цикл")
else:
    print("Нет цикла")
