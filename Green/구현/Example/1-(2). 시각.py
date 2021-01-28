n = int(input())
clock = [0,0,0]
cnt = 0
while True:
    if clock[0] == n and clock[1] == 59 and clock[2] == 59:
        break
    clock[2]+=1
    if clock[2] == 60:
        clock[2] = 0
        clock[1] += 1
        if clock[1] == 60:
            clock[1] = 0
            clock[0] += 1
    str_clock = list(map(str,clock))
    for i in str_clock:
        if '3' in i:
            cnt+=1
            break
print(cnt)
# 완전탐색
# 3중 for문
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
