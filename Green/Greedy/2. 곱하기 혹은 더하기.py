# 곱하기 혹은 더하기
# 0 or 1 은 더하기
# 그 외에는 곱하기
#   - 앞 뒤를 살펴보고 곱하거나 더하기.
# 즉, 4가지 total 0or1이면 더하기 & 들어온 수가 0or1이면 더하기
s = input().rstrip()
total = 0
for i in s:
    if int(i) == 0 or int(i) == 1 or total == 0 or total == 1:
        total += int(i)
    else:
        total *= int(i)
print(total)

# 풀이
data = input()
result = int(data[0]) # 내 풀이와 다른 점
for i in range(1,len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result+=num
    else:
        result*=num
print(result)