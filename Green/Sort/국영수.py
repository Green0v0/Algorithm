"""
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""
N = int(input())
student = []
for _ in range(N):
    stu = input().split()
    for i in range(4):
        if i != 0:
            stu[i] = int(stu[i])
    student.append(stu)

# 국어 영어 수학
student.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for n, k, e, m, ascii_cord in student:
    print(n)

# 다른 사람 방법
N = int(input())
score_list = []
for i in range(N):
    [name, kor, eng, math] = map(str, input().split())
    score_list.append([name, int(kor), int(eng), int(math)])

sorted_score_list = sorted(score_list, key=lambda x : (-x[1], x[2], -x[3], x[0]))

for score in sorted_score_list:
    print(score[0])
