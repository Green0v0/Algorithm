# '('와 ')'의 개수가 같다면 => 균형잡힌 괄호 문자열
# 균형잡힌 문자열에서 '('와')'의 짝도 맞다면 => 올바른 괄호 문자열

# 입력받기
p = input()

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
# 2. 문자열 w를 '두 균형잡힌 괄호 문자열' u,v로 분리.
#    단, u는 '균형잡힌 괄호 문자열'로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있다.
def split(p):
    if p == '':
        return ''
    else:
        cnt = 0
        for i in range(len(p)):
            if p[i] == ')':
                cnt -= 1
            else:
                cnt += 1
            if cnt == 0:
                break
        return p[:i+1], p[i+1:] #u,v분리

# 3. 수행한 결과 문자열을 u에 이어붙인 후 반환.
# 3-1. 문자열 u가 '올바른 괄호 문자열'이라면 문자열 v에 대해 1단계부터 다시 수행.
def check(u):
    cnt = 0
    for i in u:
        if i == '(':
            cnt += 1
        else:
            cnt -=1
        if cnt < 0: #올바른 문자열 확인. -가 되면 짝이 안맞음.
            return False
    return True

# 4. 문자열 u가 '올바른 괄호 문자열'이 아니라면 아래 과정 수행.

def solution(p):
    try:
        u,v = split(p)
    except:
        return ''

    ans = ''
    if check(u):
        ans+=u
        ans+=solution(v)
        return ans
    else:
        ans+='('
        ans+=solution(v)
        ans+=')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                ans += ')'
            else:
                ans += '('
        return ans

print(solution(p))





