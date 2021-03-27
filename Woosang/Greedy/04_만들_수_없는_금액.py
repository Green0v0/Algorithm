from itertools import combinations

n = 5
coins = [3, 2, 1, 1, 9]

add_set = set(coins) # 중복 제외
x = 2 # n개까지 모든 조합
while x != n:
    # 모든 조합을 만들어 비교(완전탐색)
    for i in set(combinations(coins, x)): 
        add_set.add(sum(i))
    x += 1

# 가장 적은 숫자 반환
for i in range(1, max(add_set)):
    if i not in add_set:
        answer = i
        break

print(answer)

# 답안 풀이 
"""
이제 만들 수를 target이라 가정한다.
동전들을 오름차순으로 정렬한 후 낮은 금액 부터 target과 비교한다.
만약 target보다 비교하는 금액이 큰 경우는 만들 수 없는 금액이다
else면 만들 수 있음 target에 비교한 수를 더해 업데이트
"""
n = 5
coins = [3, 2, 1, 1, 9]

coins.sort() # 오름차순으로 한개씩 비교
target = 1 # 만들 수

for coin in coins:
  # 만들 수 보다 비교할 금액이 크면 더 이상 못 만듬
  if target < coin:
    break
  target += coin

print(target)
