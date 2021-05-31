N = input()
a = 0
b = 0
l = len(N)//2
for i in N[:l]:
    a += int(i)
for i in N[l:]:
    b += int(i)

if a == b:
    print("LUCKY")
else:
    print("READY")