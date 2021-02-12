# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
# x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
# 작업을 수행한 결과가 조건을 만족하지 않는다면 해당 작업은 무시.
# 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제합니다. (출발 좌표 변화 기준)
# return 기준
# return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
# x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.

# 조건을 check하는 함수
# 설치 or 삭제 / 기둥 or 보
# [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# current = [[0]]
def installation(n, s, build_frame):
    # [1,0,0,1]
    x, y, build_type = s[0], s[1], s[2]
    if build_type == 0:
        pillar(n, x,y, build_frame)
    else:
        crossbeam(x, y, build_frame)
    pass

def elimination(s, build_frame):
    # [1,0,0,1]
    x, y, build_type = s[0], s[1], s[2]
    if build_type == 0:
        pillar(x,y, build_frame)
    else:
        crossbeam(x, y, build_frame)
    pass

# 구조물이 겹치도록 설치하는 경우와, 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않습니다.
def pillar(n, x, y, build_frame):
    current = [[]]
    # 조건을 만족하면 return True
    if y == 0:
        return True

def crossbeam(x, y, build_frame):
    pass
def solution(n, build_frame):

    answer = [[]]
    for i in build_frame:
        if i[3] == 1: # 설치
            answer = installation(i)
        else:
            answer = elimination(i)
    return answer



solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]] 시작점 위치로 return
solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

def solution(n, build_frame):
    current = [['']*(n+1) for _ in range(n+1)] # 0부터 n까지 이므로 n+1까지 좌표를 만들어야 한다.
    # build_frame 순회
    for value in build_frame:
        # 설치
        if value[3] == 1:
            # 기둥
            if value[2] == 0:
                x, y = value[0], value[1]
                if y == 0: # 바닥에 기둥('p')을 설치한 경우
                    current[y][x] = 'p' # current의 idx가 거꾸로인거를 기억하자

            # 보
            else:
                pass
        # 제거
        elif value[3] == 0:
            pass
    print(current)
solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]] 시작점 위치로 return