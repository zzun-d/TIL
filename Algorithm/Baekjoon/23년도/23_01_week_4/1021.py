def left(lst, cnt):
    lst = lst[1:] + lst[:1]
    return lst, cnt+1

def right(lst, cnt):
    lst = lst[-1:] + lst[:-1]
    return lst, cnt+1

N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]
cnt = 0
for n in map(int, input().split()):
    l = len(lst)
    n_idx = lst.index(n)

    if l//2 >= n_idx:
        while lst[0] != n:
            lst, cnt = left(lst, cnt)
        lst.pop(0)
    else:
        while lst[0] != n:
            lst, cnt = right(lst, cnt)
        lst.pop(0)
print(cnt)