def len(st):
    ans = 0
    for s in st:
        ans += 1
    return ans


for _ in range(10):
    t = int(input())
    s_s = input()
    S = input()
    ans = 0
    for i in range(len(S) - len(s_s) + 1):
        if S[i:i+len(s_s)] == s_s:
            ans += 1
    print(f'#{t} {ans}')