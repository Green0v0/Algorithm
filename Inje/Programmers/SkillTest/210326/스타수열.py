def solution(a):
    num_lst = list(set(a))
    cnt_lst = [a.count(num_lst[i]) for i in range(len(num_lst))]

    cnt_lst.sort(reverse=True)
    if len(cnt_lst)>1:
        return min(sum(cnt_lst[1:]), cnt_lst[0]) * 2
    else:
        return 0