M = max(int(input()), 2)
N = int(input())
ans = []
for num in range(M, N+1):
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            break
    else:
        ans.append(num)
if ans:
    print(sum(ans))
    print(ans[0])
else:
    print(-1)
    