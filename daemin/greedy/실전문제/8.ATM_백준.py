n=5
data=[3, 1, 4, 3, 2]
# runtime error


# n= int (input())
# data = list(map(int,input().split(" ")))
data.sort()
minute=[data[0]]

for i in range(0,len(data)-1):
    minute.append(minute[i]+data[i+1])
print(sum(minute))

