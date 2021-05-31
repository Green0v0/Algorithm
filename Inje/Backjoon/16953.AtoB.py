from collections import deque

a, b = map(int(input().split()))
q = deque([a])

while q:
    nums = q.pop()
    for now_num in nums:
        if 
