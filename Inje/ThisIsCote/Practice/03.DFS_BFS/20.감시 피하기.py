import copy

N = int(input())

graph = []
for i in range(N):
    graph.append(list(input().split()))

answer = "NO"
now_graph = [] # 장애물을 채운 후 그래프 복사해오기(깊은 복사)


def dfsesc(x, y, drt):
    global answer, tmp_ans
    if x not in range(N) or y not in range(N) or now_graph[x][y] == 'O':
        return False
    if now_graph[x][y] == 'S':
        tmp_ans = False
        return False

    now_graph[x][y] = 'T'
    if drt == 0:
        dfsesc(x-1, y, 0)
    elif drt == 1:
        dfsesc(x+1, y, 1)
    elif drt == 2:
        dfsesc(x, y-1, 2)
    else:
        dfsesc(x, y+1, 3)
    

def dfs(x, y, cnt):
    global answer, tmp_ans, now_graph
    if cnt >= 3:
        now_graph = copy.deepcopy(graph)
        tmp_ans = True # 지금 이 답이 끝날 때까지 유지된다면 이는 가능한 것.
        for i in range(N):
            for j in range(N):
                # 선생님들 시야를 모두 T로 채우기
                if graph[i][j] == 'T':
                    dfsesc(i-1, j, 0)
                    dfsesc(i+1, j, 1)
                    dfsesc(i, j-1, 2)
                    dfsesc(i, j+1, 3)
        # 끝날 때까지 유지되었다. 즉, 학생들이 숨을 수 있는 방법이 있다
        if tmp_ans: 
            answer = "YES"

    else:
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    dfs(i, j, cnt+1)
                    graph[i][j] = 'X'

dfs(0, 0, 0)

print(answer)