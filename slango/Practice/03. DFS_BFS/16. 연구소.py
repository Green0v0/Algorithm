N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))


def count0(graph):
    cnt = 0
    for gra in graph:
        cnt += gra.count(0)
    return cnt


answer = 0
now_graph = [[0]*M for _ in range(N)]

def dfswall(wall):
    global answer
    if wall < 3:
        for i in range(N):
            for j in range(M):
                 if graph[i][j] == 0:
                    graph[i][j] = 1
                    dfswall(wall+1)
                    graph[i][j] = 0
    else:
        # 깊은 복사
        for i in range(N):
            for j in range(M):
                now_graph[i][j] = graph[i][j]
        for i in range(N):
            for j in range(M):
                if now_graph[i][j] == 2:
                    dfsvir(i-1, j)
                    dfsvir(i+1, j)
                    dfsvir(i, j-1)
                    dfsvir(i, j+1)
        answer =  max(answer, count0(now_graph))
        

def dfsvir(x, y):
    if x in range(N) and y in range(M) and now_graph[x][y] == 0:
        now_graph[x][y] = 2
        dfsvir(x-1, y)
        dfsvir(x+1, y)
        dfsvir(x, y-1)
        dfsvir(x, y+1)
            
    
dfswall(0)

print(answer)

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2

# 8 8
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0