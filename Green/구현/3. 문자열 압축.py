def solution(s):
    if len(s) == 1:
        return 1

    slice = []
    answer = ''
    mincnt = float('inf')
    for j in range(1, len(s) // 2 + 1):
        for i in range(j, len(s) + j, j):
            slice.append(s[i - j:i])

        cnt = 0
        for x in range(1, len(slice)):
            if slice[x - 1] == slice[x]:
                cnt += 1
            else:
                if cnt == 0:
                    answer += ''.join(['', slice[x - 1]])
                else:
                    answer += ''.join([str(cnt + 1), slice[x - 1]])
                cnt = 0
            if x == len(slice) - 1:
                if cnt == 0:
                    answer += ''.join(['', slice[x]])
                else:
                    answer += ''.join([str(cnt + 1), slice[x]])

        if mincnt > len(answer):
            mincnt = len(answer)

        slice = []
        answer = ''
    return mincnt