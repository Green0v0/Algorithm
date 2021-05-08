# NxN 정사각형 연구소
# 빈칸, 벽, 바이러스로 이루어져있다
# 활성 바이러스가 비활성 바이러스로 가면 비활성이 활성으로 변한다

# 출력: 모든 빈 칸에 바이러스가 있게 되는 최소 시간
# 모든 빈 칸에 바이러스를 놓을 수 없으면 -1 출력

from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while a:
        x, y = a.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and s[nx][ny] != 1:
                visit[nx][ny] = 1
                a.append([nx, ny])
                cs[nx][ny] = cs[x][y] + 1

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
s = []
q = []
b = 0
inf = 100000000
result = inf

for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(n):
        if a[j] == 2:
            q.append([i, j])
        if a[j] != 1:
            b += 1
cq = list(combinations(q, m))

for i in cq:
    cs = [[-1] * n for i in range(n)]
    visit = [[0] * n for i in range(n)]
    a = deque()
    for x, y in i:
        visit[x][y] = 1
        cs[x][y] = 0
        a.append([x, y])
    bfs()
    cnt = 0
    for j in visit:
        cnt += j.count(1)
    if b == cnt:
        max_n = 0
        for j in range(n):
            for k in range(n):
                if s[j][k] != 1 and [j, k] not in q:
                    max_n = max(max_n, cs[j][k])
        result = min(result, max_n)

print(result if result != inf else -1)

# N이 최대 50이므로 맵 전체를 탐색한다면 2500번,
# 2의 개수는 10보다 작거나 같으므로 대략 10C5정도가 가장 큰 경우의 수
# 10C5 * 2500 * 5 = 315만
# 가지치기 해서 풀어보자

from collections import deque
from itertools import combinations


def BFS(candis, min_time, left):
    global time
    q = deque(candis)
    time_val = 0
    visited = [[0 for i in range(N)] for j in range(N)]
    for y, x in candis:
        visited[y][x] = 1

    while q:
        if not left: break
        time_val += 1
        if time_val >= min_time: return float('inf')
        for i in range(len(q)):
            y, x = q.popleft()

            for j in range(4):
                ny = y + dy[j]
                nx = x + dx[j]

                if 0 <= ny < N and 0 <= nx < N and field[ny][nx] != 1 \
                        and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                    if field[ny][nx] == 0:
                        left -= 1

    if not left:
        return time_val
    else:
        return float('inf')


N, M = map(int, input().split())
field = [list(map(int, input().split())) for i in range(N)]
virus_candis = []
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
time = float('inf')
left = 0

for i in range(N):
    for j in range(N):
        if field[i][j] == 2:
            virus_candis.append((i, j))
        if field[i][j] == 0:
            left += 1

for candi in combinations(virus_candis, M):
    time = min(time, BFS(candi, time, left))

if time == float('inf'): time = -1

print(time)

# 방법 1
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

virus = []
num_virus = 9999
safe = -3  # 벽을 3개 꼭 세워야함.


def dfs(x, y):  # virus를 퍼뜨린다.
    res = 1
    visited[x][y] = True
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):  # 위, 아래, 좌, 우
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 맵의 경계보다 커진다면
            continue  # 넘어간다.
        if not (visited[nx][ny] or board[nx][ny]):  # 방문하지 않았거나, 빈칸이 아니라면
            res += dfs(nx, ny)
    return res


def solve(start, wall):  # 벽을 세운다
    global n, m, num_virus, visited
    if wall == 3:  # 벽이 3개라면
        count = 0
        visited = [[False] * m for _ in range(n)]
        for x, y in virus:
            count += dfs(x, y)
        num_virus = min(num_virus, count)
        return
    for i in range(start, n * m):  # 2차원 배열에서 x, y의 조합을 뽑습니다.
        x = i // m
        y = int(i % m)
        if board[x][y] == 0:  # 빈칸(0) 이라면
            board[x][y] = 1  # 벽(1)을 세운다
            solve(i + 1, wall + 1)
            board[x][y] = 0  # 위에서 세운 벽을 다시 빈칸(0)으로 만든다. (초기화)


for i in range(n):
    for j in range(m):
        if board[i][j] != 1:  # 벽이 아니라면,
            safe += 1
        if board[i][j] == 2:  # virus라면
            virus.append((i, j))

solve(0, 0)
print(safe - num_virus)

# 방법 2
from itertools import combinations
from copy import deepcopy
from _collections import deque


def check(lab_tmp):  # 오염 안된 구역이 있는지 없는지 확인
    for i in range(n):
        for j in range(n):
            if lab_tmp[i][j] == '0':
                return False
    else:
        return True


def infection(virus):
    global min_time
    tmp_lab = deepcopy(lab)
    virus = deque(virus)
    for i, j in virus:  # 처음 활성화 시킬 바이러스를 0으로 초기화 해주고
        tmp_lab[i][j] = 0

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    time = 0
    virus_cnt = 0
    while virus:  # 바이러스를 퍼뜨리는 작업
        if virus_cnt == virus_count:  # 모든바이러스를 퍼뜨리면 break( 비활성화 된 바이러스는 굳이 활성화 시킬 필요 없다)
            break
        x, y = virus.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if tmp_lab[nx][ny] == '2':
                    virus.append((nx, ny))
                    tmp_lab[nx][ny] = tmp_lab[x][y] + 1
                    time = tmp_lab[nx][ny]

                elif tmp_lab[nx][ny] == '0':
                    virus.append((nx, ny))
                    tmp_lab[nx][ny] = tmp_lab[x][y] + 1
                    virus_cnt += 1  # 빈공간을 오염시켰을 때는 +1을 해준다.
                    time = tmp_lab[nx][ny]  # time에는 마지막 시간을 덮어씌워준다.

        if time > min_time:  # 가지치기 | 최솟값보다 크면 return
            return

    if check(tmp_lab):  # 모든 구역이 오염됐다면 break
        pass
    else:
        time = 2500

    min_time = min(time, min_time)


n, m = map(int, input().split())
lab = [input().split() for _ in range(n)]
min_time = 2500


virus_all = []  # 모든 바이러스의 위치를 저장
virus_count = 0  # 바이러스의 개수 -> 나중에 바이러스 퍼뜨릴 때 바이러스가 이미 다 퍼져있음에도 비활성화된 바이러스로 퍼져가려는 것을 막기 위해!
for i in range(n):
    for j in range(n):
        if lab[i][j] == '2':
            virus_all.append((i, j))
        elif lab[i][j] == '0':
            virus_count += 1

virus_combis = combinations(virus_all, m)  # 바이러스를 활성화 시킬 수 있는 갯수에 따른 경우의 수 만들기
for virus_combi in virus_combis:  # 각각의 경우의 수 마다 바이러스를 퍼뜨리는 함수 실행
    infection(virus_combi)

if min_time == 2500:  # 바이러스를 모두 퍼뜨릴 수 없는 경우
    print(-1)
else:  # 바이러스를 퍼뜨린 경우
    print(min_time)