T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input()))
    if nums[0] == 1:
        tmp = True
        cnt = 1
        ans = 1
    else:
        tmp = False
        cnt = 0
        ans = 0

    for num in nums[1:]:
        if num and tmp:
            cnt += 1
            if ans < cnt:
                ans = cnt
        elif num:
            cnt = 1
            tmp = True
        else:
            cnt = 0
    print(f'#{t} {ans}')