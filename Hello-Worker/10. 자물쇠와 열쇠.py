import copy

def rotate(key, m):
    rst = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rst[j][m-1-i] = key[i][j]
    return rst

def test(key, lock, i, j, m, n):
    dump = copy.deepcopy(lock)
    for p in range(i, i+m):
        if 0 <= p < n:
            for q in range(j, j+m):
                if 0 <= q < n:
                    dump[p][q] += key[p-i][q-j] # ??
    for line in dump:
        for item in line:
            if item != 1:
                return False
    return True

def solution(key, lock):
    m, n = len(key), len(lock)
    for _ in range(4):
        for i in range(-m+1, n):
            for j in range(-m+1, n):
                if test(key, lock, i, j, m, n):
                    return True
        key = rotate(key,m)
    return False

print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))
