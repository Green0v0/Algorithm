from collections import deque
from itertools import combinations
import copy
Y, X = map(int, input().split())

# 상하좌우 확인 함수
def explore_around(maps, x, y):
    if y-1 != -1 and maps[y-1][x] == 0:
        maps[y-1][x] = 2
        dq.append((y-1, x))

    if y+1 != Y and maps[y+1][x] == 0:
        maps[y+1][x] = 2
        dq.append((y+1, x))

    if x-1 != -1 and maps[y][x-1] == 0:
        maps[y][x-1] = 2
        dq.append((y, x-1))

    if x+1 != X and maps[y][x+1] == 0:
        maps[y][x+1] = 2
        dq.append((y, x+1))


# 맵 생성
maps, temp = [], []
for _ in range(Y):
    arr = list(map(int, input().split()))
    maps.append(arr)
    temp.extend(arr)

# 빈공간과 바이러스의 좌표 저장
zero_idx, virus_locations = [], []
for i in range(len(temp)):
    if temp[i] == 0:
        zero_idx.append(i)
    elif temp[i] == 2:
        virus_locations.append((i//X, i%X))

result = 0
# 벽을 세울수 있는 모든 경우의 수 탐색
for combine in list(combinations(zero_idx, 3)):
    maps_copy = copy.deepcopy(maps)
    for i in combine:
        y = i//X
        x = i%X
        maps_copy[y][x] = 1
        # 모든 경우의 벽을 세운다.
    # 초기 virus의 위치 정보를 넘겨주고 BFS
    dq = deque(virus_locations)
    while dq:
        y, x = dq.popleft()
        explore_around(maps_copy, x, y)
    # 0의 갯수가 많은 것을 남기기
    zero_cnt = sum([arr.count(0) for arr in maps_copy])
    result = max(zero_cnt, result)

print(result)