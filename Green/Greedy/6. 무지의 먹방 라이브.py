# 원형 : %3 해서 2(=len(food_times)-1)가 될 때 인덱스 0으로 돌아감
food_times = [3,1,2]
idx = 0
k = 5
while k != 0:
    print(food_times)
    print('idx',idx)
    print('k',k)
    if food_times == [0]*len(food_times):
        print(-1)
        break # return -1
    # 값이 0이면 다음 리스트로
    if food_times[idx%3] == 0:
        idx+=1
        continue
    else:
        food_times[idx%3] -= 1
        idx += 1
        k -= 1
print(food_times)
print(food_times[idx%3])