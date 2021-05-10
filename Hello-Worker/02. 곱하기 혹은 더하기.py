S = list(input())
answer = int(S[0])
for i in range(1,len(S)): #둘째 자리부터 시작해 전체 자릿수-1만큼 반복
    if int(S[i]) <= 1 or answer <= 1: # i=1부터 시작이므로 둘째자리부터 반복,
        answer += int(S[i]) #0이거나 1이면 더해라.
    else:
        answer *= int(S[i]) #아니면 곱해라

print(answer)

