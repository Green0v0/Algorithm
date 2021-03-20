# n,k=map(int,input().split(" "))
# coin = []
# count =0
n =10
k=4200
coin=[1,5,10,50,100,500,1000,5000,10000,50000]
count=0

# for i in range(n):
#     coin.append(int(input()))

coin.sort(reverse = True)
for i in coin:
    while True:
        if i<=k:
            k-=i
            count+=1
        else:
            break
print(count)