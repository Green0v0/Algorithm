import math

def solution(s):
    tmp_ansrs = []
    
    for i in range(1,len(s)+1):
        tmp_ans = 0
        split_lst=[s[i*j:i*(j+1)] for j in range(math.ceil(len(s)/i))]
        
        now_tok = ''
        cnt = 1
        for j in split_lst:
            if now_tok != j:
                if cnt >= 1000:
                    tmp_ans += 4
                elif cnt >= 100:
                    tmp_ans += 3
                elif cnt >= 10:
                    tmp_ans += 2
                elif cnt > 1:
                    tmp_ans += 1
                cnt = 1
                tmp_ans += len(now_tok)
                now_tok = j
            else:
                cnt += 1
        
        if cnt >= 1000:
            tmp_ans += 4
        elif cnt >= 100:
            tmp_ans += 3
        elif cnt >= 10:
            tmp_ans += 2
        elif cnt > 1:
            tmp_ans += 1
        tmp_ans += len(now_tok)
        
        tmp_ansrs.append(tmp_ans)
        
    tmp_ansrs=sorted(tmp_ansrs)
    return tmp_ansrs[0]
