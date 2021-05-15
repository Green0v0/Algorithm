from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input().rstrip()))
"""
4 6
101111
201010
301011
411011
"""

visited = [[False] * M for _ in range(N)]
dq = deque([(0,0)])

board[0][0] = 1
visited[0][0] = True

while dq:
    nx, ny = dq.popleft()
    for x, y in [(1,0),(0,1),(-1,0),(0,-1)]:
        cx, cy = nx + x, ny + y
        if cx < 0 or cx >= N or cy < 0 or cy >= M:
            continue
        if board[cx][cy] == '1' and visited[cx][cy] == False:
            dq.append((cx,cy))
            board[cx][cy] = board[nx][ny] + 1

print(board[-1][-1])