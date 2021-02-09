## 접근법
- 문제의 요구사항을 따른다!!...
## flow
1. 2차원 배열 n * n 으로 만든다.
2. 사과는 2, 뱀은 1로 맵에 표시
3. 시간(time)과 방향에 관련된 변수, 함수를 정의
4. 게임이 끝날 때 까지 반복문을 돌린다. 
    1. time+1, 앞으로 이동
    2. 앞에으로 갔을 때 맵을 벗어나거나 자신의 몸(1)에 닿는지 확인
        1. 닿았으면 게임 끝 break
        2. 안닿았으면
            1. 사과가 있는지 확인
                1. 없으면 앞으로 전진하고 뱀의 꼬리부분(뱀 배열의 처음 값)을 제거
                2. 있으면 앞으로만 전진
            2. 방향을 전환 시간 확인
                1. 전환할 시간이면 방향전환 함수 ㄱㄱ
                2. 아니면 pass
5. 반복문을 나오면 time을 반환
```python
def turn(d, c):
  if c == 'L':
    d = (d-1)%4
  else:
    d = (d+1)%4
  return d
def solution():
  direction = 1 # 처음 방향 동쪽
  # 북동남서 순서
  dy = [-1,0,1,0]
  dx = [0,1,0,-1]
  y, x = 0, 0 # 초기 뱀의 방향
  map_arr[y][x] = 1
  snake = [[y,x]]
  time = 0

  while True:
    time+=1
    y += dy[direction]
    x += dx[direction]

    if y == -1 or y == n or x == -1 or x == n or map_arr[y][x] == 1:
      break # 맵을 벗어나거나 자신의 몸에 닿으면 게임 끝
      
    else: 
      if map_arr[y][x] == 0: # 아무것도 없다면
        map_arr[y][x] = 1
        snake.append([y,x])
        a, b = snake.pop(0) # 꼬리제거
        map_arr[a][b] = 0 
      elif map_arr[y][x] == 2: # 사과가 있다면
        map_arr[y][x] = 1
        snake.append([y,x])

    if time in time_location.keys():
      direction = turn(direction, time_location[time])
  return time

if __name__ == "__main__":
  n = int(input()) # 맵크기
  k = int(input()) # 사과 갯수
  map_arr = [[0]*n for _ in range(n)] # 맵 만들기
  for _ in range(k):
    a, b = map(int, input().split())
    map_arr[a-1][b-1] = 2 # 맵의 사과 2로 표시 
  l = int(input()) # 시간과 방향
  time_location = {}
  for _ in range(l): # keys = 시간, values = 방향
    x, c = input().split()
    time_location[int(x)] = c

  print(solution())

```
