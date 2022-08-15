def remove_cover(s, idx):
    return s[:idx[0]] + s[idx[0]+1:idx[1]] + s[idx[1]+1:]
    

prob = input()
ans = []
l_p = []
result = []
for idx, p in enumerate(prob):
    if p == '(':
        l_p.append((p, idx))
    elif p == ')':
        ans.append((l_p.pop()[1], idx))
for i in range(1<<10):
    for j in range(10):
        if i & (1<<j):
            print(remove_cover(prob, ans[j]))

