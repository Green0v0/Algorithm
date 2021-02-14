import sys
input = sys.stdin.readline
# input보다 입력받는 시간이 빠름
from collections import deque

n, m, k, x = map(int, input().split())
nodes = [[] for _ in range(n+1)] # 각 노드 리스트 생성
for _ in range(m):
  a, b = map(int, input().split())
  nodes[a].append(b) # 각 노드 리스트의 값을 삽입

# 각 노드 거리 초기화 (방문하지 않은 곳 -1)
distince = [-1] * (n + 1) 
distince[x] = 0
dq = deque([x]) # 처음 위치를 받는다.

while dq:
  curr = dq.popleft() # 처음 위치 넘기기
  for next_node in nodes[curr]: # 노드무리의 처음 위치 탐색
    if distince[next_node] == -1:
      # 방문하지 않은 곳이라면 거리를 저장
      distince[next_node] = distince[curr] + 1
      dq.append(next_node)

check = False
for i in range(1, n+1):
  if distince[i] == k:
    print(i)
    check = True

if check is False:
  print(-1)