from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(input()))

vstd = [[False] * n for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt_w, cnt_b = 0, 0
def bfs(i, j):
    global cnt_w, cnt_b
    que = deque([])
    now_color = graph[i][j]
    vstd[i][j] = True
    que.append((i,j))
    if now_color=='W':
        cnt_w += 1
    else:
        cnt_b += 1
    while que:
        now_i, now_j = que.popleft()
        for direct in range(4):
            x, y = now_i+dx[direct], now_j+dy[direct]
            if x in range(m) and y in range(n)\
                and not vstd[x][y] and graph[x][y]==now_color:
                vstd[x][y] = True
                que.append((x,y))
                if now_color=='W':
                    cnt_w += 1
                else:
                    cnt_b += 1


pow_w, pow_b = 0, 0
for i in range(m):
    for j in range(n):
        if not vstd[i][j]:
            bfs(i, j)
            pow_w += cnt_w**2
            pow_b += cnt_b**2
            cnt_w, cnt_b = 0, 0

print(pow_w, pow_b)

# 5 5
# WBWWW
# WWWWW
# BBBBB
# BBBWW
# WWWWW