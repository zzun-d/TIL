N = int(input())
ans = [666]
i = 1665
while len(ans) < N:
    if str(i).count('666') >= 1:
        ans.append(i)
    i += 1
print(ans[N-1])