def case_search(n):
    if case_lst[n]:
        return case_lst[n]
    else:
        case_lst[n] = case_search(n-1) + 2 * case_search(n-2)
        return case_search(n)

T = int(input())
case_lst = [0] * 31
case_lst[1] = 1
case_lst[2] = 3
for t in range(1, T+1):
    N = int(input())//10
    case_search(N)
    print(f'#{t} {case_lst[N]}')
