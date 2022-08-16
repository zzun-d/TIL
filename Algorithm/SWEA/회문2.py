for _ in range(10):
    t = input()
    arr = [input() for _ in range(100)]
    
    ans = 0
    for l in range(100, 1, -1):
        for i in range(100-l+1):
            for j in range(100):
                tmp = True
                for k in range(l//2):
                    if arr[j][i+k] != arr[j][i+l-k-1]:
                        tmp = False
                        break
                if tmp:
                    ans = l
                    break
            if tmp:
                break
        if tmp:
            break
    
    tmp = True
    for l in range(100, ans, -1):
        for i in range(100-l+1):
            for j in range(100):
                tmp = True
                for k in range(l//2):
                    if arr[i+k][j] != arr[i+l-k-1][j]:
                        tmp = False
                        break
                if tmp:
                    ans = l
                    break
            if tmp:
                break
        if tmp:
            break
    print(f'#{t} {ans}')
        
                    

