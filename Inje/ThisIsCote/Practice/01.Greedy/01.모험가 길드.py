# 의사코드
# 1. 리스트 입력
# 2. 모험가의 공포도 순서대로 소팅
# 3. 공포도 큰 모험가부터 그룹 생성
#     - 공포도=그룹의 인원 결정
#     - 완벽히 모든 그룹이 생성된 후 cnt 변수로 그룹 수 임시저장
#     - max 함수로 cnt의 최대값을 매번 업데이트
# 4. cnt 최대값 리턴

def Adventer():
    N=int(input())
    lst=list(map(int,input().split()))
#     lst.sort(reverse=True)
#     print(lst)
    
#     N 전체인원
#     lst 2 3 1 2 2  1,2,2,2,3
    idx=0
    while True:
        N-=lst[idx]
        if N<=0:
            break
        idx+=1
        
        ## 수정필요
    print(idx)
