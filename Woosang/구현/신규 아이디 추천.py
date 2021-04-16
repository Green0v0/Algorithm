def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    del_list = []
    for i in range(len(new_id)):
        if new_id[i].isalnum() or new_id[i] in ['-', '_', '.']:
            continue
        else:
            del_list.append(new_id[i])
    
    while del_list:
        i = del_list.pop()
        new_id = new_id.replace(i, '')
    
    # 3단계
    for i in range(1, len(new_id)):
        if new_id[i] == '.' and new_id[i-1] == new_id[i]:
            del_list.append(i)
    new_id = list(new_id)
    
    while del_list:
        i = del_list.pop()
        new_id.pop(i)
    
    # 4단계
    def remove_comma(new_id):
        if len(new_id) != 0:
            if new_id[0] == '.':
                new_id = new_id[1:]
            elif new_id[-1] == '.':
                new_id = new_id[:-1]
        return new_id
    new_id = remove_comma(new_id)
    new_id = remove_comma(new_id)
    # 5단계, 6단계
    if len(new_id) == 0:
        new_id.append('a')
    elif len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = remove_comma(new_id)
    
    # 7단계
    if len(new_id) <= 2:
        new_id.append(new_id[-1]*(3-len(new_id)))
    
    return ''.join(new_id)