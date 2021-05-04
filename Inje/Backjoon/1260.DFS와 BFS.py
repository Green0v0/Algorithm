import sys
from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for nodes in graph:
    nodes = nodes.sort()

vstd_dfs = [False] * (n+1)
stck = [v]
dfs_ans = []
while stck:
    nxt_node = stck.pop()
    if not vstd_dfs[nxt_node]:
        vstd_dfs[nxt_node] = True
        stck.extend(sorted(graph[nxt_node], key=lambda x: -x))
        dfs_ans.append(nxt_node)

for i in dfs_ans:
    print(i, end=' ')


vstd_bfs = [False] * (n+1)
que = deque([v])
vstd_bfs[v] = True
bfs_ans = [v]
while que:
    now_node = que.popleft()
    for nxt_node in graph[now_node]:
        if not vstd_bfs[nxt_node]:
            vstd_bfs[nxt_node] = True
            que.append(nxt_node)
            bfs_ans.append(nxt_node)

print()
for i in bfs_ans:
    print(i, end=' ')


# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1

# 1000 1 1000
# 999 1000