def dfs(v, color):
    global flag
    used[v] = color
    for to in g[v]:
        if not used[to]:
            dfs(to, 3 - color)
        elif used[to] == color:
            flag = False 
            

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

flag = True
used = [0] * n
for i in range(n):
    if not used[i]:
        dfs(i, 1)
if not flag:
    print("No solution")
else:
    first = []
    second = []
    for i in range(n):
        if used[i] == 1:
            first.append(i + 1)
        else:
            second.append(i + 1)
    print(*first)
    print(*second)
