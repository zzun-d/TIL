T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mx = 0
    if len(A) > len(B):
        A, B = B, A

    for i in range(len(B)-len(A)+1):
        sm = 0
        for j in range(len(A)):
            sm += A[j]*B[i+j]
        if sm > mx:
            mx = sm
    print(f'#{tc} {mx}')

