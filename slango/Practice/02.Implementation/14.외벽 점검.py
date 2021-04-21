# 포인트: weak와 dist의 길이가 짧으므로 완전 탐색 가능
def solution(n, weak, dist):
    # # 그냥 dist 만큼의 길이의 원호들을 링에 채워넣어가며 비교한다고 생각하면 될듯
    # for wea in weak:

    length = len(weak)
    # weak의 길이를 2배로 늘려 원형을 일자형태로 변형
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist)+1 # min함수로 업데이트하기 위해 최대값+1로 초기화

    # 모든 점을 시작점으로 설정
    for start in range(length):
        # 친구를 차례로 줄지은 경우 모두 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count-1]
            for index in range(start, start+length):
                if position < weak[index]: # 친구가 갈 수 있는 거리보다 포인트가 더 멀다면
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1

    return answer


n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]
solution(n, weak, dist)


# # 2nd try: 가장 긴 거리의 친구만 고려
# def solution(n, weak, dist):
#     answer = 0
#     dist.sort(reverse=True)

#     def get_dis(x, y):
#         return (y-x)%n

#     vstd = [False]*len(weak)
#     for dis in dist:
#         cnt_lst = [[0,0,i] for i in range(len(weak))]
#         for i in range(len(weak)):
#             for j in range(1,len(weak)):
#                 next_i = (i+j)%len(weak)
#                 if get_dis(weak[i], weak[next_i])<=dis:
#                     cnt_lst[i][0] += 1
#                     # 뒷 요소에는 최대의 거리 업데이트하여 거리가 큰 것부터 사용될 수 있도록
#                     cnt_lst[i][1] = max(cnt_lst[i][1], get_dis(weak[i], weak[next_i]))
        
#         cnt_lst.sort(key=lambda x: -x[1])
#         to_pop_idx = cnt_lst[0][2]
#         for i in range(cnt_lst[to_pop_idx][0]):
#             vstd[(to_pop_idx+i)%n] = True
        
#         answer += 1
#         if sum(vstd)==n:
#             return answer

#     return -1





# # 1st try:
# def solution(n, weak, dist):
#     answer = 0

#     dist.sort(reverse=True)

#     def getdist(a,b):
#         return abs(a-b)%(n//2)

#     dis_lst = []
#     for i in range(len(weak)):
#         for j in range(i+1, len(weak)):
#             dis_lst.append((i, j, getdist(weak[i], weak[j])))
    
#     dis_lst.sort(key=lambda x: x[-1])
#     while dis_lst[-1] > dist[0]:
#         dis_lst.pop()
    
#     while dist and dis_lst:



#     if not 
#     return answer