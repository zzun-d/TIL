for t in range(1, 11):
    N, S = input().split()
    while True:
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                S = S[:i] + S[i+2:]
                break
        else:
            break
    print(f'#{t} {S}')

