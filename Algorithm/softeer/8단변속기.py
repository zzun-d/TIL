lst = input().split()
ascending = '1234567'
descending = '8765432'
if lst[0] == '1':
    for i in range(1, 7):
        if lst[i] != ascending[i]:
            print('mixed')
            break
    else:
        print('ascending')

elif lst[0] == '8':
    for i in range(1, 7):
        if lst[i] != descending[i]:
            print('mixed')
            break
    else:
        print('descending')
        
else:
    print('mixed')
 