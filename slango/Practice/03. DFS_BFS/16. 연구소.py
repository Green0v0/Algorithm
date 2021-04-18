N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

answer = 0
now_graph = []

def dfswall(wall):
    if wall < 3:
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    dfswall(wall+1)
                    graph[i][j] = 0
    else:
        global answer
        global now_graph
        now_graph = graph.copy()
        for i in range(N):
            for j in range(M):
                if now_graph[i][j] == 2:
                    dfsvir(i-1, j)
                    dfsvir(i+1, j)
                    dfsvir(i, j-1)
                    dfsvir(i, j+1)
        answer =  max(answer, count0(now_graph))
        

def dfsvir(x, y):
    global now_graph
    if x<= -1 or x>=N or y<=-1 or y>=M:
        return False
    if now_graph[x][y] == 0:
        now_graph[x][y] = 2
        dfsvir(x-1, y)
        dfsvir(x+1, y)
        dfsvir(x, y-1)
        dfsvir(x, y+1)


def count0(graph):
    cnt = 0
    for gra in graph:
        cnt += gra.count(0)
    return cnt
            
    
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