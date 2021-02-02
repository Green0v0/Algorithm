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