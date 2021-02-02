di = {'abc':2}
print(di.keys(), di.values())
# print(list(zip(di.keys(),di.values())))
t = list(zip(di.values(),di.keys()))
print(t)
x = 'abcabcdede'
print(x)
for i,j in t:
    # print(str(i)+j)
    if i*j in x:
        print('i*j',i*j)
        print(type(i*j))
        print(str(i)+j)
        x = x.replace(i*j,str(i)+j)
    print(x)
