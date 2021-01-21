# 주의!! 0, 1은 곱하기보다 더하기!

s = input()
ret = int(s[0]) # 반환값 초기화(s의 첫번째 값)

for i in s[1:]: # 초기화한 값 빼고 반복문
    i = int(i)
    if ret <= 1 or i <= 1: # 0과 1인 경우 (+)
        ret += i
    else: # 나머지는 (*)
        ret *= i
print(ret)

## s = "02184"
## 결과값 = 96
