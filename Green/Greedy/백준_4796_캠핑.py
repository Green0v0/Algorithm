# P일 중 L일 동안 사용 가능 V일의 휴가
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    # 연속 사용 일
    n = v // p
    answer = (n * l) +(v - ((v//p)*p))
    # if answer > 0:
        # print(answer)
    print(answer)