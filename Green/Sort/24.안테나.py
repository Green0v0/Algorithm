"""
4
5 1 7 9
"""
n = int(input())
houses = list(map(int, input().split()))
houses.sort()

print(houses[(n-1)//2])




# def getdist(a,b):
#     return abs(a-b)

# answer = []
# for antenna in range(houses[0], houses[-1]+1):
#     # dist_lst = list(map(getdist, (antenna, houses)))
#     # answer.append((antenna, sum(dist_lst)))
#     tmp_sum = 0
#     for house in houses:
#         # dist_lst = list(map(getdist, (antenna, house)))
#         tmp_sum += getdist(antenna,house)
#     answer.append((tmp_sum, antenna))
    
# answer.sort(key=lambda x: x[0])

# print(answer[0][1])
