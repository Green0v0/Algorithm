S = list(input())
zero = 0 # 1 2 3
one = 0 # 1 2
for i in range(len(S)-1): #마지막 자리는 필요없음
    if S[i] == '0': # 첫번째자리가 0이면
        zero += 1 # 0그룹 1증가
    if S[i] != S[i+1]: #연속된 숫자가 아니면
        if S[i+1] == '0':
            zero += 1 #0으로 바뀌면 0그룹 1증가
        else:
            one += 1 #1으로 바뀌면 1그룹 1증가

print(min(zero,one))

#0으로 바뀌는 횟수, 1로 바뀌는 횟수
#s = input()
#a = []
#for i in range(len(s) - 1):
#    if s[i + 1] != s[i]:
#        a.append(s[i])
#a.append(s[-1])

#print(min(a.count('1'), a.count('0')))
 # 0 1 0 1 1 => 2