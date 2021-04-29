def solution(genres, plays):
    answer = []
    gen = list(set(genres))

    alll = [[] for _ in range(len(gen))]
    for idx, (ge, pl) in enumerate(zip(genres, plays)):
        alll[gen.index(ge)].append((idx, pl))

    new = []
    for i in alll:
        sum1 = 0
        for j in i:
            sum1 += j[1]
        k = sorted(i, key=lambda x: -x[1])
        k.append(sum1)
        new.append(k)

    new.sort(key=lambda x:x[-1], reverse=True)

    for i in new:
        answer.append(i[0][0])
        if len(i)>2:
            answer.append(i[1][0])
    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))