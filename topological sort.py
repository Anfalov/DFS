def dfs(v):
    used[v] = 1
    for to in g[v]:
        if not used[to]:
            dfs(to)
    res.append(v)

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

used = [0] * n
res = []
for i in range(n):
    if not used[i]:
        dfs(i)
res = res[::-1]
print(res)
