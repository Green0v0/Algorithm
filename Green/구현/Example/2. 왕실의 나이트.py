n = list(input())
li = ['a','b','c','d','e','f','g','h']
target = [0,0]
for j in li:
    if n[0] == j:
        target[0] = li.index(j) + 1
target[1] = int(n[1])
dx = [-2,-1,1,2,-2,-1,1,2]
dy = [-1,-2,-2,-1,1,2,2,1]
cnt = 0
for i in range(len(dx)):
    nx = target[0] - dx[i]
    ny = target[1] - dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny>8:
        continue
    cnt+=1
print(cnt)
# 현재의 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 #ord()는 알파벳을 유니코드로 바꿔주는 함수, 숫자로 변환할 때 사용되었다.

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_colum = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >=1 and next_row<=8 and next_colum>=1 and next_colum<=8:
        result+=1
print(result)
