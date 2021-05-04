def chk(s):
    lst = []
    for chr in s:
        if chr in ['(','[','{']:
            lst.append(chr)
        elif chr == ')' and lst and lst[-1] == '(':
            lst.pop()
        elif chr == ']' and lst and lst[-1] == '[':
            lst.pop()
        elif chr == '}' and lst and lst[-1] == '{':
            lst.pop()
        else:
            return False
    if not lst:
        return True
    else:
        return False
        
def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        s = s[1:] + s[0]
        if chk(s):
            answer += 1
            
    return answer

solution("[](){}")
# solution("}]()[{")