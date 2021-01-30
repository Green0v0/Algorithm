from collections import deque
# 90도 회전하는 함수
def rotation(key): # key: list
    total = []
    for i in range(len(key)):
        result = []
        for j in range(len(key)-1,-1,-1): # 90도 회전이기에 역순으로
            result.append(key[j][i])
        total.append(result)
    return total

# 4방향으로 움직이는 함수
# 이동시 나머지 칸은 빈칸으로 채우기
def moveup(key,m):
    dq = deque(key)
    dq.popleft()
    dq.append([0 for _ in range(m)])
    return dq
def movedown(key,m):
    dq = deque(key)
    dq.pop()
    dq.appendleft([0 for _ in range(m)])
    return dq
def moveleft(key,m):
    global dq
    for i in range(m):
        dq[i].popleft()
        # dq

def moveright(key,m):
    pass

def solution(key,lock):
    m = len(key[1]) # 길이 변수
    dq = deque(key)

    pass

solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]])