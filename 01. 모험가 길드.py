N = input()
X = sorted(list(map(int, input().split())))
group = 0
group_num = 0

for i in X:
    group += 1 # 공포도를 하나씩 호출하며 그룹 인원수 증가
    if i <= group : # 공포도<=그룹에 속한 인원수
        group_num += 1 # 총 그룹수 +1 => 그룹화를 의미
        group = 0 #새로운 그룹화를 통해 그룹내 인원 0으로 초기화

print(group_num)