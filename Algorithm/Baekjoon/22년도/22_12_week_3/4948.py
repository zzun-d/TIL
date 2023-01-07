lst = [-1] * ((123456*2) + 1)
while True:
    n = int(input())
    if n == 0:
        break
    ans = 0
    
    for num in range(n + 1, 2*n + 1):
        if lst[num] >= 0:
            if lst[num] == 1:
                ans += 1
            continue
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                lst[num] = 0
                break
        else:
            lst[num] = 1
            ans += 1
    
    print(ans)