# 2nd try:
n = int(input())
num_lst = list(map(int, input().split()))
ops = list(map(int, input().split()))

ans_min, ans_max = 999999999, -999999999

result = [0] * n
result[0] = num_lst[0]

def dfs(now):
    if now == n-1:
        global ans_min, ans_max
        ans_min = min(ans_min, result[-1])
        ans_max = max(ans_max, result[-1])
    else:
        for i in range(4):
            if ops[i] > 0:
                ops[i] -= 1
                tmp = result[now+1]
                if i==0:
                    result[now+1] = result[now] + num_lst[now+1]
                elif i==1:
                    result[now+1] = result[now] - num_lst[now+1]
                elif i==2:
                    result[now+1] = result[now] * num_lst[now+1]
                else:
                    if result[now]//num_lst[now+1] >= 0:
                        result[now+1] = result[now] // num_lst[now+1]
                    else:
                        result[now+1] = -(-result[now] // num_lst[now+1])
                dfs(now+1)
                result[now+1] = tmp
                ops[i] += 1

dfs(0)
print(ans_max, ans_min, sep='\n')

# 2
# 5 6
# 0 0 1 0

# 3
# 3 4 5
# 1 0 1 0

# 6
# 1 2 3 4 5 6
# 2 1 1 1






# # 1st try:
# from itertools import permutations

# n = int(input())
# num_lst = list(map(int, input().split()))
# ops = list(map(int, input().split()))

# ans_min, ans_max = 999999999, -999999999

# result = [0] * n
# result[0] = num_lst[0]
# all_ops = []
# # ops에 모든 연산자 넣기
# # [0,0,1,0] => [2]
# # [2,1,1,1] => [0,0,1,2,3]
# for i in range(len(ops)):
#     all_ops.extend([i]*ops[i])

# # 연산자를 순서대로 나열할 수 있는 모든 경우의 리스트 permutation
# ops_permu = list(permutations(all_ops, n-1))
# def dfs(now):
#     if now == n-1:
#         global ans_min, ans_max
#         ans_min = min(ans_min, result[-1])
#         ans_max = max(ans_max, result[-1])
#     else:
#         for now_permu in ops_permu:
#             tmp = result[now+1]
#             if now_permu[now]==0:
#                 result[now+1] = result[now] + num_lst[now+1]
#             elif now_permu[now]==1:
#                 result[now+1] = result[now] - num_lst[now+1]
#             elif now_permu[now]==2:
#                 result[now+1] = result[now] * num_lst[now+1]
#             else:
#                 if result[now]//num_lst[now+1] >= 0:
#                     result[now+1] = result[now] // num_lst[now+1]
#                 else:
#                     result[now+1] = -(-result[now] // num_lst[now+1])
#             dfs(now+1)
#             result[now+1] = tmp