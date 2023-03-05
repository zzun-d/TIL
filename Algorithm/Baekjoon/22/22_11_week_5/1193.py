N = int(input())
x = 1
cnt = 1
while N > x:
    cnt += 1
    x += cnt
if cnt%2:
    print(f'{x - N+1}/{cnt - (x - N)}')
else:
    print(f'{cnt - (x - N)}/{x - N+1}')