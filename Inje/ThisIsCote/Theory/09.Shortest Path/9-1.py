## 간단하지만 복잡도 N^2 인 알고리즘

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 의미

# 노드 개수, 간선 개수 입력
n, m = map(int, input().split())
# 시작 노드 입력
strt = int(input())

# 번호 그대로 인덱스로 사용하기 위해 각 리스트의 크기는 n+1로 설정
# 각 노드에 연결된 노드 정도 담을 리스트
graph = [[] for i in range(n+1)]
# 방문 여부 체크 리스트
vstd = [False] * (n+1)
# 최단 거리 테이블 모두 무한으로 초기화
dist = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append(((b, c)))

# 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 번호 반환
def get_smallest_node():
    min_val = INF
    index = 0 # 최단거리가 가장 짧은 노드
    for i in range(1, n+1):
        if dist[i] < min_val and not vstd[i]:
            min_val = dist[i]
            index = i
    return index

def dijkstra(strt):
    # 시작 노드에 대해 초기화
    dist[strt] = 0
    vstd[strt] = True
    for j in graph[strt]:
        dist[j[0]] = j[1]
    # 시작 노드 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드 꺼내어 방문처리
        now = get_smallest_node()
        vstd[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = dist[now] + j[1]
        # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
        if cost < dist[j[0]]:
            dist[j[0]] = cost

# 다익스트라 수행
dijkstra(strt)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우 무한으로 출력
    if dist[i] == INF:
        print("INFINITY")
    # 있을 경우 거리 출력
    else:
        print(dist[i])


# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2