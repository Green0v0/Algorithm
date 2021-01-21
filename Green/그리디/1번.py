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