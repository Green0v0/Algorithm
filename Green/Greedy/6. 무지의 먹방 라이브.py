# 원형 : %3 해서 2(=len(food_times)-1)가 될 때 인덱스 0으로 돌아감
food_times = [3,1,2]
idx = 0
k = 5
while k != 0:
    print(food_times)
    print('idx',idx)
    print('k',k)
    if food_times == [0]*len(food_times):
        print(-1)
        break # return -1
    # 값이 0이면 다음 리스트로
    if food_times[idx%3] == 0:
        idx+=1
        continue
    else:
        food_times[idx%3] -= 1
        idx += 1
        k -= 1
print(food_times)
print(food_times[idx%3])

# 해답
import heapq

def solution(food_times,k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times)<=k:
        return -1

    # 시간이 작은 음식부터 빼야 함, 우선순위 큐 사용
    q = []
    for i in range(len(food_times)):
        # (음식시간, 음식번호) 형태로 삽입
        heapq.heappush(q,(food_times[i],i+1))
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간

    length = len(food_times) # 남은 음식의 개수
    # sum_value + (현재의 음식시간 - 이전 음식시간) * 현재 음식 개수와 k 비교
    while sum_value+((q[0][0] - previous)*length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous)*length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x : x[1]) # 음식의 번호 기준으로 정렬
    return result[(k-sum_value)%length][1]