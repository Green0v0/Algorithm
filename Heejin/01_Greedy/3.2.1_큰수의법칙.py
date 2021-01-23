'''
- n : 배열의 크기 
- m : 숫자가 더해지는 횟수 
- k : 연속해서 더하기 가능 한 갯수
'''

# 공백으로 구분하여 입력 받기 
n, m, k = map(int,input().split()) 

# n개의 수를 공백으로 구분해서 입력받기 
# # check : n 개 입력 제한해서 받기는?
data = list(map(int, input().split()))

#입력받은 수들 정렬한 후, 가장 큰수와 두번째 큰 수 구별하기 
data.sort() 
first = data[n-1] # 가장 큰 수 
second = data[n-2] # 가장 작은 수 

result = 0 

while True : 
    for _ in range(k) : # 가장 큰 수 k번 더하기 
        if m == 0 : 
            break 
        result += first 
        m -= 1 
    if m == 0 : 
        break 
    result += second 
    m -= 1 

print(result)
