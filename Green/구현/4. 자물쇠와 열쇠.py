from collections import deque

def turn(n, key):
    new_key = []
    row = []

    for i in range(n):
        for j in range(n):
            row.append(key[j][i])
        new_key.append(row[ : : -1])
        row = []

    return new_key

def vert(n, key, k):
    new_key = deque(key)
    add = [0] * n

    if k == 0:
        return new_key
    elif k > 0:
        for i in range(k):
            new_key.pop()
            new_key.appendleft(add)
    else:
        for i in range(abs(k)):
            new_key.popleft()
            new_key.append(add)

    return new_key

def hori(n, key, k):
    new_key = []
    add = 0

    for x in range(n):
        new_key.append(deque(key[x]))

    if k == 0:
        return new_key
    elif k > 0:
        for i in range(k):
            for j in range(n):
                new_key[j].pop()
                new_key[j].appendleft(add)
    else:
        for i in range(abs(k)):
            for j in range(n):
                new_key[j].popleft()
                new_key[j].append(add)

    return new_key

def check(result, lock):
    answer = [[r + l for r, l in zip(R, L)] for R, L in zip(result, lock)]

    for i in range(len(result)):
        for j in range(len(lock)):
            if answer[i][j] != 1:
                return False
    else:
        return True

def solution(key, lock):
    # key의 길이와 lock의 길이가 다를 때
    if len(key) < len(lock):
        diff = len(lock) - len(key)

        for i in range(len(key)):
            for j in range(diff):
                key[i].append(0)

        for _ in range(diff):
            key.append([0] * len(lock))

    n = len(key)
    new_key = key
    arange = list(range(-(n - 1), n))

    for _ in range(4):
        turn_key = turn(n, new_key)
        for i in arange:
            hori_key = hori(n, turn_key, i)
            for j in arange:
                result = vert(n, hori_key, j)
                if check(result, lock):
                    return True
        new_key = turn_key

    else:
        return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 1, 0]]))
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))