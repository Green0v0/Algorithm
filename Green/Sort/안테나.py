n = int(input().rstrip())
houses = list(map(int, input().split()))
houses.sort()
# result = []
# for start in range(houses[0],houses[-1]):
#     m = 0
#     for i in range(n):
#         m += abs(start - houses[i])
#     result.append((start,m))
#
# result.sort(key=lambda x:x[1])
# print(result[0][1])

# 다른 풀이
answer = houses[len(houses)//2] if n % 2 == 1 else houses[len(houses)//2 -1]
print(answer)