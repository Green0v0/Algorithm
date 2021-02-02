s = "c2"

move = [[-2,1],[-2,-1],[2,1],[2,-1],[-1,2],[1,2],[-1,-2],[-1,2]]
location = [0, 0]
location[0] = int(s[1]) - 1

# alpha = "abcdefghijklmnopqrstuvwxyz"
# for i in alpha: # 말의 현재 위치 location 변수에 담기
#     if i == s[0]:
#         location[1] = alpha.index(i)
#         break
location[1] = int(ord(s[0])) - int(ord("a"))


result = 0
for i in range(len(move)): 
    # 체스말이 움직일 수 있는 모든 경우의 수 대입
    temp = []
    for j in range(len(location)):
        temp.append(location[j] + move[i][j])
    # 말의 위치가 체스판을 벗어나지 않으면 cnt +
    if -2 in temp or -1 in temp: 
        continue
    elif 9 in temp or 10 in temp:
        continue
    else:
        result += 1
print(result)
