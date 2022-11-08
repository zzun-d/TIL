message = input()
key = input()
key_chars = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
key_setting = ''
key_visited = set()
for k in key:
    if key_visited.intersection({k}):       # 방문한 문자면 continue
        continue
    
    else:
        key_visited.add(k)
        key_setting += k
        key_chars = key_chars.replace(k, '')

key_setting += key_chars
        
msgs = []
while message:
    if len(message) >= 2:
        if message[0] != message[1]:
            msgs.append(message[:2])
            message = message[2:]
            
        
        
        elif message[0] == 'X':
            msgs.append('XQ')
            message = message[1:]

        else:
            msgs.append(message[0] + 'X')
            message = message[1:]
    
    else:
        msgs.append(message[0] + 'X')
        message = False
answer = ''

for old_1, old_2 in msgs:
    old_1_row = key_setting.index(old_1)//5
    old_2_row = key_setting.index(old_2)//5

    old_1_col = key_setting.index(old_1)%5
    old_2_col = key_setting.index(old_2)%5

    if old_1_row == old_2_row:
        if old_1_col < 4:
            new_1 = key_setting[(old_1_row * 5 + old_1_col + 1)]
        else:
            new_1 = key_setting[(old_1_row * 5)]
    
        if old_2_col < 4:
            new_2 = key_setting[(old_2_row * 5 + old_2_col + 1)]
        else:
            new_2 = key_setting[(old_2_row * 5)]

    elif old_1_col == old_2_col:
        if old_1_row < 4:
            new_1 = key_setting[((old_1_row + 1) * 5 + old_1_col)]
        else:
            new_1 = key_setting[old_1_col]
    
        if old_2_row < 4:
            new_2 = key_setting[((old_2_row + 1) * 5 + old_2_col)]
        else:
            new_2 = key_setting[old_2_col]

    else:
        new_1 = key_setting[(old_1_row * 5) + old_2_col]
        new_2 = key_setting[(old_2_row * 5) + old_1_col]
    
    answer += new_1 + new_2

print(answer)