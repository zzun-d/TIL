T = int(input())
for t in range(1, T+1):
    A, B = input().split()
    l_A = len(A)
    l_B = len(B)
    ans = l_A
    i = 0
    while i < l_A-l_B+1:
        if A[i:i+l_B] == B:
            ans -= l_B - 1
            i += l_B
        else:
            i += 1
    print(f'#{t} {ans}')