from collections import deque

n,m = map(int,input().split(' '))
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split(' '))))
print(graph)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
 
