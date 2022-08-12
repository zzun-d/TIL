T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for row in arr:
        nums = [False] * 9
        for r in row:
            nums[r-1] = True
        if all(nums):
            continue
        else:
            ans = 0
            break
    for i in range(9):
        nums = [False] * 9
        for j in range(9):
            nums[arr[j][i]-1] = True
        if all(nums):
            continue
        else:
            ans = 0
            break
    
    for k in range(0, 7, 3):
        for l in range(0, 7, 3):
            nums = [False] * 9
            for i in range(3):
                for j in range(3):
                    nums[arr[i+l][j+k]-1] = True
            if all(nums):
                continue
            else:
                ans = 0
                break
    
    
    print(f'#{t} {ans}')
            