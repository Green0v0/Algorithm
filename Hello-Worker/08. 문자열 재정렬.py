# S = list(input())
# A = [] #문자열
# B = 0 #숫자형
#
# for i in range(len(S)):
#     if str(S[i]) == str(0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
#         B += int(S[i])
#     else:
#         A.append(S[i])
#
# A.sort()
# A.append(str(B))
# print(A)

S = input()
result = []
num = 0

for i in S:
    if i.isalpha(): #알파벳인 경우 리스트 삽입
        result.append(i)
    else:
        num += int(i)

# 알파벳 정렬
result.sort()

if num != 0:
    result.append(str(num)) #0이 아닌경우 num을 가장 뒤에 삽입

# 리스트를 문자열로 변환하여 출력
print(''.join(result))