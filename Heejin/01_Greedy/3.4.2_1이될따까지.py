n, k = map(int,input().split())
result = 0 

while True : 
    # n == k 로 나누어 떨어지는 수 가 될때까지 1씩 빼기 
    target = (n//k) * k 
    result += (n - target)
    n = target 

    #n k보다 작을때 (더이상 나눌 수 없을떼) 반복문 탈출
    if n < k :
        break 

    #k로 나누기 
    result += 1 
    n //= k 

# 마지막으로 남은 수에 대하여 1씩 빼기 
result += (n-1)
print(result)
