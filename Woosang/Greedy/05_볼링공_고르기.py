# 이중 for문으로 한개씩 비교

n, m = map(int, input().split())
balls = list(map(int, input().split()))

cnt = 0

for first in range(n): # 처음 공
    for second in range(first, n): # 두번째 공
        if balls[first] != balls[second]: 
            cnt += 1 # 두 공의 무게가 다르면 counting
print(cnt)

# n, m = 5, 3
# balls = [1,3,2,3,2]