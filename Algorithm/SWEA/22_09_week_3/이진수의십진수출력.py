T = int(input())

for tc in range(1, T+1):
    nums = input()
    results = []
    for i in range(0, len(nums), 7):
        result = 0
        for j in range(7):
            result += int(nums[i+j])*(2**(6-j))
        results.append(result)
    print(f'#{tc}', *results)
