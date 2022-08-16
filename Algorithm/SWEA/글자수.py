T = int(input())
for t in range(1, T+1):
    s1 = list(input())
    s2 = input()
    s1 = set(s1)
    s_dict = {}
    for s in s2:
        if s_dict.get(s):
            s_dict[s] += 1
        else:
            s_dict[s] = 1
    ans = 0
    for s in s1:
        if s_dict.get(s):
            if s_dict[s] > ans:
                ans = s_dict[s]
    print(f'#{t} {ans}')
