# 입력받는 숫자들중에 가장 작은 수들을 모아서 그 중 가장 큰 수 찾기 
#----처음 풀이--------------------------------------------------
# n,m = map(int,input().split())
# m =[]

# for _ in range(n):
#    k = list(map(int, input().split()))
#    d = min(k)
#    m.append(d)
# print(max(m))
#----------------------------------------------------------------

# 3 3
# 3 1 2
# 4 1 4 
# 2 2 2

# 이중 반복문 사용해서 문제 해결방법

n,m = map(int,input().split())
result = 0
for _ in range(n):
    k = list(map(int, input().split()))
    min_value = 1001
    for i in k :
       min_value = min (min_value,i)
result = max(result, min_value)
print(result)
       

