from collections import deque

# 입력받기
n, k = map(int, input().split())

maps = [[0]*(n+1)]
for _ in range(n):
    maps.append([0] + list(map(int, input().split())))

s, x, y = map(int, input().split())


# 바이러스 좌표
virs_idx = [[] for _ in range(k+1)]
for i in maps:
    for j in i:
        # 해당 자리에 바이러스가 있다면 좌표 virs_idx에 넣기awwwwwwwwwwwww
        if j:
            virs_idx[j] = [maps.index(i), i.index(j)]

# 방문 리스트는 맵의 바이러스 번호로 대체 가능
# # 방문 리스트
# visited = [[False] * (n+1) for _ in range(n+1)]

# 바이러스마다 확인할 위치를 큐로 리스트에 추가
virs_que = []
for i in virs_idx:
    virs_que.append(deque([i]))

# bfs 메소드 정의
def vir_bfs(now_vir, maps):
    # 한번에 푸쉬할 임시큐
    tmp_q = virs_que[now_vir]
    virs_que[now_vir] = deque()

    for v in tmp_q:
        if v[0] > 1 and not maps[v[0]-1][v[1]]:
            virs_que[now_vir].append([v[0]-1, v[1]])
            maps[v[0]-1][v[1]] = now_vir
        if v[0] < n and not maps[v[0]+1][v[1]]:
            virs_que[now_vir].append([v[0]+1, v[1]])
            maps[v[0]+1][v[1]] = now_vir
        if v[1] > 1 and not maps[v[0]][v[1]-1]:
            virs_que[now_vir].append([v[0], v[1]-1])
            maps[v[0]][v[1]-1] = now_vir
        if v[1] < n and not maps[v[0]][v[1]+1]:
            virs_que[now_vir].append([v[0], v[1]+1])
            maps[v[0]][v[1]+1] = now_vir


for _ in range(s):
    for i in range(1, k+1):
        vir_bfs(i, maps)

print(maps[x][y])


# # 1st try:
# from collections import deque
#w
# # 입력받기
# n, k = map(int, input().split())
#
# maps = [[]]
# for _ in range(n):
#     maps.append([0] + list(map(int, input().split())))
#
# s, x, y = map(int, input().split())
#
#
# # 바이러스 좌표
# virs_idx = [[] for _ in range(k+1)]
# for i in maps:
#     for j in i:
#         # 해당 자리에 바이러스가 있다면 좌표 virs_idx에 넣기
#         if j:
#             virs_idx[j] = [maps.index(i), i.index(j)]
#
# # 방문 리스트는 맵의 바이러스 번호로 대체 가능
# # # 방문 리스트
# # visited = [[False] * (n+1) for _ in range(n+1)]
#
# # 바이러스마다 확인할 위치를 큐로 리스트에 추가
# virs_que = []
# for i in virs_idx:
#     virs_que.append(deque([i]))
#
# # bfs 메소드 정의
# def vir_bfs(now_vir, maps):
#     v = virs_que[now_vir].popleft()
#     if v[0] > 1 and not maps[v[0]-1][v[1]]:
#         virs_que[now_vir].append([v[0]-1, v[1]])
#         maps[v[0]-1][v[1]] = now_vir
#     if v[0] < n and not maps[v[0]+1][v[1]]:
#         virs_que[now_vir].append([v[0]+1, v[1]])
#         maps[v[0]+1][v[1]] = now_vir
#     if v[1] > 1 and not maps[v[0]][v[1]-1]:
#         virs_que[now_vir].append([v[0], v[1]-1])
#         maps[v[0]][v[1]-1] = now_vir
#     if v[1] < n and not maps[v[0]][v[1]+1]:
#         virs_que[now_vir].append([v[0], v[1]+1])
#         maps[v[0]][v[1]+1] = now_vir
#
# for _ in range(s):
#     for i in range(k):
#         vir_bfs(i+1, maps)
#
# print(maps[x][y])

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2

# 4 2
# 1 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 2
# 3 3 2

# 2 4
# 1 2
# 3 4
# 1 1 1