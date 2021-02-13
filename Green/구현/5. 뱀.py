n = int(input().rstrip()) # 보드의 크기
k = int(input().rstrip()) # 사과의 개수
# 사과의 위치
apple = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    x,y = map(int, input().split())
    apple[y-1][x-1] = 2
print(apple)