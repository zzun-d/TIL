N = int(input())
cnt = 0
if N < 100:
    cnt = N
elif N == 1000:
    cnt = 144
else:
    cnt += 99
    for i in range(100, N+1):
        a = i % 10
        i = i // 10
        b = i % 10
        i = i // 10
        c = i % 10
        if a-b == b-c:
            cnt += 1
print(cnt)