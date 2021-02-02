# 모험가 길드
# 큰 순서대로 sort
# 공포도가 큰 순서대로 그룹 생성
#   - 공포도를 새로운 변수에 집어넣어 횟수로 카운트
N = int(input())
nlist = list(map(int,input().split()))
nlist.sort(reverse=True)
group = 0
cnt = 0
for i in range(N):
    if cnt == 0:
        cnt = nlist[i]
        group += 1
    cnt -= 1

print(group)

# 공포도가 오름차순으로 정렬되어 있다는 점에서 항상 최소한의 모험가의 수만 포함하여 그룹을 결정하게 된다.
# 즉, 최대한 많은 그룹이 구성되는 방법
n = int(input())
data = list(map(int,input().split()))
data.sort()
result = 0 # 총 그룹수
count = 0 # 모험가의 수
for i in data:
    count+=1
    if count >= i:
        result += 1
        count = 0
print(result)