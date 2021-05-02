def solution(n, weak, dist):
    answer = 0
    dist.sort(reverse=True)
    chk = [False] * n

    def get_dis(a, b):
        return abs(a-b)%int(n/2)

    for dis in dist:
        cnt = [0] * len(weak)
        for i in range(len(weak)):
            for j in range(i+1,len(weak)):
                if get_dis(weak[i], weak[j])<=dis and not chk[i] and not chk[i]:
                    cnt[i]+=1
        max_cnt_idx = cnt.index(max(cnt))
        chk[max_cnt_idx] = True
        answer += 1
        for i in range(len(weak)):
            if i!=max_cnt_idx and get_dis(weak[i], weak[max_cnt_idx])<dis:
                chk[i] = True
        if sum(chk)>=len(weak):
            break
    
    return answer

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))