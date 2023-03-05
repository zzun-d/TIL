lst = input()
cnt = 0
n = 0
result = ''
tmp = True
while cnt < len(lst):
    if lst[cnt] == 'X':
        n += 1
    else:
        if n%2:
            print(-1)
            tmp = False
            break
        else:
            if n%4:
                result += 'AAAA'*(n//4) + 'BB' + '.'
            else:
                result += 'AAAA'*(n//4) + '.'
        n = 0
    cnt += 1
if n%2 and tmp:
    print(-1)
    tmp = False
    
else:
    if n%4:
        result += 'AAAA'*(n//4) + 'BB'
    else:
        result += 'AAAA'*(n//4)
    
if tmp:
    print(result)
