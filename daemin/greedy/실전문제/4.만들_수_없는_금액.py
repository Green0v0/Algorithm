n=5
coin= [5,4,2,1,9]

# n = int(input()) 
# coin = list(map(int, input().split()))
"""
아이디어
target 금액은 1부터 시작하고 화폐 단위는 오름차순 정렬을 수행한다.(coin에 1이없다면 최소단위가 1이다.)
화폐단위를 순차적으로 검사하면서 만약 target보다 단위가 작을 경우 해당 target은 만들 수 있다.
target을 만들 수 있을 경우, 다음 target은 해당 화폐단위를 더한 값으로 갱신한다.
target보다 큰 값이 검사 단위로 주어질 경우 해당 target은 만들지 못한다고 판단되어 그때의 target이 답으로 출력한다.
핵심은 target 이하의 값은 모두 만들 수 있다고 정의(가정?)하는 것이었다.
화폐 단위가 작은 동전부터 하나씩 확인하면서 target을 증가시키고 가장 작은 target 값을 찾아가기 때문에 그리디 알고리즘으로 분류된다.
"""


coin.sort()
target = 1
for c in coin:
    if c <= target:
        target+=c
    else:
        break
print(target)
            