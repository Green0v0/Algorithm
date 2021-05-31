# def solutions(food_times, k):
#     s = food_times.sort() #전체적으로 한바퀴 도는 회전수를 세기 위해 음식양 오름차순 정렬
#     l = len(food_times) #요소 개수 세어줌
#     time = 0 #먹는시간 (먹은 음식의 개수)
#
#     if sum(food_times) < k: #총 음식시간의 합 < 전체 시간
#         return -1
#
#     for i in s:
#         if i != 0 :
#             for j in i:
#                 time += 1 #총 음식 시간
#     last_time = time - k
#
# print(solutions([3, 1, 2], 5))


def solution(food_times, k):
    food_times_list = []
    totalTime = 0

    # 음식의 번호와 음식의 양을 저장
    for i in range(0, len(food_times)):
        food_times_list.append([i, food_times[i]])
        totalTime += food_times[i]

    # 전체 먹는 시간보다 k가 크면 계산 불가능 이므로 -1
    if totalTime <= k:
        return -1
    # 음식 양이 적은 순으로 정렬
    # key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.
    # c = sorted(a, key=lambda x: x[0])
    # c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
    food_times_list.sort(key=lambda x: x[1]) #1번째 인덱스 음식 양순으로 정렬

    # 제일 적은 음식을 길이에 곱한 시간 계산
    delTime = food_times_list[0][1] * len(food_times_list)
    # i 사라진 음식의 개수
    i = 1
    # k 가 음식을 사라지게 하는 수보다 클 경우 아래 의 반복문 실행
    while delTime < k: # 전체적으로 삭제되는양 < k
        k -= delTime # k = k-delTime 전체 바퀴돌고 남은시간
        delTime = (food_times_list[i][1] - food_times_list[i - 1][1]) * (len(food_times_list) - i)
        i += 1 ######################
    # 인덱스 수순으로 배치
    food_times_list = sorted(food_times_list[i - 1:], key=lambda x: x[0])
    # k번쨰 음식의 인덱스를 출력
    return food_times_list[k % len(food_times_list)][0] + 1


print(solution([3, 1, 2], 5))


