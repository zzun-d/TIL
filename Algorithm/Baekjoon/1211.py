import copy

for _ in range(10):
    t = int(input())
    ARR = [list(map(int, input().split())) for _ in range(100)]
    i_min = 0
    c_min = 10000
   
    for s_x in range(100):
        if ARR[0][s_x]:       
            arr = copy.deepcopy(ARR)
            cnt = 0
            x = s_x
            y = 0
            while y < 99:
                if x > 0 and arr[y][x-1]:
                    while x > 0 and arr[y][x-1]:
                        arr[y][x] = 0
                        x -= 1
                        cnt += 1
                elif x < 99 and arr[y][x+1]:
                    while x < 99 and arr[y][x+1]:
                        arr[y][x] = 0
                        x += 1
                        cnt += 1
                else:
                    y += 1
            if c_min > cnt:
                c_min = cnt
                i_min = s_x

    print(f'#{t} {i_min}')
