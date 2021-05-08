import heapq

def solution(n, k, cmd):
    answer = '0'*n
    
    data = []
    for i in range(n)):
        heapq.heappush(data, (i, i))
    del_memory = []

    cursor = k
    for cm in cmd:
        if cm[0] == 'U':
            cursor -= int(cm.split()[-1])
        elif cm[0] == 'D':
            cursor += int(cm.split()[-1])
        elif cm[0] == 'C':
            if cursor == len(data):
                data[cursor] = -1
                del_memory.append()
            else:

                cursor += 1
        else:
            to_rst = del_memory.pop()



    return answer