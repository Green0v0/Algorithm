# 전체공간 빈곳 = 0 / 기둥 = 1 / 보 = 2 / 기둥+보 = 3
# !!!좌표와 행열의 행번호는 위아래 반전임 유의!!!!

# # 2nd try:
def ispsb(now_ans):
    # 이 함수가 실행될 때마다 모든 구조물에 대한 가능성을 확인하여
    # 전체 구조물에 대해 가능한 구조인지 확인
    for x, y, struct in now_ans: # 한개의 구조물씩 확인하는 이터레이션

        if struct == 0:
            if not y or [x-1, y, 1] in now_ans or [x, y, 1] in now_ans\
                    or [x, y-1, 0] in now_ans:
                continue
            return False

        elif struct == 1:
            if [x, y-1, 0] in now_ans or [x+1, y-1, 0] in now_ans\
                or ([x-1, y, 1] in now_ans and [x+1, y, 1] in now_ans):
                continue
            return False

    return True

def solution(n, build_frame):
    now_ans = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            now_ans.remove([x, y, stuff])
            if not ispsb(now_ans):
                now_ans.append([x, y, stuff])
        elif operate == 1:
            now_ans.append([x, y, stuff])
            if not ispsb(now_ans):
                now_ans.remove([x, y, stuff])
    return sorted(now_ans)


n1 = 5
bf = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
      [1, 1, 1, 0], [2, 2, 0, 1], [4, 1, 0, 1], [4, 2, 0, 1], [4, 3, 0, 1], [4, 4, 0, 1]]

print(solution(n1, bf))

# # 1st try:
# # 이 과정에서는 한 구조물을 설치하거나 삭제할 때 해당 구조물만 가능한지 확인하려 했으나,
# # 이외의 구조물에 대한 가능성을 확인하지 못하여 실패
# board = []
#
#
# def ispsb(struct):
#     global board
#     pos = struct[:2]
#
#     # 만약 기둥이라면,
#     if not struct[2]:
#         # 바닥이거나 /왼쪽 또는 현위치에 보가 있거나 /아래에 기둥이 있어야 한다.
#         if not pos[1] or (pos[0] > 0 and board[pos[1]][pos[0] - 1] >= 2) or board[pos[1]][pos[0]] >= 2\
#                 or (pos[1] > 0 and board[pos[1] - 1][pos[0]] % 2):
#             return True
#         else:
#             return False
#
#     # 만약 보라면,
#     else:
#         # 현위치아래나 오른쪽아래에 기둥이 있거나,
#         if (pos[1] > 0 and (board[pos[1] - 1][pos[0]] % 2 or board[pos[1] - 1][pos[0] + 1] % 2)):
#             pass
#         # 아니라면 양쪽에 모두 보가 있어야 한다.
#         else:
#             if (pos[0] > 0 and not board[pos[1]][pos[0] - 1] % 2)\
#                     and (pos[0] < len(board) and not board[pos[1]][pos[0] + 1] % 2):
#                 return True
#             else:
#                 return False
#
#
# def solution(n, build_frame):
#     answer = []
#     global board
#     board = [[0] * (n + 1) for _ in range(n + 1)]
#
#     # 각 이터레이션에서 가능한지 체크하기 위해 보드에 추가
#     for i in build_frame:
#         # 설치할 때
#         if i[3] and ispsb(i):
#             board[i[1]][i[0]] += i[2] + 1
#             answer.append(i[:3])
#         # 삭제할 때, 뺄 수 있다면 제거
#         else:
#             # 일단 제거 시도
#             board[i[1]][i[0]] -= i[2] + 1
#             pos = i[:2] # 위치 추적할 변수
#
#             # 기둥이라면 위에 기둥이 있는 경우에만 원상복구
#             if i[2] % 2 == 1:
#                 if  board[i[1]+1][i[0]] == 1:
#                 pass
#             # 보라면 양옆에 보만 있는 경우에만 원상복구
#             elif i[2] >= 2 and board[i[1]][i[0]-1] >= 2 and board[i[1]][i[0]+2] >= 2:
#                 pass
#
#             # # 만약 삭제하려는게 기둥이었다면
#             # if i[2] == 1:
#             #     # 위의 구조물 찾아 그에 맞는 ispsb 사용
#             #     i_t = [pos[0], pos[1], board[pos[0]][pos[1]]]
#             #     if i_t[2] < 3 and ispsb(i_t):
#             #         answer.remove(i[:3])
#             #     elif i_t[2] == 3:
#             #         if ispsb()
#             #
#             #         # # 위에 보 또는 기둥이 없거나, 바닥에 위치한 기둥이라면 삭제
#             #         # if not board[i[1] + 1][i[0]] or not i[1]:
#             #         #     answer.remove(i[:3])
#             #
#             #     # 아니라면 원상복구
#             #     else:
#             #         board[i[1]][i[0]] += i[2] + 1
#             # # 양옆에 보만 있고 그 아래 기둥이 없다면 원상복구
#             # if i[1] in range(1, n + 2) and i[0] in range(1, n - 1) \
#             #         and board[i[1]][i[0] - 1] == 2 and board[i[1]][i[0] + 1] == 2 \
#             #         and not board[i[1] - 1][i[0]] % 2 and not board[i[1] - 1][i[0] + 1] % 2:
#             #     board[i[1]][i[0]] += i[2] + 1
#             # # 아니라면 삭제
#             # else:
#             #     answer.remove(i[:3])
#
#
#     answer.sort()
#     return answer