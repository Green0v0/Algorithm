# 문제 파악
# 1. 적게 뒤집어야 한다 무적권.
# 2. 뒤집는 횟수가 적으려면 0이나 1중에 갯수가 적은거?
# 3. 아니면 연속된 수를 하나의 묶음으로 봤을때 그 묶음수가 적은거?
# 4. 3번 같다.

# 의사코드
# 1. 총 묶음의 수를 센다
#     - 셀 수의 종류는 0,1 두가지뿐이므로 cnt할 cnt=[0,0] 만들기
#     - 각 자리의 숫자를 현재 저장된 수와 비교할 수 있게할 하나의 변수 now_num

def revesrt():
    lst=input()
    now_num=lst[0]
    cnt=[0,0]
    
    for i in range(1,len(lst)):
        if now_num!=lst[i]:
            now_str=lst[i]
            =int(now_str)
            cnt[now_soo]+=1
            cnt[1]+=1
            cnt[0]
        
    if cnt[0]<cnt[1]:
        print(cnt[0])
    else:
        print(cnt[1])
