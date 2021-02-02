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

# 해설
n, m = map(int,input().split())
kg = list(map(int,input().split()))
array = [0]*11  # 인덱스 무게를 가진 수를 count
# 각 무게에 해당하는 볼링공의 개수 카운트
for i in kg:
    array[i]+=1
result = 0
# 1~m까지의 각 무게에 대하여 처리
for j in range(1,m+1):
    n-=array[j] # 무게가 i인 볼링공의 개수 제외 (A가 선택할 수 있는 개수)
    result += array[j]*n # B가 선택하는 경우의 수와 곱하기
print(result)