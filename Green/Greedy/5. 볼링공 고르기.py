# 볼링공 고르기
# 조합하되, 같은 무게는 제외
from itertools import combinations
n, m = map(int, input().split())
kg = list(map(int, input().split()))
com = [i for i in combinations(kg,2)]
print(com)
cnt = 0 # 수를 카운트
for i,j in com:
    if i!=j:
        cnt+=1
print(cnt)