#data =list(input())

data = [0,2,9,8,4]
#data = [5,6,7]
#data = [0,2,4,0,1]

"""
** 제일 중요 P.312
## 0,1이면은 곱하는것보단 더하는게 좋다  0 은 0이되고 1은 그대로기때문에 더하는게 숫자의 크기를 키운다.

1. 0은 더하기를 해도 아무 변화없다. 하지만 곱하기를 하면 0 이되서 최고 큰 수가 될 수 없다.
2. 곱하기는 순서를 어떻게 해도 상관없다.
3. 0을 아예 없앤다. //그리고 나머지 다 곱한다.

"""

# data.sort()

# for i in data:
#     if 0 in data:
#         data.remove(0) # remove는 중간에 껴있는 0을 지우지 못 한다. 그래서 정렬을 해서 0을 앞으로 다빼냈다.
#         data = data

# result = data[0]
# for i in data[1:]:
#     if result == 1 or data[i]==1:
#         result +=i
#     else:
#         result*=i
# print(result)

################################## 책 풀이 ###################################

#data = input()

result = int(data[0])

for i in range(1,len(data)):
    num= int(data[i])
    if num <= 1 or result <=1: # num,result 가 1또는 0일때를 표현함
        result += num
    else:
        result *= num

print(result)



