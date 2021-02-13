
# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
from collections import deque
n, m, k, x = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
# idx <= 목적지 값 = 최단거리
dist = [float('inf')]*(n+1)
dist[x] = 0 # [inf,0,inf...]
queue = deque([x])
"""
4 4 1 1
1 2
1 3
2 3
2 4
"""
while queue:
    current = queue.popleft()
    for start, end in graph:
        if start == current and dist[current] + 1 < dist[end]:
            queue.append(end)
            dist[end] = dist[current] + 1

print(dist)
# 도달할 수 있는 도시가 없는 경우 -1
result = -1
for i in range(len(dist)):
    if k not in dist:
        # print(-1)
        # break
        print(result)
    elif dist[i] == k:
        # print(i)
        result = i
        print(result)