from collections import deque

n, m = map(int, input().split())
graph = []
vstd = [[False]*m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, list(input()))))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 1
q = deque()
q.append((0,0))
vstd[0][0] = True

while q:
    to_break = False
    for _ in range(len(q)):
        now = q.popleft()
        i, j = now[0], now[1]
        if i == n-1 and j == m-1:
            to_break = True
            break
        for drt in range(4):
            x, y = i + dx[drt], j + dy[drt]
            if x in range(n) and y in range(m)\
                and graph[x][y] and not vstd[x][y]:
                vstd[x][y] = True
                q.append((x, y))
    if to_break:
        break
    answer += 1
    
print(answer)

"""
4 6
101111
101010
101011
111011
"""
"""
4 6
110110
110110
111111
111101
"""
"""
2 25
1011101110111011101110111
1110111011101110111011101
"""


# n, m = map(int, input().split())
# graph = []
# vstd = [[False]*m for _ in range(n)]

# for _ in range(n):
#     graph.append(list(map(int, list(input()))))

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# answer = 100001
# def dfs(i, j, now):
#     if i == n-1 and j == m-1:
#         global answer
#         answer = min(answer, now)
#     for drt in range(4):
#         x, y = i + dx[drt], j + dy[drt]
#         if x in range(n) and y in range(m)\
#             and graph[x][y] and not vstd[x][y]:
#             vstd[x][y] = True
#             dfs(x, y, now+1)
#             vstd[x][y] = False

# dfs(0,0,1)
# print(answer)