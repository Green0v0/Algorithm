# 3rd try:
def dsting(i, j, graph):
    chk = False # 거리두기 실패시 True
    for x in range(i-2, i+3):
        for y in range(j-2, j+3):
            if abs(x-i)+abs(y-j) <= 2 and x in range(5) and y in range(5)\
                and (x != i or y != j) and graph[x][y] == 'P':
                skip = False # 중간에 파티션 설치시 True
                if (x==i and graph[x][(y+j)//2]=='X')\
                    or (y==j and graph[(x+i)//2][y]=='X')\
                        or (x!=i and y!=j and graph[x][j]=='X' and graph[i][y]=='X'):
                        skip = True

                if not skip:
                    chk = True
                    break
    
    return chk


def solution(places):
    answer = []

    leng = len(places)
    for now in range(leng):
        now_ans = True
        place = places[now]
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and dsting(i, j, place):
                    now_ans = False
                    break

        answer.append(int(now_ans))

    return answer

# places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
#  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
#  ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], 
#  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
#  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

# places = [["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"]]

# places = [ ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"] ]

places = [["POOPX",
           "XXPXP",
           "PXXXX", 
           "OXXPX", 
           "OOOXP"]]

print(solution(places))







# # 1st try:
# def dsting(i, j, graph):
#     chk = False # 거리두기 실패시 True
#     for x in range(i-2, i+3):
#         for y in range(j-2, j+3):
#             if (x != i or y != j) and x in range(5) and y in range(5)\
#                 and abs(x-i)+abs(y-j) <= 2 and graph[x][y] == 'P':
#                 skip = False # 중간에 파티션 설치시 True
#                 for m in range(min(x, i), max(x, i)+1):
#                     for n in range(min(y, j), max(y, j)+1):
#                         if (m != i or n != j) and graph[m][n] == 'X':
#                             skip = True
#                 if not skip:
#                     chk = True
#                     break
    
#     return chk


# def solution(places):
#     answer = []

#     leng = len(places)
#     for now in range(leng):
#         now_ans = True
#         place = places[now]
#         for i in range(5):
#             for j in range(5):
#                 if place[i][j] == 'P' and dsting(i, j, place):
#                     now_ans = False
#                     break

#         answer.append(int(now_ans))

#     return answer










# # 2nd try:
# def dst(a, b):
#     return abs(a[0]-b[0]) + abs(a[1]-b[1])

# # def interup(a, c, b):
# #     ret = False
# #     if dst(a, b)==2:
# #         if a[0]==b[0] and a[0]==c[0]:
# #             ret = True
# #         elif a[1]==b[1] and a[1]==c[1]:
# #             ret = True
# #         elif (a[0]==c[0] and b[1]==c[1]) or (a[1]==c[1] and b[0]==c[0]):
# #             ret = True

# #     return ret

# def solution(places):
#     answer = []

#     for place in places:
#         ps = []
#         xs = []
#         for i in range(5):
#             for j in range(5):
#                 if place[i][j] == 'P':
#                     ps.append((i,j))
#                 elif place[i][j] == 'X':
#                     xs.append((i,j))

#         now_ans = True
#         for i in range(len(ps)):
#             to_break = False
#             for j in range(i+1, len(ps)):
#                 if dst(ps[i], ps[j]) == 1:
#                     now_ans = False
#                     to_break = True
#                     break 
#                 if dst(ps[i], ps[j]) == 2:
#                     tmp_ans = False
#                     if (ps[i][0]==ps[j][0] and (ps[i][0], (ps[i][1]+ps[j][1])//2) in xs)\
#                          or (ps[i][1]==ps[j][1] and ((ps[j][0]+ps[i][0])//2, ps[i][1]) in xs):
#                         tmp_ans = True
#                     elif (ps[i][0]!=ps[j][1] and ps[i][1]!=ps[j][0]) and (ps[i][0],ps[j][1]) in xs\
#                         and (ps[i][1],ps[j][0]) in xs:
#                         tmp_ans = True
#                     if tmp_ans == False:
#                         now_ans = False
#                         to_break = True
#                         break

#             if to_break:
#                 break
#                     # for k in range(len(xs)):
#                     #     if interup(ps[i], xs[k], ps[j]):
#                     #         now_ans = True
        
#         answer.append(int(now_ans))

#     return answer