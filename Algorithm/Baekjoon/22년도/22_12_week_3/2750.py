N = int(input())
lst = []
for _ in range(N):
    n = int(input())
    for i in range(len(lst)):
        if lst[i] >= n:
            lst = lst[:i] + [n] + lst[i:]
            break
    else:
        lst.append(n)
for l in lst:
    print(l)