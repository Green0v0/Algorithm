from itertools import permutations

def eval_calc(num_idx, oper_idx, operator_list):
    global num_list, first_num
    # 맨 앞의 숫자면 함수 끝내기
    if num_idx == 0:
        return num_list[num_idx]
    # 함수가 종료 조건 만날때까지 재귀
    ret_num = eval_calc(num_idx-1, oper_idx-1,operator_list)
    # 나눗셈이면 바꾸기
    if operator_list[oper_idx] == '/':
        operator_list[oper_idx] = '//'
        # 나누기인데 음수인 경우
        if ret_num[0] == '-':
            return '-' + str(eval(ret_num[1:] + operator_list[oper_idx] + num_list[num_idx]))
    return str(eval(ret_num + operator_list[oper_idx] + num_list[num_idx]))

N = int(input())
num_list = list(map(str, input().split()))
tmp = list(map(int, input().split()))

# 연산자 정의
operator_dict = {0:'+', 1:'-', 2:'*', 3:'/'}
operator_list = ''
for i in range(4):
    if tmp[i]:
        operator_list += operator_dict[i]*tmp[i]

max_num, min_num = float('-inf'), float('inf')
for combine in set(permutations(operator_list, N-1)):
    ret = eval_calc(N-1, N-2, list(combine))
    max_num = max(max_num, int(ret))
    min_num = min(min_num, int(ret))

print(max_num)
print(min_num)

#################################################
from itertools import permutations

# 숫자와 연산자 배열을 넘겨 받아 계산해 주는 함수
def calc(num_list, operators):
    ret = num_list[0]
    for i in range(N-1):
        if operators[i] == '+':
            ret += num_list[i+1]
        elif operators[i] == '-':
            ret -= num_list[i+1]
        elif operators[i] == '*':
            ret *= num_list[i+1]
        else:
            if ret < 0:
                ret = -(abs(ret) // num_list[i+1]) 
            else:
                ret //= num_list[i+1]
    return ret

N = int(input())
num_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))

# 연산자 정리
operator_dict = {0:'+', 1:'-', 2:'*', 3:'/'}
operators = ''
for i in range(4):
    if operator_list[i]:
        operators += operator_dict[i] * operator_list[i]

# 큰값과 작은 값 초기 정의
max_num, min_num = float('-inf'), float('inf')
for case in set(permutations(operators, N-1)):
    compare = calc(num_list, case)

    max_num = max(max_num, compare)
    min_num = min(min_num, compare)

print(max_num)
print(min_num)