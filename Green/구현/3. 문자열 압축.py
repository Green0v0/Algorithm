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
            answer += ''.join([cnt,value])
        if mincnt > len(answer):
            mincnt = len(answer)
        slist = []
        result = []
        cnt = 0
        answer = ''

    return mincnt

# 정답 처리된 코드
def compress(s):
    slice = []
    answer = ''
    mincnt = float('inf')
    # for j in range(1,len(s)//2+1):
    # 1글자일때, inf로 나오기 때문에, 안전하게 +2를 해도 좋다.
    for j in range(1,len(s)//2+2):
        for i in range(j,len(s)+j,j):
            slice.append(s[i-j:i])
        # print(slice)
        cnt = 0
        for x in range(1,len(slice)):
            if slice[x-1] == slice[x]:
                cnt+=1
            else:
                if cnt == 0:
                    answer+=''.join(['',slice[x-1]])
                else:
                    answer+=''.join([str(cnt+1),slice[x-1]])
                cnt=0
            if x==len(slice)-1:
                if cnt == 0:
                    answer+=''.join(['',slice[x]])
                else:
                    answer+=''.join([str(cnt+1),slice[x]])
        if mincnt > len(answer):
            mincnt = len(answer)
        # print(answer)
        slice = []
        answer =''
    return mincnt
print(compress('aabbaccc'))

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
