def solution(s):
    answer = 0

    lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        chk = True
        for i in lst:
            if i in s:
                s = s.replace(i, str(lst.index(i)))
                chk = False
        if chk:
            break

    return int(s)

print(solution("one4seveneight"))