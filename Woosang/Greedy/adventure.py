# 공포도 정렬 후 레벨이 높은 사람을 중심으로 그룹 결성
# 1 == 조커카드

n = int(input())
data = list(map(int, input().split()))

data.sort()
group = [] # or cnt = 0
while len(data):
    member = []
    for _ in range(data[-1]):
        member.append(data.pop()) # data리스트의 -1번 인덱스부터 한명씩 뽑아간다.
        if member[0] == len(member): # 처음 뽑힌 사람 == 공포도(max) == len(member)
            group.append(member) # or cnt += 1
print(len(group))

## n = 5
## data = [2, 3, 1, 2, 2]
## 결과값 [[3,2,2],[2,1]]
## len(ret) == 2