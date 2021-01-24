# 8th try:
# def solution(food_times, k):
#     N = len(food_times)
#     # 무지가 먹어야 할 전체 음식량
#     food_sum = sum(food_times)
#     min_fd = min(food_times)
    
#     # [인덱스, 음식량] 을 원소로 리스트 생성
#     lftfd_lst = []
#     for time in enumerate(food_times):
#         lftfd_lst.append(list(time))
#     # 음식량 순서대로 정렬
#     lftfd_lst = sorted(lftfd_lst, key = lambda x: x[1])
#     print(lftfd_lst)
    
#     # 효율성을 위해 음식량이 에러발생시간 이전에 끝나는 경우는 -1 리턴하고 제외
#     # 음식량이 그 시간 이후인 경우만 계산
#     if food_sum > k:
        
#         now_fd = 0
#         last_idx = 0
        
#         for i in lftfd_lst:
#             print("for k:", k, "now_idx:",lftfd_lst.index(i), "food:",i[1])
#             if k < (N-lftfd_lst.index(i)) * (i[1] - now_fd):
#                 last_idx = lftfd_lst.index(i)
#                 break
#             if i[1] == now_fd:
#                 continue
# #             lftfd_lst.index(i)< N-1 and i[1] == lftfd_lst[lftfd_lst.index(i) + 1][1]:
# #                 continue
#             k -= (N-lftfd_lst.index(i)) * (i[1] - now_fd)
#             now_fd = i[1]
#             last_idx = lftfd_lst.index(i)
#         print("afterfor, k:", k, "now last_idx:",last_idx, "food:",i[1])
        
#         lftfd_lst = lftfd_lst[last_idx:]
#         print(last_idx, k, lftfd_lst)
        
#         lftfd_lst = sorted(lftfd_lst)
#         print(lftfd_lst)
        
#         return lftfd_lst[k % len(lftfd_lst)][0] + 1
#     else:
#         return -1









# 7th try:
# def solution(food_times, k):
#     N = len(food_times)
#     # 무지가 먹어야 할 전체 음식량
#     food_sum = sum(food_times)
#     min_fd = min(food_times)
    
#     # [인덱스, 음식량] 을 원소로 리스트 생성
#     lftfd_lst = []
#     for time in enumerate(food_times):
#         lftfd_lst.append(list(time))
#     # 음식량 순서대로 정렬
#     lftfd_lst = sorted(lftfd_lst, key = lambda x: x[1])
#     print(lftfd_lst)
    
#     # 효율성을 위해 음식량이 에러발생시간 이전에 끝나는 경우는 -1 리턴하고 제외
#     # 음식량이 그 시간 이후인 경우만 계산
#     if food_sum > k:
#         idx = 0
#         now_fd = 0
#         tmp_N = N
#         for i in lftfd_lst:
#             print("for", k, tmp_N, i[1])
#             if k < tmp_N * (i[1] - now_fd):
#                 break
#             k -= tmp_N * (i[1] - now_fd)
#             now_fd = i[1]
#             idx += 1
#             while idx < len(lftfd_lst) - 1 and i[1] == lftfd_lst[idx + 1][1]:
#                 idx += 1
#             tmp_N = N - idx
#         print("afterwhile", idx, k, lftfd_lst)
        
#         # 모든 원소를 위에서 k를 깎은만큼 같이 깎자
# #         fir_fd = lftfd_lst[0][1]
#         # print('decrease fd',fir_fd)
#         # 무조건깎아야되는지 확인!
# #         for i in range(len(lftfd_lst)):
# #             lftfd_lst[i][1] -= fir_fd
        
# #         while True:
# #             if lftfd_lst[0][1]<=0:
# #                 lftfd_lst.pop(0)
# #             else:
# #                 break
#         lftfd_lst = lftfd_lst[idx:]
#         print(idx, k, lftfd_lst)
#         lftfd_lst = sorted(lftfd_lst)    
#         print(lftfd_lst)
        
#         return lftfd_lst[k % len(lftfd_lst)][0] + 1
#     else:
#         return -1








