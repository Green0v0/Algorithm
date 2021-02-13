# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
from collections import deque
# n, m, k, x = map(int,input().split())
# graph = [list(map(int, input().split())) for _ in range(m)]
# graph.insert(0,[])?? visited = [False]* ??
# 가지치기
# 다익스트라 알고리즘
# dist = [float('inf')]*(n+1)
#     dist[x] = 0 # [inf,0,inf...]
#     queue = deque([x])
#     while queue:
#         current = queue.popleft()
#         for start, end in graph:
#             if start == current and dist[current] + 1 < dist[end]:
#                 queue.append(end)
#                 dist[end] = dist[current] + 1
# def solution(n, x, graph):
#     if x > n:
#         return [-1]
#     # dist = [float('inf')]*(n+1)
#     dist = [9999999]*(n+1)
#     dist[x] = 0 # [inf,0,inf...]
#     queue = deque([x])
#     while queue:
#         current = queue.popleft()
#         for start, end in graph:
#             if start == current and dist[current] + 1 < dist[end]:
#                 queue.append(end)
#                 dist[end] = dist[current] + 1
#     return dist
#
# # 도달할 수 있는 도시가 없는 경우 -1
#
# dist = solution(n, x, graph)
# for i in range(len(dist)):
#     if k not in dist:
#         print(-1)
#         break
#     if dist[i] == k:
#         print(i)

# 해설
# BFS 너비 우선 탐색
from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 도로정보를 인접 리스트로 변환시켜 저장
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # idx를 출발지점으로 생각

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# BFS(너비 우선 탐색) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)