N = int(input())
nums = list(map(int, input().split()))
bal_num = [i for i in range(1, N+1)]
ans = []
now = 0
for i in range(N):    
    ans.append(bal_num.pop(now))
    mv = nums.pop(now)
    if mv > 0:
        now = (now + mv) % (N-i) - 1
    else:
        now += mv
    if now < 0 :
        now = (N-i-1) + now
print(ans)