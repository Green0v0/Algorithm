# 2nd try:
def solution(s):
    answer = 10000

    for len_now in range(1,len(s)+1):
        now_str = ''
        now_tok = s[:len_now]
        cnt = 1

        for i in range(len_now,len(s),len_now):
            if now_tok != s[i:i+len_now]:
                if cnt != 1:
                    now_str += str(cnt)
                now_str += now_tok
                now_tok = s[i:i+len_now]
                cnt = 1
            else:
                cnt += 1
                
        if cnt != 1:
            now_str += str(cnt)
        now_str += now_tok
        
        # answer에 전체 길이들을 append해서 min으로 하는 것보다는
        # 최소값은 그때그때 update하는 것이 메모리 상으로 효율적
        answer = min(answer, len(now_str))

    return answer

# s = "aabbaccc"
s = "abcabcdede"
print(solution(s))




# # 1st try:
# import math

# def solution(s):
#     tmp_ansrs = []
    
#     for i in range(1,len(s)+1):
#         tmp_ans = 0
#         split_lst=[s[i*j:i*(j+1)] for j in range(math.ceil(len(s)/i))]
        
#         now_tok = ''
#         cnt = 1
#         for j in split_lst:
#             if now_tok != j:
#                 if cnt >= 1000:
#                     tmp_ans += 4
#                 elif cnt >= 100:
#                     tmp_ans += 3
#                 elif cnt >= 10:
#                     tmp_ans += 2
#                 elif cnt > 1:
#                     tmp_ans += 1
#                 cnt = 1
#                 tmp_ans += len(now_tok)
#                 now_tok = j
#             else:
#                 cnt += 1
        
#         if cnt >= 1000:
#             tmp_ans += 4
#         elif cnt >= 100:
#             tmp_ans += 3
#         elif cnt >= 10:
#             tmp_ans += 2
#         elif cnt > 1:
#             tmp_ans += 1
#         tmp_ans += len(now_tok)
        
#         tmp_ansrs.append(tmp_ans)
        
#     tmp_ansrs=sorted(tmp_ansrs)
#     return tmp_ansrs[0]