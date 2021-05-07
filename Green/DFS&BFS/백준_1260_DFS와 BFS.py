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

# 다른 사람 풀이
N,M,V=map(int,input().split())
matrix=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
visit_list=[0]*(N+1)

def dfs(V):
    visit_list[V]=1 #방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1,N+1):
        if(visit_list[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):
    queue=[V] #들려야 할 정점 저장
    visit_list[V]=0 #방문한 점 0으로 표시
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i]==1 and matrix[V][i]==1):
                queue.append(i)
                visit_list[i]=0

dfs(V)
print()
bfs(V)

# 다른 사람 풀이
N, M, V = map(int, input().split())

# Graph Set
graph_list = [set([]) for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph_list[i].add(j)
    graph_list[j].add(i)


# DFS
def dfs(graph_list, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += sorted(list(graph_list[node] - set(visited)), reverse=True)
            # 스택은 뒤부터 나가니 역순 정렬

    return visited


# BFS
def bfs(graph_list, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue += sorted(list(graph_list[node] - set(visited)))
            # 큐는 앞부터 나가니 순정렬

    return visited


for i in list(dfs(graph_list, V)):
    print(i, end=" ")
print()
for j in list(bfs(graph_list, V)):
    print(j, end=" ")