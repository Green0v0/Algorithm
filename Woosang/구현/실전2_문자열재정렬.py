s = "K1KA5CB7"
s_num = "0123456789"

num_lst = []
s_lst = []
for i in s: # 문자열의 숫자와 문자 분리 작업
    if i in s_num:
        num_lst.append(int(i)) # 숫자는 정수형으로 변환
    else:
        s_lst.append(ord(i)) # 문자는 아스키코드 정수형으로 변환
s_lst.sort() # 아스키 문자 정렬

new_s = [chr(i) for i in s_lst] # 아스키코드 문자로 바꾸기
new_num = sum(num_lst)

print("".join(new_s) + str(new_num))