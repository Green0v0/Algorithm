# 3rd try:
# pseudo code
# 1. 움직이고, 회전하는 함수 -> 키 회전만 함수로, 이동은 for문으로
# 2. 모든 이동과 회전의 경우에 대해
# 3. 모든 위치를 확인. 다만, 자물쇠와 키가 겹쳐있는 부분만 확인하면 된다. -> 여기서 틀렸다.
# 3.1 겹쳐있는 부분만 확인하는게 아니라, 자물쇠의 모든 홈을 채워야 한다.

# 키를 회전하는 함수
def rotated(key):
    leng = len(key)
    tmpkey = [[0]*leng for _ in range(leng)]
    newkey = [[0]*leng for _ in range(leng)]

    for i in range(leng):
        for j in range(leng):
            tmpkey[i][j] = key[j][i]
    for i in range(leng):
        for j in range(leng):
            newkey[i][j] = tmpkey[i][leng-j-1]
    
    return newkey


def solution(key, lock):
    M, N = len(key), len(lock)

    # 회전을 반영한 모든 경우의 키 list
    rot_key_list = [key]
    for _ in range(3):
        newkey = rotated(key)
        if newkey not in rot_key_list:
            rot_key_list.append(newkey)
        key = newkey

    # 모든 회전한 키에 대해
    for now_key in rot_key_list:

        # 모든 가로세로방향으로 이동한 만큼
        for d_x in range(-(M-1), N):
            for d_y in range(-(M-1), N):

                # 모든 부분에 대해
                for x in range(N):
                    for y in range(N):
                        now_idx = lock[x][y]
                        key_x, key_y = x - d_x, y - d_y
                        if key_x in range(M) and key_y in range(M):
                            now_idx += now_key[key_x][key_y]
                        
                        if now_idx != 1:
                            chk_all_area = False
                            out_for = True
                            break

                        if chk_all_area:
                            return True

                    
    # 아무런 방향 위치에서도 맞출 수 없다면 그건 안되는 조합
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
                


                # # pseudo code
                # # 1. 움직이고, 회전하는 함수 -> 키 회전만 함수로, 이동은 for문으로
                # # 2. 모든 이동과 회전의 경우에 대해
                # # 3. 모든 위치를 확인. 다만, 자물쇠와 키가 겹쳐있는 부분만 확인하면 된다. -> 여기서 틀렸다.
                # # 2nd try:
                # for x in range(max(0, d_x), min(N, M+d_x)):
                #     # 이중 for문 한번에 나가는 체크
                #     out_for = False
                #     for y in range(max(0, d_y), min(N, M+d_y)):
                #         if lock[y][x] + now_key[y-d_y][x-d_x] != 1:
                #             chk_all_area = False
                #             out_for = True
                #             break
                #     if out_for:
                #         break
                # # 만약 모든 부분이 맞았다면 키로 열 수 있는 것이므로 바로 정답!
                # if chk_all_area:
                #     return True
                    



# # 1st try:

# # 어차피 열쇠를 움직여 확인해야 하므로 m*m 내에서 움직이는 작업x
# # def move_hor(key,dx):
# #     return key

# # def move_ver(key,dy):
# #     return key

# def rotated(key, m):
#     aftrot = []
#     for i in range(m):
#         aftrot.append([0 for _ in range(m)])
#     for i in range(m):
#         for j in range(m):
#             aftrot[j][m - i - 1] = key[i][j]
#     return aftrot


# def solution(key, lock):
#     M = len(key)
#     N = len(lock)

#     new_keys = [key]
#     for _ in range(3):
#         key = rotated(key, M)
#         if new_keys[-1] != key:
#             new_keys.append(key)

#     # 가장먼저 회전한 모든 키 순서대로 조회
#     for now_key in new_keys:
        
#         # key 가 오른쪽으로 dx만큼, 아래로 dy만큼 움직였다고 가정했을 때,
#         # 모든 위치별로 조회
#         for dx in range(-M, N):
#             for dy in range(-M, N):
                
#                 now_ans = True
#                 # 각 지점의 (y,x) 좌표로 모든 지점 확인
#                 for x in range(N):
#                     for y in range(N):
#                         nowkey_x = x - dx
#                         nowkey_y = y - dy
#                         tmp = 0
#                         if nowkey_x in range(M) and nowkey_y in range(M):
#                             tmp = now_key[nowkey_y][nowkey_x] + lock[y][x]
#                         else:
#                             tmp = lock[y][x]

#                         if tmp != 1:
#                             now_ans = False
#                             break
#                 if now_ans:
#                     return True

#     return False