"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""

"""
10 15
8  1  0
2 7 4 4
4 5 2 6 5
"""
"""
18 16 15  dp = [18, 16, 15]
2  7  4  4
4 5 2 6 5
"""

n = int(input())

triangle = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    triangle.append(tmp)

for i in range(n-1):
    for j in range(i+2):
        if j == 0:
            triangle[i+1][j] += triangle[i][j]
        elif j == i+1:
            triangle[i+1][j] += triangle[i][j-1]
        else:
            triangle[i+1][j] += max(triangle[i][j], triangle[i][j-1])

print(max(triangle[-1]))


dp = [0]*n
dp[0] = triangle[0][0]