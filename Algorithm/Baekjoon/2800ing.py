from itertools import combinations

def remove_cover(s, idx):
    return s[:idx[0]] + s[idx[0]+1:idx[1]] + s[idx[1]+1:]
    

prob = input()
ans = []
l_p = []
results = []
for idx, p in enumerate(prob):
    if p == '(':
        l_p.append([p, idx])
    elif p == ')':
        ans.append([l_p.pop()[1], idx])

for i in range(1<<len(ans)):
    result = []
    for j in range(len(ans)):
        if i & (1 << j):
            result.append(ans[j])
    if result:
        results.append(result)

