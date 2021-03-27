# 25 5
n,k = 10,3

count= 0
while True:
    target =(n//k)*k   #몫이랑 k 를 곱하면 k의 배수  n이 1이되면 target == 0 이된다.
    count += (n - target) #  n-target = -1 씩 빼야할 (count)횟수 / -1씩 해야할 횟수
    n = target            # n 을  k 의 배수로 바꿈

    if n < k:
        break
    count +=1
    n//=k
#n < k 가 되면 그때는 -1씩 계속 빼줘야함.// 
count += (n-1)  # n-1을 하면 -1씩 해줘야 하는 횟수를 구할 수 있으니까 그것을 count에 더하고 끝냄/
print(count)




#-------내 풀이----------------------------
# count = 0
# while True:
#     if n%k == 0:
#         n = n//k
#         count +=1
#     elif (n>1) & (n%k != 0):
#         n =n-1
#         count+=1
#     elif n == 1 :
#         print(count)
#         break
#-------------------------------------------------




# 같은 아이디어로 해결한 책에 있는 풀이
# count =0
# while n >k:
#     while n % k !=0:
#         n-=1
#         count+=1
#     n//=k
#     count+=1

# while n > 1 : # n이 1이면 반복문 실행안함
#     n-=1
#     count+=1
    
# print(count)

    