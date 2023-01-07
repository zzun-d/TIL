def b_sort(lst, l):
    for i in range(l-1):
        for j in range(l-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

T= int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    scores = b_sort(scores, N)
    ans = 0
    
    for i in range(1, K+1):
        ans += scores[-i]

    print(f'#{t} {ans}')
