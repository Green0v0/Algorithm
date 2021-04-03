def solution(x):
    # i는 1글자, 2글자, 3글자...
    # 큰 수 부터 확인한다면 더 빠를 듯.
    min_cnt = len(x)
    for i in range(1,len(x)//2+1):
        # 비교할 기준 변수 : 첫 값은 길이가 1인 첫번째 글자
        # check값과 비교할 값이 다르다면 비교한 값으로 update
        check = x[:i]
        # 초기 범위 변수
        s = i
        e = s+i
        # count할 변수
        answer = dict()
        while e < len(x)+1:
            if check != x[s:e]:
                check = x[s:e]
            else:
                answer[check] = answer.get(check,1)+1
            s = e
            e = s+i
        zip_answer = list(zip(answer.values(),answer.keys()))
        cnt = 0
        for v,k in zip_answer:
            if v*k in x:
                x = x.replace(v*k, str(v)+k)
            cnt = len(x)
            if min_cnt > cnt:
                min_cnt = cnt

    print(min_cnt)
solution('abcabcdede')

# 1. 자르고 압축한 값을 내보내는 함수
# 2. solution에서는 비교
def solution(s):
    slist = []
    result = []
    cnt = 0; answer = ''
    mincnt = float('inf')
    for j in range(1,len(s)//2+1):
        for i in range(j,len(s)+j,j):
            slist.append(s[i-j:i])
        for x in range(1,len(slist)):
            if slist[x-1] == slist[x]:
                cnt+=1
            else:
                result.append([cnt,slist[x-1]])
                cnt=0
            if x==len(slist)-1:
                result.append([cnt, slist[x]])
        for cnt,value in result:
            if cnt!=0:
                cnt = str(cnt+1)
            else:
                cnt = ''
            answer+=''.join([cnt,value])
        if mincnt > len(answer):
            mincnt = len(answer)
        slist = []
        result = []
        cnt = 0
        answer = ''

    return mincnt

def solution(s):
    if len(s) == 1:
        return 1
    slice = []
    answer = ''
    mincnt = float('inf')
    for j in range(1, len(s)//2+1):
        for i in range(j, len(s)+j, j):
            slice.append(s[i-j:i])

        cnt = 0
        for x in range(1, len(slice)):
            if slice[x-1] == slice[x]:
                cnt+=1
            else:
                if cnt == 0:
                    answer += ''.join(['', slice[x-1]])
                else:
                    answer += ''.join([str(cnt+1), slice[x-1]])
                cnt=0
            if x == len(slice) - 1:
                if cnt == 0:
                    answer += ''.join(['', slice[x]])
                else:
                    answer += ''.join([str(cnt+1), slice[x]])

        if mincnt > len(answer):
            mincnt = len(answer)
        slice = []
        answer =''
    return mincnt
print(solution('aabbaccc'))

# str slicing으로만 풀어보려 했던 풀이, 마지막 부분을 처리하기 어려워서
# 포기했다!
def practice(s):
    a = 'aabbaccc'
    check = ''
    cnt = 0
    result = ''
    for i in range(1, len(a) // 2 + 1):
        check = a[:i]
        for j in range(i, len(a), i):
            if check == a[j:i + j]:
                cnt += 1
            else:
                # if j > len(a)-i and len(check) != a[j:]:
                #     result+=''.join(a[j:])
                if cnt != 0:
                    result += ''.join([str(cnt + 1), check])
                else:
                    result += ''.join(['', check])
                cnt = 0
                check = a[j:i + j]
            if j == len(a) - 1:
                result += ''.join([str(cnt + 1), check])
        print(result)
        cnt = 0
        result = ''

# 문자열 압축 문제의 경우 풀이 방향은 좋습니다. :)
# 다음과 같은 방향으로 로직을 마무리하면 될 것 같습니다.
#
# 문자열을 길이의 절반만큼 순회합니다.
# 선택된 길이(number) 만큼 문자열을 자르며 이전 문자열과 비교하며 압축이 가능한지 확인합니다.
# 더 이상 압축이 불가능하다면 압축된 문자열을 만든 후 다음 문자열을 잘라 2번을 반복합니다.
# 압축된 문자열의 길이를 확인하고 이전에 압축한 문자열보다 짧다면 갱신합니다.
# 가장 짧은 압축된 문자열의 길이를 반환합니다.
# 만약 구현이 너무 어렵다면 이후 정답 코드를 보는 것도 좋습니다. :) 너무 오래 고민하지 않으셔도 괜찮아요.

# 다른 사람 풀이
def solution(s):
    answer = len(s)

    for step in range(1, len(s)// 2 + 1):
        key = s[0:step]
        result_str = ""

        count = 1

        for i in range(step, len(s) + step, step):
            next = s[i:i + step]
            prev = key

            if next == key:
                count += 1
            else:
                key = next
                result_str += str(count) + prev if count > 1 else prev
                count = 1

        answer = min(answer, len(result_str))

    return answer

def codereviewSolution(s):
    if len(s) == 1:
        return 1

    slice = []
    answer = ''
    mincnt = float('inf')

    for j in range(1, len(s) // 2 + 1):
        for i in range(j, len(s) + j, j):
            slice.append(s[i - j : i])

        cnt = 0
        for x in range(1, len(slice)):
            prev = slice[x - 1]
            curr = slice[x]

            if prev == curr:
                cnt += 1

            else:
                # 대입되는 변수가 같은 경우 inline if를 사용할 수도 있습니다.
                answer += ''.join(['', prev]) if cnt == 0 else ''.join([str(cnt + 1), prev])
                cnt = 0

            if x == len(slice) - 1:
                answer += ''.join(['', curr]) if cnt == 0 else ''.join([str(cnt + 1), curr])

        mincnt = min(mincnt, len(answer))

        slice = []
        answer = ''

    return mincnt