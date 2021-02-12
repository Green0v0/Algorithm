n, m = 4, 5
graph = [
  [0,0,1,1,0],
  [0,0,0,1,1],
  [1,1,1,1,1],
  [0,0,0,0,0]
]

def dfs(y, x):
  if y <= -1 or y >= n or x <= -1 or x >= m:
    return False # 범위를 벗어나면 false
  if graph[y][x] == 0:
    graph[y][x] = 1
    # 상하좌우 제귀로 확인
    dfs(y-1, x)
    dfs(y+1, x)
    dfs(y, x-1)
    dfs(y, x+1)
    # 처음노드를 기준으로 인접해있는 0을 전부 1로 바꾼다.
    return True
  return False

cnt = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j):
      cnt+=1

print(cnt)
# 결과값 : 3