n = int(input())
lst = [int(input()) for _ in range(n)]
bag = []
ans = []
i = 1
j = 0
while i <= n+1:
    if bag:
        if bag[-1] != lst[j]:
            bag.append(i)
            ans.append('+')
            i += 1
        else:
            bag = bag[:-1]
            ans.append('-')
            j += 1
    else:
        bag.append(i)
        ans.append('+')
        i += 1
if bag[:-1]:
    print('NO')
else:
    print(*ans[:-1])

