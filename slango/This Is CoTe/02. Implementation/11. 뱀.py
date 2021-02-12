def solution():
    n = int(input())
    k = int(input())
    a_pos = []
    for i in range(k):
        a_pos.append(list(map(int, input().split())))
    l = int(input())
    dirs = []
    dir_time = []
    for i in range(l):
        tmp = input().split()
        dirs.append([int(tmp[0]), tmp[1]])
        dir_time.append(int(tmp[0]))

    board = []
    for i in range(n):
        board.append([0 for _ in range(n)])

    for i in a_pos:
        board[i[0]-1][i[1]-1] = 2  # 사과가 있는 지점은 2
    snake = [[0, 0]]  # 뱀의 꼬리부터 머리 순으로 몸의 모든 좌표 저장
    # 뱀이 위치하는 지점은 1
    board[snake[0][0]][snake[0][1]] = 1

    now_time = 0
    time_idx = 0
    now_dir = 0  # 뱀의 이동방향은 0부터 3까지 순서대로 동쪽부터 시계방향 순. 동=0/남=1/서=2/북=3
    directs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    to_mv = []
    new_head = []
    while True:
        now_time += 1
        to_mv = directs[now_dir]
        now_head = snake[-1]
        new_head = [now_head[0] + to_mv[0], now_head[1] + to_mv[1]]
        snake.append(new_head)

        # 벽이나 자기 몸에 닿으면 끝
        if new_head[0] not in range(n) or new_head[1] not in range(n)\
                or board[new_head[0]][new_head[1]] == 1:
            break
        # 사과가 없으면
        elif board[new_head[0]][new_head[1]] == 0:
            # 꼬리자리 0으로 변환후 꼬리 줄이기
            board[snake[0][0]][snake[0][1]] = 0
            snake.pop(0)

        # 머리 위치, 몸 업데이트
        board[new_head[0]][new_head[1]] = 1
        now_head = new_head

        # 회전할 때라면
        if now_time in dir_time:
            # 방향전환
            if dirs[dir_time.index(now_time)][1] == 'L':
                now_dir = (now_dir - 1) % 4
            else:
                now_dir = (now_dir + 1) % 4
        # if dirs[time_idx][0] == now_time:
        #     # 방향전환
        #     if dirs[time_idx][1] == 'L':
        #         now_dir = (now_dir - 1) % 4
        #     else:
        #         now_dir = (now_dir + 1) % 4
        #     time_idx += 1

    print(now_time)

solution()