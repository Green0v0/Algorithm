n, m, k = 5, 8, 3
num = [2,4,5,4,6]

# n= num의 원소 개수
# m = 더할 횟수
# k = 반복가능 횟수
"""
1. a = 반복가능 횟수만큼 가장 큰 숫자를 더한다 
   b = 두번째로 큰수를 1번 더한다.(반복을 끊게 하기위해)
   a+b = 반복될 배열의 원소 개수

2. m을  배열의 원소의 개수로 나눈 몫*k 와  나머지를 더한 숫자가 가장 큰 수가 나오는 횟수 
3. m - 가장 큰 수 나오는 횟수 = 두번째로 큰 숫자가 나오는 횟수 
"""

num.sort()
result = 0

first = num[-1]
second = num[-2]

f = first *(k*(m/(k+1))+(m%(k+1)))
result+=f
s= second*(int(m/(k+1)))
result+=s

print(result)

