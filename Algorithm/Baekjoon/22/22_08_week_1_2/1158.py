N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]
ans = []
for i in range(N):
    ans.append(lst.pop((K-1)%(N-i)))
    lst = lst[(K-1)%(N-i):] + lst[:(K-1)%(N-i)]
print('<', end='')
for num in ans[:-1]:
    print(str(num)+', ', end='')
print(str(ans[-1]) + '>')

