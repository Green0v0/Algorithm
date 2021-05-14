from collections import deque

Y, X = map(int, input().split())
maps = [list(input()) for _ in range(Y)]

def bfs(start):
    dq = deque([start])
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    while dq:
        y, x, cost = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny in range(Y) and nx in range(X) and maps[ny][nx] == '1':
                if ny == Y-1 and nx == X-1:
                    return cost + 1
                else:
                    maps[ny][nx] = 'v'
                    dq.append([ny, nx, cost+1])
print(bfs([0, 0, 1]))
