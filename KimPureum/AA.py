import sys
N, M = map(int,sys.stdin.readline().split())
total = []
for i in range(1,N+1):
    for j in range(1,M+1):
        total.append(i+j)
# 딕셔너리 형태
w_count={}
for lst in total:
    try: w_count[lst]+=1
    except: w_count[lst]=1
w_count_keys = list(w_count.keys())
final = []
for j in w_count_keys:
    if max(w_count.values()) == w_count[j]:
        final.append(j)

print(*final)
# print(len(total))