# 3rd try:
def solution(n):
    soo_set = {2:[1], 3:[7], 4:[4], 5: [2,3,5], 6:[0,6,9], 7:[8]}
    soo_lst = list(soo_set.keys())
    soo_rev_lst = sorted(soo_lst, reverse=True)
    # [2, 3, 4, 5, 6, 7]
    tmp_soo = n
    soo_min = ''
    tmp_soo_min = '8'*(n//7)
    left_soo = n%7
    if left_soo==0:
        soo_min = tmp_soo_min
    elif left_soo==1:
        soo_min = '10'+tmp_soo_min[1:]
    elif 2<=left_soo<=5:
        soo_min = str(soo_set[left_soo][0])+tmp_soo_min
    elif left_soo==6:
        soo_min = '6'+tmp_soo_min

    soo_max = '7'*(n%2) + '1'*((n//2)-(n%2))
    
    return (soo_min, soo_max)

for i in range(2, 101):
    print(i, solution(i))





# # 2nd try:
# def solution(n):
#     soo_set = {2:[1], 3:[7], 4:[4], 5: [2,3,5], 6:[0,6,9], 7:[8]}
#     soo_lst = list(soo_set.keys())
#     soo_rev_lst = sorted(soo_lst, reverse=True)
#     # [2, 3, 4, 5, 6, 7]
#     tmp_soo = n
#     soo_min = ''
#     while tmp_soo>8:
#         for digit in soo_rev_lst:
#             if tmp_soo >= digit:
#                 tmp_soo -= digit
#                 if min(soo_set[digit])==0:
#                     soo_min += str(soo_set[digit][1])
#                 else:
#                     soo_min += str(min(soo_set[digit]))
#                 break
#     if tmp_soo==8:
#         soo_min += '01'
#     else:
#         for digit in soo_rev_lst:
#             if tmp_soo >= digit:
#                 tmp_soo -= digit
#                 if min(soo_set[digit])==0:
#                     soo_min += str(soo_set[digit][1])
#                 else:
#                     soo_min += str(min(soo_set[digit]))
#                 break

#     tmp_soo_min = soo_min[::-1]

#     if n%2==0:
#         soo_max = '1'*(n//2)
#     else:
#         soo_max = '7'*(n%2) + '1'*((n//2)-1)
    
#     return (tmp_soo_min, soo_max)

# for i in range(2, 101):
#     print(i, solution(i))



# 0 6
# 1 2
# 2 5
# 3 5
# 4 4
# 5 5
# 6 6
# 7 3
# 8 7
# 9 6




# n = int(input())

# soo_set = {2:[1], 3:[7], 4:[4], 5: [2,3,5], 6:[0,6,9], 7:[8]}
# soo_lst = list(soo_set.keys())
# soo_rev_lst = sorted(soo_lst, reverse=True)
# # [2, 3, 4, 5, 6, 7]
# to_do = []
# for i in range(n):
#     to_do.append(int(input()))

# answer = []
# for soo in to_do:
#     tmp_soo = soo
#     soo_min = ''
#     while tmp_soo>8:
#         for digit in soo_rev_lst:
#             if tmp_soo >= digit:
#                 tmp_soo -= digit
#                 if min(soo_set[digit])==0:
#                     soo_min += str(soo_set[digit][1])
#                 else:
#                     soo_min += str(min(soo_set[digit]))
#                 break
#     if tmp_soo==8:
#         soo_min += '01'
#     else:
#         for digit in soo_rev_lst:
#             if tmp_soo >= digit:
#                 tmp_soo -= digit
#                 if min(soo_set[digit])==0:
#                     soo_min += str(soo_set[digit][1])
#                 else:
#                     soo_min += str(min(soo_set[digit]))
#                 break

#     tmp_soo_min = soo_min[::-1]

#     if soo>2:
#         soo_max = '7'*(soo%2) + '1'*((soo//2)-1)
#     else:
#         soo_max = '1'
    
#     answer.append((tmp_soo_min, soo_max))

# for i in answer:
#     print(i[0], i[1])