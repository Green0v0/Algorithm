# 어차피 열쇠를 움직여 확인해야 하므로 m*m 내에서 움직이는 작업x
# def move_hor(key,dx):
#     return key

# def move_ver(key,dy):
#     return key

def rotated(key, m):
    aftrot = []
    for i in range(m):
        aftrot.append([0 for _ in range(m)])
    for i in range(m):
        for j in range(m):
            aftrot[j][m - i - 1] = key[i][j]
    return aftrot


def solution(key, lock):
    M = len(key)
    N = len(lock)

    new_keys = [key]
    for _ in range(3):
        key = rotated(key, M)
        if new_keys[-1] != key:
            new_keys.append(key)

    # 가장먼저 회전한 모든 키 순서대로 조회
    for now_key in new_keys:
        
        # key 가 오른쪽으로 dx만큼, 아래로 dy만큼 움직였다고 가정했을 때,
        # 모든 위치별로 조회
        for dx in range(-M, N):
            for dy in range(-M, N):
                
                now_ans = True
                # 각 지점의 (y,x) 좌표로 모든 지점 확인
                for x in range(N):
                    for y in range(N):
                        nowkey_x = x - dx
                        nowkey_y = y - dy
                        tmp = 0
                        if nowkey_x in range(M) and nowkey_y in range(M):
                            tmp = now_key[nowkey_y][nowkey_x] + lock[y][x]
                        else:
                            tmp = lock[y][x]

                        if tmp != 1:
                            now_ans = False
                            break
                if now_ans:
                    return True

    return False
