n = 5
cnt = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            # 매 시, 분, 초를 더해줘 문자열로 만들고 그안에 문자열 3이 있는지 확인
            if "3" in str(h) + str(m) + str(s):
                cnt+=1

print(cnt)
