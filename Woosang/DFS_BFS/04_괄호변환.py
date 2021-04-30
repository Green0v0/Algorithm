# 균형잡힌 괄호 문자열로 나누는 함수
def balance_split(string):
    open_str, close_str = 0, 0
    for i in range(len(string)):
        if string[i] == '(':
            open_str += 1
        else:
            close_str += 1
        if open_str == close_str:
            break
    return string[:i+1], string[i+1:]

# 올바른 문자열 확인 함수
def check_proper_string(string):
    check, ret = 0, True
    for i in range(len(string)):
        if string[i] == '(':
            check += 1
        else:
            check -= 1
        if check == -1:
            ret = False
            break
    return ret

def solution(p):
    if not(p):
        return p
    u, v = balance_split(p)
    if check_proper_string(u):
        return u + solution(v)
    else:
        ret = '(' + solution(v) + ')'
        for i in u[1:-1]:
            if i == '(':
                ret += ')'
            else:
                ret += '('
        return ret

p = "()))((()"
print(solution(p))