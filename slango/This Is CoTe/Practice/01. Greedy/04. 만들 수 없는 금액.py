# 의사코드
# - 1. 리스트 받아 소팅
# - 2. 1원부터 리스트로 만들어 보면서 while문 진행
# - 3. 만들 수 있으면 break

def imposPrice():
    N = int(input("N:"))
    lst = list(map(int,input("Coins:").split()))
    
    lst.sort()
    lstlen = len(lst)
    
    # 2진수
    max2jin = 2**lstlen
#     3 2 1 1 9
#     1 -> 00001 -> 9
#     2 -> 00010 -> 1
#     3 ->
    
#     32 -> 
    sum_lst = []
    
    #발생가능한 모든 비트에 모든 합 구해 'sum_lst'에 넣기
    for i in range(1,max2jin+1):
        now_bit = bin(i)[2:]     # 비트는 '0bxxx'형식이라 자르고 비트생성
        now_sum = 0
        # 해당 비트로 더할 수 들을 골라 더한다.
        for j in range(0,len(now_bit)):
            if int(now_bit[j]):
                now_sum += lst[j]
        # 더해진 수를 sum_lst
        sum_lst.append(now_sum)
        
    lst2 = list(set(sum_lst))
    for i in range(1,1000001):
        if not i in lst2:
            return i
    return 1000000
        
#     for i in range(0,len(lst2)-1):
#         if lst2[i]!=lst2[i+1]-1:
#             return lst2[i]+1
#     return lst2[-1]+1
