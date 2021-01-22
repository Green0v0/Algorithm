n, m = map(int, input().split())
li = []
min_li=[]
for i in range(n):
    li.append(list(map(int, input().split())))
for j in li:
    min_li.append(min(j))
print(max(min_li))