# 처음 풀이
n = 5
# R R R U D D
li = list(input().split())
R = [0,1]
L = [0,-1]
D = [1,0]
U = [-1,0]
start = [1,1]
for i in range(len(li)):
    if li[i] == 'R':
        li[i] = R
    elif li[i] == 'L':
        li[i] = L
    elif li[i] == 'D':
        li[i] = D
    else:
        li[i] = U
for i in li:
    start[0] += i[0]
    start[1] += i[1]
    if start[0] == 0 or start[1] == 0:
        start[0] -= i[0]
        start[1] -= i[1]
print(start)
# 답지
n = int(input())
x,y = 1,1
plans = input().split()
# 이동값
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans: # 굳이 리스트에 담지 않음
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i] # x = x + dx[i]가 아닌 한 번 다른 변수에 담고 그 이후 (조건이 맞다면) 업데이트
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n: #첫 풀이는 n보다 큰 경우 생각하지 않았슴
        continue
    # 업데이트값으로 수정
    x,y = nx, ny
print(x,y)