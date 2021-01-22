N, M, K = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
total = 0
for i in range(M):
    if i != 0 and (i+1)%(K+1) == 0:
        total += li[1]
    else:
        total += li[0]
print(total)