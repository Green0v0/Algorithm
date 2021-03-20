# n,m = map(int,input().split())
# k= list(map(int,input().split()))

# n,m= 8,5
# k = [1,5,4,3,2,4,5,2]

# import time

# start_time = time.time()

# n,m= 10,3
# data= [1,3,2,3,2,1,2,3,2,3,]

# count =0
"""
1. 인덱스를 사용했다.
2. k[1]!=k[j] 이면 count 했다.(조합// 서로 다른 무게의 볼링공을 고른다!// 무게가 같아도 다른 공으로 생각한다.)
3. k[1]==k[j] 이면 같은 무게 pass
* 문제 설명 예시를 보니까 한번 선택했던거는 다시 선택하지 않고 진행방향으로만 실행되는 것에서 idea를 얻었다.

"""
# for i in range(n):
#     for j in range(i+1,n):
#         if data[i] !=data[j]:
#             count +=1
#         else:
#             pass
# print(count)

# end_time = time.time()
# print('수행시간 :',end_time - start_time) 



# 책 풀이 # 로직을 이해못하겠음

n,m= 5,3
data= [1,3,2,3,2]

array=[0]*11
for i in data:
    array[i]+=1
    
result = 0
for i in range(1, m+1):
    n-=array[i]
    result += array[i] * n
print(result)

