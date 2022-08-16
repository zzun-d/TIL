prob = list(input())
v = []
l_p = []
results = []
ans = []
for idx, p in enumerate(prob):
    if p == '(':
        l_p.append([p, idx])
    elif p == ')':
        v.append([l_p.pop()[1], idx])

for i in range(1<<len(v)):
    result = []
    for j in range(len(v)):
        if i & (1 << j):
            result.append(v[j])
    if result:
        results.append(result)
for result in results:
    idxs = []
    p = prob[:]
    for r in result:
        idxs.append(r[0])
        idxs.append(r[1])
    idxs.sort(reverse=True)
    for idx in idxs:
        p = p[:idx] + p[idx+1:]
    ans.append(p)
result = []
for answer in ans:
    result.append(''.join(answer))
result = list(set(result))
result.sort()
for r in result:
    print(r)