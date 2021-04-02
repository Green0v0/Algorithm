# 2nd try:
def reorg(strr):
    alp = []
    num = 0
    for let in strr:
        if let.isalpha():
            alp.append(let)
        else:
            num += int(let)
    alp.sort()
    alp = ''.join(alp)

    return alp+str(num)

# strr = 'K1KA5CB7'
strr = 'AJKDLSI412K4JSJ9D'
print(reorg(strr))







# # 1st try:
# # 문자열 재정렬
# def re_str():
#     # 하나의 문자열 S로 입력받는다
#     S = input("input S:")
#     # 알파벳만 따로 저장할 공간
#     alphas = strs = ''
#     # 숫자는 따로 더할 공간
#     sums = 0
    
#     for i in S:
#         # 알파벳이라면 alpha에 더하기
#         if i.isalpha():
#             alphas += i
#         # 숫자라면 그냥 바로 덧셈
#         else:
#             sums += int(i)
#     # 알파벳들은 순서 정렬
#     alphas=sorted(alphas)
#     for i in alphas:
#         strs += i
#     return strs+str(sums)