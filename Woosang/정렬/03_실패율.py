from collections import Counter

N = 4
stages = [4,4,4,4,4]
len_stages = len(stages)

# stage의 unique를 key로, 개수를 value저장
unique_cnts = Counter(stages)
result_list = []
for i in range(1, N+1):
    # 값이 있으면
    if i in unique_cnts.keys():
        # 실패율 계산 후 실패율과 stage를 짝으로 result_list에 넣어준다.
        fail_rate = unique_cnts[i] / len_stages
        result_list.append((fail_rate, i))
        # 분모는 줄여주기
        len_stages -= unique_cnts[i]
    # 값이 없으면 0 넣어 주기
    else:
        result_list.append((0, i))
# 실패율로 정렬 같은 경우 stage를 이용해 정렬
result_list.sort(key=lambda x: (-x[0], x[1]))
answer = []
# stage들만 뽑아주기
for i in result_list:
    answer.append(i[1])

print(answer)

# -------------------------------------------------------------

from collections import Counter

def solution(N, stages):
    len_stages = len(stages)
    unique_cnts = Counter(stages)
    result_list = []
    for i in range(1, N+1):
        if i in unique_cnts.keys():
            fail_rate = unique_cnts[i] / len_stages
            len_stages -= unique_cnts[i]
            result_list.append((fail_rate, i))
        else:
            result_list.append((0, i))
    result_list.sort(key=lambda x: (-x[0], x[1]))
    
    answer = []
    for i in result_list:
        answer.append(i[1])
    
    return answer

#-----------------------------------------
def solution1(N, stages):
    result = {}
    len_stages = len(stages)
    for stage in range(1, N+1):
        if len_stages:
            cnt = stages.count(stage)
            result[stage] = cnt / len_stages
            len_stages -= cnt
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution1(N, stages))