s = input()
total = 0
s = ''.join(sorted(s))
answer = ''
for i in s:
    if i.isdigit():
        total += int(i)
    else:
        answer += i

print(answer + str(total))