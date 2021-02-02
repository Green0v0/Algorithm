n = "123402"

half = len(n)//2  # 문자열의 중간 값을 찾는다.

first = [int(i) for i in n[:half]] # 앞에서 부터 3개(0부터 2까지)
second = [int(i) for i in n[:half-1:-1]] # 뒤에서 부터 3개(-1부터 -3 까지)

if sum(first) == sum(second): # first와 second가 같으면 럭~~~키~~!!
    print("LUCKY")
elif sum(first) != sum(second): # 다르면 레디...
    print("READY")