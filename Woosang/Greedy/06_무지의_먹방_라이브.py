"""
딕셔너리를 이용한 풀이
- idx를 values에 붙여주고 value가 0인 친구들 지워가며 비교
결과 : **시간 초과**
딕셔너리를 반복문 돌리는 중 길이가 변환되는 함수 사용할 수 없다.
"""
def solution(food_times, k):
    dict_ft = {k:v for k, v in enumerate(food_times, 1)} # idx 달아주기
    while True:
        for i in dict_ft.keys(): # 키 값 반복문 돌리기
            dict_ft[i] -= 1
            k -= 1
            if k == -1: # 정전 발생 이후 이기 때문에 -1값
                return i
        dict_ft = {k:v for k,v in dict_ft.items() if v != 0}
        # 딕셔너리는 반복문 도중 변환이 있으면 에러가 나기때문에
        # comprehension으로 0을 제외하며 재정의
        
"""
입력값 = [3, 1, 2], 5
출력값 = 1
"""

"""
heapq 함수를 이용한 풀이
- food_times를 heapq을 이용해 (value, idx)형식의 튜플로 묶어 리스트(h)에 넣는다.

- 반복문을 k 가 0보다 크거나 같을때 까지만 돌린다.
    - 리스트(h) 안에 최소값(cur)을 빼내 남은 음식들 길이(n)랑 곱한 후 k-=1 한다.
    - 최소값(cur)으로 리스트를 한바퀴를 돌면 최소값은 없어지므로 배열의 길이(n)-=1
    - 변수(last_food)에 최소값(cur)을 대입한다.
    - 다음 최소값(cur)은 이전의 최소값(last_food)을 빼서 위에 과정을 반복한다.

- 리스트(h)를 idx값으로 정렬을 해준다.
"""
import heapq

def solution(food_times, k):
    h = []
    for i in range(len(food_times)): # heapq정렬 [(food_times의 값, idx),...]정의
        heapq.heappush(h, (food_times[i], i+1))

    n = len(food_times)
    last_food = 0 # 다음은 음식을 매순간 빼주는 것보다 다음 최솟값이랑 빼서 계산
    while k - (h[0][0] - last_food) * n >= 0: # 최솟값 배열 한바퀴 돌아 최솟값*배열의길이 - k한다.
        cur = heapq.heappop(h)[0]
        k -= (cur - last_food) * n
        n -= 1
        last_food = cur

    h.sort(key=lambda x: x[1])
    return h[k%n][1]
"""
결과값 : 1
"""

