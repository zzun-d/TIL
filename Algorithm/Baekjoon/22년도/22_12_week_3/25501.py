N = int(input())
for _ in range(N):
    s = input()
    cnt = 1
    tmp = 1
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            tmp = 0
            break
        l += 1
        r -= 1
        cnt += 1
    print(tmp, cnt)