# 6th try:
#         # 각 반복에서 제일 적은(맨 앞의) 음식량를 저장하면서
#         # (제일 적은 음식량 * 남은 전체 음식 종류 수) 만큼
#         # 시간 k도 줄이고 음식량도 동일하게 줄인다
#         nowtot_food = 0
#         while True:
#             # 언제까지? sum보다  작아질 때까지, 즉 k가 더 작아지면 중단
#             if food_sum < N * lftfd_lst[0][1]:
#                 print("2:",food_sum, lftfd_lst[0][1])
#                 break
#             nowtot_food += lftfd_lst[0][1]
#             food_sum -= N * nowtot_food
#             print("1:",food_sum, lftfd_lst[0][1])
#             k = food_sum
#             lftfd_lst.pop(0)
#             N -= 1
            
#         print("now:",nowtot_food)
#         for i in range(len(lftfd_lst)):
#             lftfd_lst[i][1] -= nowtot_food
#         print("2:",len(lftfd_lst),lftfd_lst, k, food_sum)
        
#         return lftfd_lst[ k % len(lftfd_lst)][0] + 1









# 5th try:

# def solution(food_times, k):
#     N = len(food_times)
#     # 무지가 먹어야 할 전체 음식량
#     food_sum = sum(food_times)
#     min_fd = min(food_times)
#     lftfd_lst = []
#     for time in enumerate(food_times):
#         lftfd_lst.append(list(time))
    
#     # 효율성을 위해 음식량이 에러발생시간 이전에 끝나는 경우는 -1 리턴하고 제외
#     # 음식량이 그 시간 이후인 경우만 계산
#     if food_sum > k:
#         # 언제? k가 (가장 적은 음식 * 전체 음식 개수) 이상일 동안
#         while k>=min_fd*len(lftfd_lst):
#             # 효율성을 위해 하나씩 비교하지 않고 전체중에서 가장 적은 음식을 
#             # 전 인덱스에서 공통적으로 빼면서 반복
#             k -= min_fd * len(lftfd_lst)
#             for idx in range(len(lftfd_lst)):
#                 lftfd_lst[idx][1] -= min_fd
#             # 또한 효율성을 위하여 남은 음식이 없는 음식은 리스트에서 제거
#             idx2 = 0
#             while idx2<len(lftfd_lst):
#                 if not lftfd_lst[idx2][1]:
#                     lftfd_lst.pop(idx2)
#                 else:
#                     idx2 += 1
#             # 제일 적은 음식 업데이트
#             print(lftfd_lst)
#             for i in lftfd_lst:
#                 min_fd = min(min_fd,i[1])
#             print(min_fd)
        
#         print(lftfd_lst, 'k: ',k)
#         return lftfd_lst[k%len(lftfd_lst)][0] + 1
    
#     else:
#         return -1











#         4th try:
#         lftfd_lst = []
#         for times in enumerate(food_times):
#             lftfd_lst.append(list(times))
        
#         # iteration 작업
#         idx = 0
#         while k:
#             lftfd_lst[idx][1] -= 1
#             if not lftfd_lst[idx][1]:
#                 lftfd_lst.pop(idx)
#                 N -= 1
#             else:
#                 idx += 1
#             if idx>=N:
#                 idx = 0
                
#             k -= 1
#             print(lftfd_lst)
            
#         return lftfd_lst[idx][0] + 1







# 3rd Try
# def solution(food_times, k):
    N = len(food_times)
    # 무지가 먹어야 할 전체 음식량
    food_sum = sum(food_times)
    
    # 효율성을 위해 음식량이 에러발생시간 이전에 끝나는 경우는 -1 리턴하고 제외
    # 음식량이 그 시간 이후인 경우만 계산
    if food_sum > k:
        idx = 0
        
        while k:
            food_times[idx] -= 1
            idx = (idx + 1) % N
            while not food_times[idx]:
                idx = (idx + 1) % N
            k -= 1
            print(food_times, idx, k)
            
        return idx + 1
    else:
        return -1








    
# 2nd try
#         lftfd_lst = []
#         for food_idx, food_left in enumerate(food_times):
#             lftfd_lst.append([food_idx,food_left])
            
#         idx = 0
#         while True:
#             # iteration 작업            
#             lftfd_lst[idx%N][1] -= 1
#             if not lftfd_lst[idx%N][1]:
#                 lftfd_lst.pop(idx%N)
#                 N -= 1
#                 idx %= N
#             else:
#                 idx += 1
                
#             print("먹은후: ",lftfd_lst, idx, N)
            
#             k -= 1
#             if not k:
#                 break
            
#             print("다음 먹을: ",idx, N,'\n')
            
#         return lftfd_lst[idx][0] + 1
