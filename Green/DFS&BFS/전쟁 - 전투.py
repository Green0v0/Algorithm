# BFS
from collections import deque
m, n = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
check = [[False]*m for _ in range(n)]
w, b = 0, 0

def bfs(i, j, c):
    q = deque()
    q.append((i, j))
    cnt = 1
    check[i][j] = True
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not check[nx][ny] and a[nx][ny] == c:
                q.append((nx, ny))
                check[nx][ny] = True
                cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        if not check[i][j]:
            k = bfs(i, j, a[i][j])
            if a[i][j] == 'W':
                w += k*k
            else:
                b += k*k
print(w, b)
"""
5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW
"""
