from collections import deque

n, m = 5, 6
graph = [
  [1,0,1,0,1,0],
  [1,1,1,1,1,1],
  [0,0,0,0,0,1],
  [1,1,1,1,1,1],
  [1,1,1,1,1,1]
]

def bfs(y,x):
  q = deque()
  q.append((y, x))
  dy = [-1, 0, 1, 0]
  dx = [0, 1, 0, -1]
  while q:
    y, x = q.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      # 맵을 벗어나거나 괴물한테 가면 바로 반복
      if ny == -1 or ny == n or nx == -1 or nx == m or graph[ny][nx] == 0:
        continue
      # 원하는 인덱스들이 나오면 끝내기 (괜찮은건가?..)
      elif y == n-1 and x == m-1:
        return graph[n-1][m-1]
      # 갈수 있는 길이면 가면서 새로운길 지나가면서 count하기
      if graph[ny][nx] == 1:
        graph[ny][nx] = graph[y][x] + 1
        q.append((ny, nx))
  return graph[n-1][m-1]

print(bfs(0,0))