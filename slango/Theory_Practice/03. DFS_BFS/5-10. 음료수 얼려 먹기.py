# 그래프 연결관계를 행렬로 표시할 시,
# INF는 연결되지 않음을, 0은 자기자신과의 연결을 나타낼 때 주로사용
INF = 999999999

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        # 현재 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)