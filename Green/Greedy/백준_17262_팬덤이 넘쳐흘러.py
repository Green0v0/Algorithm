n = int(input())
max_x = float('-inf') # -무한대
min_y = float('inf') # 무한대
# min_y = 1000000000
# (1 ≤ si ≤ ei ≤ 100,000)
for i in range(n):
    x, y = map(int,input().split())
    # 최소의 최대, 최대의 최소
    max_x = max(x, max_x)
    min_y = min(y, min_y)

print(max_x, min_y)

if min_y - max_x > 0:
    print(0)
else:
    print(abs(min_y - max_x))
