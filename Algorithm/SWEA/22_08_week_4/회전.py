T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = input().split()
    print(f'#{t} {lst[M%N]}')