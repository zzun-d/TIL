T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if N > M:          # a 길이가 b 보다 크면 a <-> b, N <-> M
        a, b = b, a
        N, M = M, N
    ans = sum([a[i] * b[i] for i in range(N)])    # ans 초기값 각 인덱스 0부터

    for i in range(M - N):     # 리스트 길이 차이만큼 인덱스 옮겨가며 진행
        cross_sum = sum([a[j] * b[j+i+1] for j in range(N)])
        if cross_sum > ans:
            ans = cross_sum
    print(f'#{t} {ans}')