def chk(p):
    cnt = 0
    for ch in p:
        if ch == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True

def recur(p):
    if not p or chk(p):
        return p

    for i in range(2,len(p)+1,2):
        u, v = p[:i], p[i:]
        if u.count('(') == u.count(')'):
            break

    if chk(u):
        return u+recur(v)

    tmp_str = u[1:-1].replace('(','-')
    tmp_str = tmp_str.replace(')','(')
    tmp_str = tmp_str.replace('-',')')
    
    return '(' + recur(v) + ')' + tmp_str

def solution(p):
    return recur(p)

# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))