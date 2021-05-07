N = int(input())
students = []
for _ in range(N):
    student = input().split()
    student[1:] = map(int, student[1:])
    students.append(student)

students.sort(key=lambda x: [-x[1], x[2], -x[3], x[0]])

for i in range(N):
    print(students[i][0])
