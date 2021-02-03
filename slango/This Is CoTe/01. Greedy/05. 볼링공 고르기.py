# 의사코드
# - 1. 공들을 무게 순으로 소팅
# - 2. 무게가 같은 공들을 한 리스트에 저장, 무게는 1 ~ M 중에 존재
# - 3. 각각의 번호는 모두 다르다. 번호는 1 ~ N 까지 모두 고유하게 부여
#     - ex) 
#     - 무게가 1인 번호list :[1],
#     - 무게가 2인 번호list: [2,5]
#     - 무게가 3인 번회list: [3,4]
# - 5. 여러 무게 중 2개의 리스트를 골라 그중 하나씩 순서대로 선택

def pickball():
    N, M = map(int, (input("N, M:").split()))
    lst = list(map(int, input("weights:").split()))
    
    # 조합 카운트
    cnt = 0
    for i in range(0,len(lst)-1):
        for j in range(i,len(lst)):
            if lst[i]!=lst[j]:
                cnt += 1
                
    print(N,M,cnt)
    return cnt
