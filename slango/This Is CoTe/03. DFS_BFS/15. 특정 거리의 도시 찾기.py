# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

from collections import deque

roads = []
idxd_roads = []
visited = []
answer = []

def bfs(start, k, visited):
    global roads
    global idxd_roads
    queue = deque([start])
    if k < 0:
        for i in queue:
            answer.append(i)

    visited[start] = True
    while queue and k:
        v = queue.popleft()
        k -= 1
        print(v, end=' ')
        for h in roads:
            if not visited[v]:
                queue.append(h)
                visited[h] = True


def solution():
    global roads
    global idxd_roads
    global visited
    n, m, k, x = map(int, input("N,M,K,X: ").split())

    # all_map = [[0]*n for _ in range(n)]
    for _ in range(m):
        roads.append(list(map(int, input().split())))

    visited = [False] * (n + 1)


    roads = sorted(roads)

    # idxd_roads => [
    #     [[1,2], [1,3]],
    #     [[2,3], [2,4]]
    # ]
    idx = 1
    tmp = []
    for i in roads:
        if i[0] != idx:
            idxd_roads.append(tmp)
            tmp.clear()
            while i[0] != idx:
                idx += 1
        tmp.append(i)
    idxd_roads.append(tmp)

    bfs(1, k, visited)


solution()
















