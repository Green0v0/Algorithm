def solution(new_id):    
    # 1단계
    new_id = new_id.lower()

    # 2단계
    # spe_chars = ['-', '_', '.']
    # for char in new_id:
    #     if char.isupper() or char.isdigit() or char not in spe_chars:
    #         new_id = new_id.replace(char, '')
    
    spe_chars = ['-', '_', '.']
    to_del_lst = []
    newidset = list(set(new_id))
    for char in newidset:
        if char not in spe_chars and char in new_id and char not in to_del_lst\
            and not char.islower() and not char.isdigit():
            to_del_lst.append(char)
    to_del_lst = ''.join(to_del_lst)
    table = str.maketrans(to_del_lst, ' '*len(to_del_lst))
    new_id = new_id.translate(table)
    new_id = new_id.replace(' ', '')

    
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..','.')

    # 4단계
    new_id = new_id.strip('.')

    # 5단계
    if len(new_id) == 0:
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id.endswith('.'):
        new_id = new_id.rstrip('.')

    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))