import sys

n = int(input())
scores = []
for _ in range(n):
    tmp_lst = sys.stdin.readline().rstrip().split()
    name, (kor, eng, math) = tmp_lst[0], map(int, tmp_lst[1:])
    scores.append((name, kor, eng, math))

scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in scores:
    print(i[0])