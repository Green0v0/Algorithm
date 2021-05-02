from itertools import combinations
import copy
N = int(input())
maps = [list(input().split()) for _ in range(N)]
teacher_loc = []
empty_loc = []

def explore_around(maps, y, x, direction):
    global ret
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    ny = y + dy[direction]
    nx = x + dx[direction]
    if ny in range(N) and nx in range(N):
        if maps[ny][nx] in ['X', 'T']:
            maps[ny][nx] = 'T'
            stack.append((ny, nx))
        elif maps[ny][nx] == 'S':
            ret = 'NO'

# 빈공간과 선생님 위치 정보 저장
for i in range(N):
    for j in range(N):
        if maps[i][j] == 'T':
            teacher_loc.append((i, j))
        elif maps[i][j] == 'X':
            empty_loc.append((i, j))

for combine in list(combinations(empty_loc, 3)):
    # 장애물 세우기
    maps_copy = copy.deepcopy(maps)
    for y, x in combine:
        maps_copy[y][x] = 'O'
    ret = 'YES'
    # 선생님을 기준으로 한방향씩 쭉 탐색하기
    for direction in range(4):
        stack = copy.deepcopy(teacher_loc)
        while stack and ret != 'NO':
            y, x = stack.pop()
            explore_around(maps_copy, y, x, direction)
        if ret == 'NO':
            break
    # ret이 Yes면 멈추기
    if ret == 'YES':
        break
print(ret)

