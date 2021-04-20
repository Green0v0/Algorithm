from itertools import permutations

def solution(n, weak, dist):
    # 예외 상황 외벽의 길이 보다 크거나 같은 친구가 있으면 1반환
    if n <= max(dist):
        return 1

    # weak의 초기길이는 요긴하게 쓰임, dist는 내림차순
    weak_len = len(weak)
    dist.sort(reverse=True)
    
    # weak 2배 늘리기
    tmp = [i+n for i in weak]
    weak.extend(tmp)
    
    # dist 모든 경우의 수 설정 extend를 이용해 2차원으로 만들기
    check_list = []
    for i in range(len(dist)):
        checks = list(permutations(dist[:i], i))
        check_list.extend(checks)
        
    # 완전 탐색
    for checks in check_list: # check_list (4,), (4, 3), (3, 4), ...
        for start_idx in range(weak_len):
            # checks로 못찾았으면 start와 visit 초기화
            start = weak[start_idx]
            visit = [False] * weak_len
            for check in checks: # checks = (4, 3) ....
                # checks의 원소 하나하나 확인
                # 시작값과 친구 이동거리 더해서 끝값 설정
                end = start + check
                for w_idx in range(start_idx, len(weak)):
                    # 시작idx부터 시작하여 효율성 높이기
                    # weak를 전부 확인하기
                    if start <= weak[w_idx] <= end:
                        # start와 end 사이에 있으면 방문체크
                        visit[w_idx%weak_len] = True
                    elif end < weak[w_idx]:
                        # end 보다 높으면 start 재설정 후 다음 친구 ㄱㄱ
                        start = weak[w_idx]
                        break
                    if False not in visit:
                        # 모든 방문이 끝났다면 끝~!
                        return len(checks)
    # 전부 확인했지만 없으면 -1...
    return -1

n = 12
weak = [1,3,4,9,10]
dist = [3,5,7]
print(solution(n, weak, dist))