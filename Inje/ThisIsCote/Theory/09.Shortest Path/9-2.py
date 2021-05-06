import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
strt = int(input())
# 각 노드에 연결되어 있는 노드 정보 담는 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 모두 무한으로 초기화
dist = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용 = c
    graph[a].append((b, c))

def dijkstra(strt):
    q = []
    # 시작 노드로 가기 위한 최단 경로 0으로 하여 큐에 삽입
    heapq.heappush(q, (0, strt))
    dist[strt] = 0
    while q: # 큐에 내용물이 있을 동안
        # 최단 거리가 가장 짧은 노드에 대한 정보 pop
        dis, now = heapq.heappop(q)
        # 현재 노드가 이미 처리되었다면 무시
        if dist[now] < dis:
            countinue
        # 현재 노드와 연결된 다른 인접한 노드를 확인
        for i in graph[now]:
            cost = dis + i[1]
            # 현재 노드 거쳐서 다른 노드까지의 경로가 더 짧을 경우
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(strt)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if dist[i] == INF:
        print("INFINITY")
    # 아니라면 거리 출력
    else:
        print(dist[i])

6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2