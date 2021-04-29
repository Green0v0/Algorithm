# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

# 3rd try:
from collections import deque
n, m, k, x = map(int, input().split())

graph = {key:[] for key in range(n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# vstd = [False] * (n+1)
dist = [-1] * (n+1)
dist[x] = 0
que = deque([x])
while que:
    now_node= que.popleft()
    for next_node in graph[now_node]:
        # dist[next_node] = min(dist[now_node]+1, dist[next_node])
        if dist[next_node] == -1:
            dist[next_node] = dist[now_node] + 1
        que.append(next_node)

chk = False
for i in range(len(dist)):
    if dist[i] == k:
        print(i)
        chk = True
if not chk:
    print(-1)




















# # 2nd try: 답지 참고
# from collections import deque


# def solution():
#     n, m, k, x = map(int, input("N,M,K,X: ").split())
#     graph = [[] for _ in range(n+1)]

#     for _ in range(m):
#         a, b = map(int, input().split())
#         graph[a].append(b)

#     dist = [-1] * (n+1)
#     dist[x] = 0

#     queue = deque([x])
#     while queue:
#         v = queue.popleft()
#         for next_node in graph[v]:
#             if dist[next_node] == -1:
#                 dist[next_node] = dist[v] + 1
#                 queue.append(next_node)
#     chk = False
#     for i in range(1, n+1):
#         if dist[i] == k:
#             print(i)
#             chk = True

#     if chk == False:
#         print(-1)


# from collections import deque
#
# roads = []
# # idxd_roads = []
# visited = []
# answer = []
# graph = [[]]
#
# def bfs(start, k):
#     # global idxd_roads
#     global visited
#     queue = deque([start])
#     visited[start] = True
#
#     tmp = 0
#     while queue and k:
#         v = queue.popleft()
#         if len(graph) != 0:
#             tmp = graph[v][-1]
#
#         print(v, end=' ')
#         # for h in idxd_roads:
#         for i in graph[v]:
#             if not visited[v]:
#                 queue.append(i)
#                 visited[i] = True
#             if i == tmp:
#                 k -= 1
#
#
# def solution():
#     global roads
#     # global idxd_roads
#     global visited
#     global graph
#
#     n, m, k, x = map(int, input("N,M,K,X: ").split())
#
#     # all_map = [[0]*n for _ in range(n)]
#     for _ in range(m):
#         a, b = map(int, input().split())
#         graph[a] = roads[b]
#
#     visited = [False] * (n + 1)
#     roads.sort()
#
#     graph = [[] for _ in range(n + 1)]
#
#     # idx = 1
#     # tmp = []
#     # for i in roads:
#     #     if i[0] != idx:
#     #         idxd_roads.append(tmp)
#     #         tmp.clear()
#     #         while i[0] != idx:
#     #             idx += 1
#     #     tmp.append(i)
#     # idxd_roads.append(tmp)
#
#     bfs(1, k)















