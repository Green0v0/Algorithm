# 문자열 뒤집기
# 조건: 뒤짚으려면 연속된 하나 이상의 숫자를 잡고 모두 뒤짚는 것
# 숫자가 달라질 때를 count 하고 -1 하면 뒤짚는 횟수
#   - 예외조건: count 1번일 때는 -1하면 0이지만 뒤집는 횟수는 1번
s = input().rstrip()
# 직전 숫자를 저장할 변수
pa = s[0]
# 변할 때 count하는 변수
cnt = 0
for i in s:
    if pa != i:
        cnt += 1
    pa = i
if cnt > 2:
    # return
    print((cnt+1)//2) # 3,4일때 2번 뒤집, 5,6일때 3번 뒤집음
elif cnt == 2 or cnt == 1:
    print(1)
else:
    print(0)