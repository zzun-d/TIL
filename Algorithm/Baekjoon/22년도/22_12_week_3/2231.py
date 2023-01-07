N = input()
l = len(N)
N = int(N)

for i in range(N-9*l, N):
    if i < 0:
        continue
    sm = num = i
    while num:
        sm += num % 10
        num //= 10
    if sm == N:
        print(i)
        break
else:
    print(0)