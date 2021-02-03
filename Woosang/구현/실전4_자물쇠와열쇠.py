def rotate(a): # 90도 회전 함수
    return list(zip(*a[::-1]))

def check(new_lock): # 자물쇠가 전체 1인지 확인
    lock_len = len(new_lock) // 3
    for i in range(lock_len, lock_len*2):
        for j in range(lock_len, lock_len*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    k = len(key)
    l = len(lock)

    # 자물쇠 확장 후 중앙에 자물쇠 배치
    new_lock = [[0] * (l*3) for _ in range(l * 3)]
    for i in range(l):
        for j in range(l):
            new_lock[l+i][l+j] = lock[i][j]

    # 4가지 방향 확인
    for rotation in range(4):
        rotate(key) # 열쇠 회전
        for x in range(l*2):
            for y in range(l*2):
                # 자물쇠에 열쇠 넣기`
                for i in range(k):
                    for j in range(k):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True: # 자물쇠 확인
                    return True
                # 열쇠 빼기
                for i in range(k):
                    for j in range(k):
                        new_lock[x+i][y+j] -= key[i][j]
    return False