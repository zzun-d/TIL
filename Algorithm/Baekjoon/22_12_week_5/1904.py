N = int(input())

if N < 3:
    print(N)

else:
    post = 2
    now = 3
    for i in range(4, N+1):
        now, post = (now+post)%15746, now%15746
        
    print(now)