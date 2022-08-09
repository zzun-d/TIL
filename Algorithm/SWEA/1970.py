T = int(input())
for t in range(1, T+1):
    c = int(input())
    cnt = []
    for money in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        cnt.append(c//money)
        c = c % money
    print(f'#{t}')
    print(*cnt)