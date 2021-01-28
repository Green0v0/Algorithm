# 첫 풀이
n = input()
fn = list(map(int,n[0:len(n)//2]))
bn = list(map(int,n[len(n)//2:]))
if sum(fn) == sum(bn):
    print('LUCKY')
else:
    print('READY')

