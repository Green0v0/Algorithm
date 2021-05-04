def solution(routes):
    answer = 0
    
    times = []
    for stt, end in routes:
        times.append((stt, 0))
        times.append((end, 1))
        
    times.sort(key=lambda x:x[0])
    
    for i in range(len(times)-1):
        if times[i][1] == 0 and times[i+1][1] == 1:
            answer += 1
    
    return answer

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]


print(solution(routes))