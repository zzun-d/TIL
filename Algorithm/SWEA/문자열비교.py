T = int(input())
for t in range(1, T+1):
    str_1 = input()
    str_2 = input()
    if str_1 in str_2:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')