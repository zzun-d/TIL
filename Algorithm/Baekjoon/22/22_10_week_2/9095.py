def find(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return find(n-1) + find(n-2) + find(n-3)

T = int(input())
for _ in range(T):
    N = int(input())
    print(find(N))