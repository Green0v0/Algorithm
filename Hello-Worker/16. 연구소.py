# 3개의 벽 세우기 : 1을 3개 대입- 조합 이용
# 최대 안전 구역 확보 : 2가 min인 경우 = 0이 max인 경우 - BFS탐색

import copy
from itertools import combinations

# 입력받기
n,m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

list_0 = []
list_1 = []
list_2 = []

# 위치리스트
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            list_0.append([i, j])
        if data[i][j] == 1:
            list_1.append([i,j])
        if data[i][j] == 2:
            list_2.append([i, j])

# 바운더리 체크
def iswall(x,y):
    if x<0 or x>=m or y<0 or y>=n:
        return True
    return False

# BFS
def BFS():
    copy_data = copy.deepcopy(data)

# check

# 벽 세우기
for case in combinations(list_0,3):
    if check():
        exit()
    for [x, y] in case:
        data[x][y] = '0'


# 0의 개수 찾기
def cnt_zero(data):
    cnt = 0
    for x in range(len(n)):
        for y in range(len(m)):
            if data[x][y] == 0:
                cnt += 1
    return cnt

# 0 max 찾기
