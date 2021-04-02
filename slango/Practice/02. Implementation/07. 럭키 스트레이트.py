# 2nd try:
def luc():
    tmpstr = input()
    lft = tmpstr[:int(len(tmpstr)/2)]
    rgt = tmpstr[int(len(tmpstr)/2):]

    lftnums=list(map(int, lft))
    rgtnums=list(map(int, rgt))

    if sum(lftnums)==sum(rgtnums):
        print("LUCKY")
    else:
        print("READY")

luc()









# # 1st try:
# def luc_str():
#     N = input("N:")
    
#     # 어차피 짝수 길이로 N을 입력받음, 따라서 절반으로 나눌 수 있다.
#     leng = len(N)//2
#     str_l = N[:leng] # 왼쪽 문자열
#     str_r = N[leng:] # 오른쪽 문자열
    
#     sum_l = 0 # 왼쪽 문자열 합
#     sum_r = 0 # 오른쪽 문자열 합
#     # 각각의 문자열 내 숫자를 더하는 과정
#     for i in str_l:
#         sum_l += int(i)
#     for i in str_r:
#         sum_r += int(i)
        
#     # 만약 합이 같다면 럭키, 아니면 레디
#     if sum_l == sum_r:
#         return 'LUCKY'
#     else:
#         return 'READY'