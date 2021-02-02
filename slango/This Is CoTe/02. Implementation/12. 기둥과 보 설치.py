# 전체공간 빈곳 = 0 / 기둥 = 1 / 보 = 2 / 기둥+보 = 3


# !!!좌표와 행열의 행번호는 위아래 반전임 유의!!!!


board = []


def isposible(struct):
    global board
    pos = struct[:2]

    # 만약 기둥이라면,
    if not struct[2]:
        # 바닥이거나 /왼쪽 또는 현위치에 보가 있거나 /아래에 기둥이 있어야 한다.
        if not pos[1] or (board[pos[1]][pos[0] - 1] >= 2 or board[pos[1]][pos[0]] >= 2) \
                or board[pos[1] - 1][pos[0]] % 2:
            return True
        else:
            return False

    # 만약 보라면,
    else:
        # 현위치아래나 오른쪽아래에 기둥이 있거나 /양쪽에 모두 보가 있어야 한다.
        if board[pos[1] - 1][pos[0]] % 2 or board[pos[1] - 1][pos[0] + 1] % 2 \
                or (board[pos[1]][pos[0] - 1] % 2 and board[pos[1] - 1][pos[0]] % 2):
            return True
        else:
            return False


def solution(n, build_frame):
    answer = []
    global board
    board = [[0] * (n + 1) for _ in range(n + 1)]

    # 각 이터레이션에서 가능한지 체크하기 위해 보드에 추가,
    # 결과로 리턴할
    for i in build_frame:
        pos = i[:2]
        # 설치할 때
        if i[3]:
            board[i[1]][i[0]] = i[2] + 1
            answer.append(i[:3])
        # 삭제할 때, 뺄 수 있다면, 제거
        elif not i[3] and isposible(i):
            board[i[1]][i[0]] = 0
            answer.remove(i[:3])

    answer.sort()
    return answer


n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))