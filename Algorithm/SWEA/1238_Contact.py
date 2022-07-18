for t in range(10):
    N, S = list(map(int, input().split()))
    S = [S]
    nums = list(map(int, input().split()))
    set_nums = set([(nums[i*2], nums[i*2 + 1]) for i in range(N//2)])
    nums = list(set_nums)
    finished = []
    while True:
        call_reciver = []
        remove_nums = []
        state = 0
        for num in nums:
            if num[0] in S and num[1] not in finished:
                call_reciver.append(num[1])
                state = 1
                remove_nums.append(num)
        finished.extend(S)
        for num in remove_nums:
            nums.remove(num)
        if state == 0:
            break
        else:
            m_nums = max(call_reciver)
            S = call_reciver
            finished.extend(S)
            
    print(f'#{t+1} {m_nums}')