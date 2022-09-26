def merge(lst):
    global cnt
    l = len(lst)
    if l == 1:
        return lst
    else:
        left = lst[:l//2]
        right = lst[l//2:]
        if max(left) > max(right):
            cnt += 1
        merge(left)
        merge(right)



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    merge(lst)
    lst.sort()
    print(f'#{tc} {lst[N//2]} {cnt}')