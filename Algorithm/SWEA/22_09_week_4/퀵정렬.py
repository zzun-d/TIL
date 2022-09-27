def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[-1]
    i = -1
    j = 0
    while j < len(lst) - 1:
        if lst[j] > pivot:
            j += 1
            continue
        else:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
        j += 1
    i += 1
    lst[i], lst[-1] = lst[-1], lst[i]

    return quick_sort(lst[:i]) + lst[i:i+1] + quick_sort(lst[i+1:])

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f'#{tc} {quick_sort(lst)[N//2]}')