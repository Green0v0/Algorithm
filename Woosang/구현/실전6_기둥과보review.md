## 접근법
  - 매순간 조건에 맞게 설치 및 삭제가 됬는지 확인
  - 작은거 하나라도 체크 잘하자
  - 리스트로 접근해도 문제는 없지만 셋으로 접근하면 효율성이 더 높다.
## flow
1. 제대로 된 설계가 들어 갔는지 확인 하는 함수 정의
    1. 기둥이라면
        - 바닥 위에 있거나, 보의 한쪽 끝 위에 있거나, 다른 기둥 위에 있으면 설치 가능
    2. 보라면
        - 한쪽 부분이 기둥위에 있거나, 양쪽 부분이 다른 보와 동시에 연결되 있으면 설치 가능
2. bulid_frame에서 한개씩 빼면서 확인
    1. 설치, 삭제인지 확인 (결과값을 담은 변수 정의) 이하 result
        1. 설치
              1. 설계도를 result에 넣는다.
              2. 제대로된 설계도가 맞는지 확인(1번 함수)
              3. 아니면 넣었던 값 remove()
        2. 삭제
              1. result에 있는 설계도를 지운다.
              2. 지운 설계도를 확인한다.
              3. 제대로 된 설계도면 지운 값을 다시 넣어준다.
  2. 순서에 맞게 정렬 후 반환
```python
def check(result):
  # 끝까지 확인을 위해 각 조건문안에서 continue 사용
  for x, y, kind in result:
    if kind == 0: # 기둥이면
      if y == 0 or (x-1,y,1) in result or (x,y,1) in result or (x, y-1, 0) in result:
        continue # 맞으면 pass
      return False # 아니면 false 반환
    else: # 보면
      if (x,y-1,0) in result or (x+1,y-1,0) in result or ((x-1,y,1) in result and (x+1,y,1) in result):
        continue # 맞으면 pass
      return False # 아니면 false 반환
  return True

def solution(build_frame):
  result = set()
  for x, y, kind, how in build_frame:
    items = (x,y,kind)
    if how == 1: # 설치
      result.add((items))
      if not check(result):
        result.remove((items))
    else: # 삭제
      result.remove((items))
      if not check(result):
        result.add((items))
  answer = map(list, result)
  return sorted(answer, key= lambda x: (x[0],x[1],x[2]))

print(solution([[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
"""
결과값 : [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]]
"""
```
