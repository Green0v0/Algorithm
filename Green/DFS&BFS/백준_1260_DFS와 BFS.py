# DFS와 BFS 탐색한 결과를 출력
# 정점이 여러 개인 경우 작은 것 먼저 방문
# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
from collections import deque
N, M, V = map(int, input().split())
data = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    # 양방향이니까..
    data[x].append(y)
    data[y].append(x)

for j in range(N+1):
    data[j] = sorted(data[j])

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

# dfs
# def dfs(visited_dfs,V,data):
#     stack = [V]
#     visited_dfs[V] = True
#     while stack:
#         now = stack.pop()
#         print(now, end=' ')
#         for i in data[now]:
#             if not visited_dfs[i]:
#                 stack.append(i)
#                 visited_dfs[i] = True

def dfs(visited_dfs, V, data):
    visited_dfs[V] = True
    print(V, end=' ')
    for i in data[V]:
        if not visited_dfs[i]:
            dfs(visited_dfs, i, data)

def bfs(visited_bfs, V, data):
    q = deque([V])
    visited_bfs[V] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in data[now]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True

dfs(visited_dfs, V, data)
print()
bfs(visited_bfs, V, data)