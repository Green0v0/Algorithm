X, Y = map(int, input().split())

maps = [list(input()) for _ in range(Y)]
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def dfs(maps, x, y, mark):
    stack = [(y, x)]
    cnt = 0
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny in range(Y) and nx in range(X) and maps[ny][nx] == mark:
                maps[ny][nx] = 'O'
                cnt += 1
                stack.append((ny, nx))
    if not cnt:
        cnt += 1
    return cnt

white_score = 0
blue_score = 0
for y in range(Y):
    for x in range(X):
        if maps[y][x] == 'W':
            white_score += dfs(maps, x, y, 'W')**2
        elif maps[y][x] == 'B':
            blue_score += dfs(maps, x, y, 'B')**2
print(white_score, blue_score)