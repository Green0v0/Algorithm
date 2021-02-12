from collections import deque
n,m = map(int, input().split())
graph = [list(map(int,input())) for _ in range(n)]

# queue = deque([[0,0]])
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# cnt = 0
# while queue:
#     x, y = queue.popleft()
#     graph[x][y] = 0
#     past = len(queue)
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or nx >= n or ny < 0 or ny >= m:
#             continue
#         if graph[nx][ny] == 1:
#             queue.append([nx, ny])
#     curr = len(queue)
#     if past != curr:
#         cnt += 1
#     if x == n-1 and y == m-1:
#         # cnt+=1
#         break
# print(cnt)

# 답지
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(dfs(0,0))