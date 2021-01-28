# n = 5
# move = ["R", "R", "R", "U", "D", "D"]
n = int(input())
move = map(str, input().split())

start = [1,1]

for i in move:
    if i == "R":
        start[1] += 1
        if start[1] == n+1:
            start[1] = n
    elif i == "L":
        start[1] -= 1
        if start[1] == 0:
            start[1] = 1
    elif i == "D":
        start[0] += 1
        if start[0] == n+1:
            start[0] = n
    elif i == "U":
        start[0] -= 1
        if start[0] == 0:
            start[0] = 1
print(start)