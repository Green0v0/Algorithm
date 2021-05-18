# from itertools import combinations
# # #순열, 조합은 combinations permunations
# N, M = map(int(input().split()))
# weight = list(int(input().split()) #볼링공의 각각 무게
# a = list(combinations(weight,2))
# print(len(a))

N, M = map(int, input().split())
weight = list(map(int, input().split()))
cnt = 0
for i in range(len(weight)): #리스트 개수만큼 반복
    for j in range(i, len(weight)): # i부터 리스트 요소의 개수만큼 반복
        if weight[i] != weight[j]: #weight[i]와 weight[j]가 같지 않다면 (for (1,1)중복제거)
            cnt +=1 #cnt 경우의수 +1
print(cnt)