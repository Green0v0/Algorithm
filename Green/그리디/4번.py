# 만들 수 없는 금액
# 목표 : 조합해서 만들 수 없는 최소값
# sorting하여 모두 조합해보기
# 빈 리스트에 인덱스를 더한 값으로 생각하고 (index 0제외) 0일 때, 없는 경우라고 생각.
from itertools import combinations
n = int(input().rstrip())
nlist = list(map(int,input().split()))
nlist.sort()
test = [0 for i in range(sum(nlist)+1)]
# 어떻게 더할지 생각
for i in range(1,n+1):
    for j in list(combinations(nlist,i)):
        test[sum(j)] = 1
test = test[1:]
print(test.index(0)+1)