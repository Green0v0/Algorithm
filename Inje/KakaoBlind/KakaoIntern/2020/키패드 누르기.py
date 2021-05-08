def dist(a, b):
    lst = ['*', 0, '#']
    if a in lst:
        a = lst.index(a) + 10
    if b in lst:
        b = lst.index(b) + 10
    return abs((a-1)//3 - (b-1)//3) + abs(a%3 - b%3)

def solution(numbers, hand):
    answer = ''
    
    now_l, now_r = '*', '#'
    to_lft, to_rgt = [1, 4, 7], [3, 6, 9]
    
    for nxt in numbers:
        if nxt in to_lft:
            answer += 'L'
            now_l = nxt
        elif nxt in to_rgt:
            answer += 'R'
            now_r = nxt
        else:
            if dist(now_l, nxt) < dist(now_r, nxt)\
            or (dist(now_l, nxt) == dist(now_r, nxt) and hand == 'left'):
                answer += 'L'
                now_l = nxt
            else:
                answer += 'R'
                now_r = nxt
    
    return answer

# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = 'right'
numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'
print(solution(numbers, hand))